# SSH / Password
`ssh cyborg4@cyborg.underthewire.tech / 88_objects`
# Instructions
The password for cyborg5 is the PowerShell module name with a version number of 8.9.8.9 PLUS the name of the file on the desktop.
# Method of solve
```Powershell
Get-Module -ListAvailable | Where-Object {$_.Version -eq "8.9.8.9"}
```
* the password is `bacon_eggs`
