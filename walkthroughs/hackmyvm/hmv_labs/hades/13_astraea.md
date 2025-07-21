# username
astraea
# password
nZkEYtjvHElOtupXKzTE
# mission contents
N/A
# method of solve
* We are logged out upon login when we use astaea credentials
* If we look at the `/etc/ssh/sshd_config` using another account, we see that astraea doesn't have a standard SSH shell
* Turns out there's a busybox binary on this server, and we can use that to enumerate other open ports on the localhost
* There's an FTP server running on localhost, so we use astraea's credenetials on localhost FTP, but first we have to move into a public writable directory
```
cat /etc/ssh/sshd_config
find / -name busybox 2>/dev/null
/var/tmp/busybox netstat -tulpn
mkdir 
ftp localhost
cd /pwned/astraea
ls -la
get atalanta.txt
get mission.txt
```
