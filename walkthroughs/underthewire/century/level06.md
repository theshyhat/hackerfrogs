# SSH Command / Password
ssh century6@century.underthewire.tech underthewire3347
# Description
The password for Century7 is the number of folders on the desktop.
# Concept
* counting files / folders using Powershell
# Method of solve
* use this command to count the number of folders in the current directory:
```
(Get-ChildItem -Path . -Directory).Count
```






