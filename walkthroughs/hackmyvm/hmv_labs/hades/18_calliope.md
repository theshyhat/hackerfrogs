# username
calliope
# password
access via SSH private key
# mission contents
The user calypso often uses write to communicate.
# method of solve
* there's a SUID binary in our home directory called `writeme`
* through some guessing, we think it might be a SUID version of the Linux `write` binary, which allows users to send messages to each other
* to check if we can receive messages through `write`, we need to use the `mesg` command:
```
mesg
```
* this command lets us knows what our sessions settings are for receiving messages from `write`
* to enable messages, we run this command:
```
mesg y
```
* and now we can get the password
