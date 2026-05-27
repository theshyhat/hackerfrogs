# URL
https://learn.cylabacademy.org/library/759
# Concept
* accessing an SMB file share
# Method of solve
* we have to interface with a network printer, which usually means it's using the SMB protocol
* we can use the following `smbclient` command to enumerate the server's fileshares
```
smbclient -L //mysterious-sea.picoctf.net -N -p <PORT_NUMBER>
```
* we see there is a `/shares` share, so we can access it using this command
```
smbclient //mysterious-sea.picoctf.net/shares -N -p <PORT_NUMBER>
```
* we don't need to supply a password, so just press enter
* once we're in, we look at the file share contents, then download the `flag.txt` file and get out
```
dir
get flag.txt
exit
```
* lastly, we read the flag
```
cat flag.txt
```





