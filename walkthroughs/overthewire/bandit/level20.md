# username
bandit20
# password
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
# objective
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).
# method of solve
This SUID binary will connect to a specified port, and if the port service provides the password for the current level as output, the binary will then output the password for bandit 21, so the first step is to setup a listener on a localhost port:
```
echo '0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO' | nc -nlvp 1234
```
Then we use the suconnect binary to access the listener we set up:
```
./suconnect 1234
```
