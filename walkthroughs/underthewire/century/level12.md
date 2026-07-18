# SSH Command / Password
`ssh century12@century.underthewire.tech / secret_sauce`
# Instructions
The password for Century13 is the description of the computer designated as a Domain Controller within this domain PLUS the name of the file on the desktop.
# Method of solve
* the first thing we need to is get the details of the Domain Controller in our environment:
```
Get-ADDomainController
```
* the identity of the computer is `UTW`. We can feed this into the next command:
```
Get-ADComputer -Identity UTW -Properties Description | Select-Object Name, Description
```
* so we can combine the description with the file name on the Desktop
