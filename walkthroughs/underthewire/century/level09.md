# SSH Command / Password
ssh century9@century.underthewire.tech 696
# Description
The password for Century10 is the 161st word within the file on the desktop.
# Method solve
* what we need to do is split the contents of the file into an array, and then reference the correct index in the array
```PowerShell
((Get-Content -Path "C:\users\century9\desktop\Word_File.txt") -split " ")[160]
```


