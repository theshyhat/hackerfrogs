# username
century2
# password
10.0.14393.7870
# objective
> The password for Century3 is the name of the built-in cmdlet that performs the wget like function within PowerShell PLUS the name of the file on the desktop.
* NOTE:
* If the name of the cmdlet is “get-web” and the file on the desktop is named “1234”, the password would be “get-web1234”.
* The password will be lowercase no matter how it appears on the screen.
# method of solve
Through research, we find that the `wget` command is actually an alias for the `Invoke-WebRequest` cmdlet, and the name of the file on the desktop is `443`, which we can obtain by using the following command:
```
dir
```
Considering that the password is always lowercase, no matter what, that means the password is `invoke-webrequest443`
