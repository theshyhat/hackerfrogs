# SSH / Password
`ssh cyborg1@cyborg.underthewire.tech / kansas`
# Instructions
The password for cyborg3 is the host A record IP address for CYBORG718W100N PLUS the name of the file on the desktop.
# Method of solve
```Powershell
Resolve-DnsName -Name CYBORG718W100N
```
* altogether, the password is `172.31.45.167_ipv4`
