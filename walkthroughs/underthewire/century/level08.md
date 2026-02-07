# SSH Command / Password
ssh century8@century.underthewire.tech point7
# Description
The password for Century9 is the number of unique entries within the file on the desktop.
# Concept
* counting unique lines in a file
# Method of solve
* we can use this command to get the number of unique lines in a file:
```
(Get-Content -Path .\unique.txt | Sort-Object -Unique).Count
```


