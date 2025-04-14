# username
bandit17
# password
Use the SSH private key from the previous level
# objective
See which line in has changed between the passwords.old file and the passwords.new file
# method of solve
Use the diff command to see what line has changed:
```
diff passwords.old passwords.new
```
