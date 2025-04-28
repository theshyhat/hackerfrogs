# username
bandit25
# password
iCi86ttT4KSNe1armKiwbQNmB3YJP3q4
# objective
Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.
# method of solve
The bandit26 user doesn't use a standard shell, but we can lookup what shell they use with the following command
```
cat /etc/passwd | grep bandit26
```
Then we can find out what kind of file we're dealing with
```
file /usr/bin/showtext
```
It's a shell script file. Let's inspect it
```
cat /usr/bin/showtext
```
This script uses the `more` command to a read a file. We could potentially break out of the `more` command if whatever we're reading is larger than what can fit on the screen. We're given an SSH key to login as `bandit26`, so we copy the key contents to our desktop and create the key. Then we make the terminal text *really* big and use the following command to login
```
ssh -i bandit26.key bandit26@bandit.labs.overthewire.org -p 2220
```
If we're in the middle of the `more` command, we can use the `v` key to switch into the VIM text editor. From there, we could use the `:shell` command to open an interactive shell, but the shell is set to the `showtext` file. We can set a new shell for the session like this:
```
:set shell=/bin/bash
```
Then open the shell
```
:shell
```
From here, we can read the password for Bandit26 in the usual location
```
cat /etc/bandit_pass/bandit26
```
