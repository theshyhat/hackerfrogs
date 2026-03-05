# SSH Command / Password
ssh century10@century.underthewire.tech / pierid
# Instructions
The password for Century11 is the 10th and 8th word of the Windows Update service description combined PLUS the name of the file on the desktop.
# Method of solve
* the first thing we need to confirm is the name of the file on the desktop: `110`
* the second thing we need to do is get the description of the Windows Update service
  * the common name of this service is "Windows Update", but the "service name" of this service is `wuauserv`
* we can use the `Get-CimInstance` cmdlet to retrieve the description for the service:
```PowerShell
Get-CimInstance Win32_Service -Filter 'Name = "wuauserv"' | Select-Object Name, Description
```
* now we need to find a way to select only the 10th and 8th word, and also select the name of the file to concat them all together:
```PowerShell
((Get-CimInstance Win32_Service -Filter 'Name = "wuauserv"').Description -split "\s+")[9] + ((Get-CimInstance Win32_Service -Filter 'Name = "wuauserv"').Description -split "\s+")[7] + (Get-ChildItem -Path "C:\users\century10\desktop\110").Name
```
