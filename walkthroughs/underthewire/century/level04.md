# username
century4
# password
123
# description
The password for Century5 is the name of the file within a directory on the desktop that has spaces in its name.
# Concept
* searching for files with spaces in its name with Powershell
# method of solve
* use this Powershell command to recursively output the files in the current directory:
```
Get-ChildItem -Recurse -Path . -File
```
