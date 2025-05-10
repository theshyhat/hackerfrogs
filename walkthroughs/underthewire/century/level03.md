# username
century3
# password
invoke-webrequest443
# objective
The password for Century4 is the number of files on the desktop.
# method of solve
The following will output the number of files in the current directory `C:\users\century3\desktop`
```
Write-Host ( Get-ChildItem C:\users\century3\desktop | Measure-Object ).Count
```
The answer is `123`
