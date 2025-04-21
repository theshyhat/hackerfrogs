# username
bandit18
# password
x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
# objective
The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.
# method of solve
The system logs you out as soon as you login, so we can run SSH with an argument to read the password file as soon as we login:
```
ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
```
