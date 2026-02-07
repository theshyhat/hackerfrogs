# SSH Command / Password
ssh century7@century.underthewire.tech 197
# Description
The password for Century8 is in a readme file somewhere within the contacts, desktop, documents, downloads, favorites, music, or videos folder in the user’s profile.
# Concept
* looking for a file in or under the current directory
# Method of solve
* we need to locate the readme file:
```
Get-ChildItem -Recurse -Path ..\ -File
```
* there's only one file:
```
type C:\users\century7\Downloads\Readme.txt
```





