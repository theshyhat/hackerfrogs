# username
bandit22
# password
tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q
# objective
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.
# method of solve
This is similar to the previous level. Let's take a look at the cronjob:
```
cat /etc/cron.d/cronjob_bandit23
```
And then the script:
```
cat /usr/bin/cronjob_bandit23.sh
```
This scripts turns a phrase into an md5 hash, then uses that hash as a file name in the /tmp directory, so we can use a similar process to read the file:
```
cat /tmp/$(echo 'I am user bandit23' | md5sum | cut -d ' ' -f 1)
```
