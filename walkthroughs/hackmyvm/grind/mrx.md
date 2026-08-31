# URL
https://hackmyvm.eu/hmvgrind/m1st3rx.php
# Concept
* SUID binaries
* SSH brute forcing
* sensitive data in scripts
* 
# Method of solve
## Q1 This server used to host a website. Everything suggests the logs are still there. We need the full log path.
* the logs for websites on Linux web servers are stored in the `/var/log` directory
* the answer is /var/log/access.log
## Q2 I'm sure you found a valid password among all of them. What is it?
* first cut the output from the log file and get just the passwords:
```
cat access.log | grep user | awk '{print $11}' | cut -d '=' -f 3 | awk 'NF'
```
* we put this into a `pass.txt` file
* and then we put all the users (helix, nova, mrx) into another file called `users.txt`
* finally, we use those two files to do a brute force attack with the Hydra tool
```
hydra -L users.txt -P pass.txt -t 32 -s 6962 hxc0.hackmyvm.eu ssh
```
* the password is `Wintermute!`
## Q3 It seems that user had more privileges than they should have. Which binary did you use to gain access? (full path)
* if we use the `sudo -l` command, we see that we have full sudo access as the `nova` user:
```
sudo -u nova sh
```
* the answer is `/usr/bin/sudo`
## Q4 The current user belongs to an interesting group. Find the password used by the next user and tell us.
* if we run the `id` command, we see that we're part of a group called `dev`
* we find all of that group's files
```
find / -group dev 2>/dev/null
```
* we're directed towards a file called `/opt/dev/backup.sh`
* the contents of the script have credentials for the `mrx` user: `ImmisterX.`
## Q5 The only thing we are interested in now is the content of /sensitiveinfo.txt.
* there is a SUID binary that runs as root, and we can find with this command:
```
find / -perm -4000 2>/dev/null
```
* so we can just run the binary we find to get the contents of `/sensitiveinfo.txt`
* `/usr/local/bin/sensitive`
