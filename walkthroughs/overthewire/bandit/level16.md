# username
bandit16
# password
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
# objective
The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000
# method of solve
The first thing we need to do is figure out which ports in the range are hosting the SSL service:
```
nmap -p31000-32000 -vv -sV localhost
```
One of the ports is serving SSL, so we send that port the password
```
echo 'kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx' | openssl s_client -quiet -connect localhost:31790
```
We receive a SSH private key as the response, so we'll need to create a private key for the next level
