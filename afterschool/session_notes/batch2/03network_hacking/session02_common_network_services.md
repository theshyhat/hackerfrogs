# HackerFrogs AfterSchool Network Hacking Session 2
## Session Topic: Common Network Services? /w TryHackMe
# Challenge 1: TryHackMe 25 Days of Cyber Security - Task 11
## TryHackMe Link (Task 11)
https://tryhackme.com/room/learncyberin25days
### YouTube Walkthrough Link
https://youtu.be/9T8DC95PoxM?t=1049
### Method of Solve
* Step 1: click on the Task 11 header
* Step 2: click on the green `Start Machine` button
* Step 3: go to the top of the webpage, and click on the "Start AttackBox" button located underneath the cloud icon with the santa hat on it
* Step 4: wait 2 minutes for the AttackBox to finish loading
* Step 5: at the top of the webpage, copy the IP address under the `Target IP Address`. You can click on the icon to the right of the IP address to copy it to your clipboard
* Step 6: click on the control bar located in the middle of the screen, then click on the clipboard button
* Step 7: in the AttackBox desktop, click on the terminal shortcut button to open a terminal
* Step 8: paste the IP address into the terminal, then use the `ping` command like the following:
```
ping -c 4 <ip_address>
```
If we can contact the IP address, then we should see that the program report that all of the packets were received
* Step 9: Use the following command to ping sweep the network range with the target machine and see what other machines are online
```
nmap -sn 10.10.11.0/24
```
You should see a few different IP addresses on the network return as `Host is up`
* Step 10: Use the following command to see the networking information of the AttackBox:
```
ip a
```
The `inet` value under the `ens5` networking interface is our IP address on the network.
* Step 11: Use the following command to scan the target machine using the Nmap program:
```
nmap -vv -sCV -p- -T4 <IP_address>
```
In the Nmap output, you should see that there are three ports open on the machine, 3389, 80, and 2222
