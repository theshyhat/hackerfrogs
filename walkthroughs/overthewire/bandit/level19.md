# username
bandit19
# password
cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8
# objective
To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.
# method of solve
This SUID binary runs as the bandit20 user. We know from the documentation the password is in the /etc/bandit_pass directory
```
./bandit20-do cat /etc/bandit_pass/bandit20
```
