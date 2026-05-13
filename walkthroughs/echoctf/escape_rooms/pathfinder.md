# URL
https://echoctf.red/target/73
# Concepts
* privilege escalation using misconfigured sudo commands
* privilege escalation using insecure custom binaries
# Method of solve
## Opportunity User
* our first user is named `opportunity`
* this user has sudo access with the `ls` command in the context of the `curiosity` user
* we can use this command to access the password for the `curiosity` user because it's just sitting in their home directory:
```
sudo -u curiosity /bin/ls /home/curiosity
```
## Curiosity User
* this user has sudo permissions with the `insight` user with the `/usr/local/sbin/insight` binary
* 
## Insight User






