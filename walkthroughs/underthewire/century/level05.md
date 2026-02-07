# SSH Command / Password
ssh century5@century.underthewire.tech 15768
# Description
The password for Century6 is the short name of the domain in which this system resides in PLUS the name of the file on the desktop.

- If the short name of the domain is “blob” and the file on the desktop is named “1234”, the password would be “blob1234”.
- The password will be lowercase no matter how it appears on the screen.
# Concept
* retrieving a computer's short domain name, i.e., its NetBIOSName
# Method of solve
* we use this Powershell command to retrieve only the NetBIOSName for the system:
```
Get-ADDomain | Select-Object -Property NetBIOSName
```
* we combine this with the name of the file on the desktop
```
dir
```


