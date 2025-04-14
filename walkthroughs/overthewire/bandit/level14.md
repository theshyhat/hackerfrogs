# username
bandit14
# password
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
# method of solve
The instructions tell us we need to send the password for the current level to localhost port 30000. We can do so with the netcat program
```
nc localhost 30000
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
```
We can also do this as a one-liner if we use the echo and a pipe:
```
echo 'MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS' | nc localhost 30000
```
