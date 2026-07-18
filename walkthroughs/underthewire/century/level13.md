# SSH Command / Password
`ssh century13@century.underthewire.tech / i_authenticate_things`
# Instructions
The password for Century14 is the number of words within the file on the desktop.
# Method of solve
```
Get-Content .\countmywords | Measure-Object -Word
```
