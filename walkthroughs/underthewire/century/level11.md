# SSH Command / password
ssh century11@century.underthewire.tech / windowsupdates110
# Instructions
The password for Century12 is the name of the hidden file within the contacts, desktop, documents, downloads, favorites, music, or videos folder in the user’s profile.
# Method of solve
* we need to search recursively inside certain directories in the User's home directory:
```Powershell
Get-ChildItem -Path ".\contacts", ".\desktop", ".\documents", ".\downlo
ads", ".\favorites", ".\music", ".\videos" -Recurse -Hidden -File -ErrorAction SilentlyContinu
e
```
