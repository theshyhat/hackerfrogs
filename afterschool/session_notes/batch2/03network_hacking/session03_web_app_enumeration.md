# HackerFrogs AfterSchool Network Hacking Session 3
## Session Topic: Web App Enumeration? /w TryHackMe
# Challenge 1: TryHackMe DVWA Room
## TryHackMe Link
https://tryhackme.com/room/dvwa
### YouTube Walkthrough Link
https://youtu.be/9T8DC95PoxM?t=1049
### Method of Solve
* Step 1: click on the Task 1 header
* Step 2: click on the green `Start Machine` button
* Step 3: go to the top of the webpage, and click on the `Start AttackBox` button located underneath the DVWA graphic
* Step 4: wait 2 minutes for the AttackBox to finish loading
* Step 5: at the top of the webpage, copy the IP address under the `Target IP Address`. You can click on the icon to the right of the IP address to copy it to your clipboard
* Step 6: click on the control bar located in the middle of the screen, then click on the clipboard button
* Step 7: in the AttackBox desktop, click on the terminal shortcut button to open a terminal
* Step 8: paste the IP address into the terminal, then use the `dirb` command like the following:
```
dirb <ip_address>
```
From the output we identify a number of different directories and webpages on the web server
* Step 9: Use the following `nikto` command to get more info about the web server
```
nikto -h http://<ip_address>
```
We get some different output from this program, including the webserver software being used, and its software version.
* Step 10: Use the following `gobuster` command to do a better directory busting attack on the webserver
```
gobuster dir -u http://<ip_address> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,zip,bak,txt
```
Note how we get a lot more results than when we scanned the web app using the `dirb` program
