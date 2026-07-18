# SSH / Password
ssh century14@century.underthewire.tech / 755
# Instructions
The password for Century15 is the number of times the word “polo” appears within the file on the desktop.
* note, whole word only, not part of other words
# Method of solve
```Powershell
(get-content .\countpolos) -split " " | sls -Pattern "^polo$" | measure-object
```
