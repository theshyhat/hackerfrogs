# username
bandit20
# password
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
# objective
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).
# method of solve
The first step we should do is figure out which ports are listening on the localhost
```
netstat -tulpn
```
Next, we use Nmap to scan the ports and see what services are running on those ports
```
nmap -vv -sV -T5 -p2232,2231,2230,2220,22,31046,31691,31960 localhost
```

