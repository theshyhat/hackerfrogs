# username
bandit13
# password
FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
# method of solve
Use the SSH private key to login to the next level
```
scp -P 2220 bandit13@bandit.labs.overthewire.org:/home/bandit13/sshkey.private .
chmod 600 sshkey.private
ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
cat /etc/bandit_pass/bandit14
```
