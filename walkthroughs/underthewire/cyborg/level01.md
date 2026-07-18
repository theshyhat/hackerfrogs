# SSH / Password
ssh cyborg1@cyborg.underthewire.tech / cyborg1
# Instructions
The password for cyborg2 is the state that the user Chris Rogers is from as stated within Active Directory.
# Method 
* we want to get the AD user for Chris Rogers
```Powershell
Get-ADUser -Filter "GivenName -eq 'Chris' -and Surname -eq 'Rogers'" -Properties State
```
