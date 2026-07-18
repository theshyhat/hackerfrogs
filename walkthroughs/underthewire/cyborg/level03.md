# SSH / Password
ssh cyborg3@cyborg.underthewire.tech / 172.31.45.167_ipv4
# Instructions
The password for cyborg4 is the number of users in the Cyborg group within Active Directory PLUS the name of the file on the desktop.
# Method of solve
```Powershell
(Get-ADGroupMember -Identity "Cyborg").Count
```
* the password is `88_objects`
