# open ports
22, 80
# initial access
* when we look at the sourcecode for the web app landing page, we see that there's a hidden endpoint `/hidden/.shell.php`
* when we navigate there, we test out the default web shell URL parameter `cmd`, and it works
* we upload a reverse shell binary and execute it, giving us reverse shell access
# privilege esclation
* there's an unusual SUID binary among the list, `python3.8`, and it's owned by `root`
* so we can use this payload to get `root` shell access
```
/usr/bin/python3.8 -c 'import os; os.execl("/bin/bash", "sh", "-p")'
```
