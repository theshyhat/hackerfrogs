# HackerFrogs AfterSchool Network Hacking Session 3
## Session Topic: Web App Enumeration? /w TryHackMe
# Challenge 1: TryHackMe 25 Days of Cyber Security - Task 11 (FTP)
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
* Step 9: Use the following FTP command to see the contents of the directory
```
ls
```
We see a few different directories, but there seems to only be one directory with content, the `public` directory
* Step 10: Use the following command to move into the `public` directory in FTP
```
cd public
```
* Step 11: Use the following command to see the directory contents
```
ls
```
There are two files in the directory, `backup.sh`, and `shoppinglist.txt`
* Step 12: Download the two files with the following two commands:
```
get backup.sh
get shoppinglist.txt
```
Now that we've downloaded the files, we can exit the server and look at the file contents
* Step 13: Use the following command to exit the FTP server
```
exit
```
* Step 14: Read the `shopping.txt` file with the following command
```
cat shoppinglist.txt
```
* Step 15: Go to the TryHackMe webpage, and navigate to the top of the webpage, and under the red Target Machine Information header, click on the red `Terminate` button
# Challenge 2: TryHackMe 25 Days of Cyber Security - Task 12 (SMB)
## TryHackMe Link (Task 12)
https://tryhackme.com/room/learncyberin25days
### YouTube Walkthrough Link
https://youtu.be/9T8DC95PoxM?t=2042
### Method of Solve
* Step 1: click on the Task 12 header
* Step 2: click on the green `Start Machine` button
* Step 3: at the top of the webpage, copy the IP address under the `Target IP Address`. You can click on the icon to the right of the IP address to copy it to your clipboard
* Step 4: click on the control bar located in the middle of the screen, then click on the clipboard button
* Step 5: in the AttackBox desktop, click on the terminal shortcut button to open a terminal
* Step 6: paste the IP address into the terminal, then use the `enum4linux` command like the following:
```
enum4linux -S <ip_address>
```
This command gives us a list of fileshares that we can access. There's only one available: `/tbfc-santa`
* Step 7: Use the following FTP command to see the contents of the directory
```
ls
```
We see a few different directories, but there seems to only be one directory with content, the `public` directory
* Step 8: Use the following smbclient command to connect to the fileshare
```
smbclient //<IP_address>/tbfc-santa -N
```
Make sure you replace <IP_address> with your own IP address for the target machine. We are now connected anonymously to the SMB fileshare
* Step 9: Use the following command to see the fileshare contents
```
dir
```
There is one file and one directory in the fileshare, but it looks like the directory is empty
* Step 10: Download the file with the following command:
```
get note_from_mcskidy.txt
```
Now that we've downloaded the files, we can exit the server and look at the file contents
* Step 11: Use the following command to exit the SMB server
```
exit
```
* Step 12: Read the `note_from_mcskidy.txt` file with the following command
```
cat note_from_mcskidy.txt
```
* Step 13: Go to the TryHackMe webpage, and navigate to the top of the webpage, and under the red Target Machine Information header, click on the red `Terminate` button
# Challenge 2: TryHackMe 25 Days of Cyber Security - Task 15 (Telnet)
## TryHackMe Link (Task 15)
https://tryhackme.com/room/learncyberin25days
### YouTube Walkthrough Link
https://youtu.be/9T8DC95PoxM?t=2042
### Method of Solve
* Step 1: click on the Task 15 header
* Step 2: click on the green `Start Machine` button
* Step 3: at the top of the webpage, copy the IP address under the `Target IP Address`. You can click on the icon to the right of the IP address to copy it to your clipboard
* Step 4: click on the control bar located in the middle of the screen, then click on the clipboard button
* Step 5: in the AttackBox desktop, click on the terminal shortcut button to open a terminal
* Step 6: paste the IP address into the terminal, then use the `telnet` command like the following:
```
telnet <ip_address>
```
There's a set of credentials in the Telnet banner message, so login with the username `santa` and password `clauschristmas`. You will not see any output while you're typing in the password. This is normal.
* Step 7: Use the following command to see the contents of the directory
```
ls
```
There are two files in this directory. Let's read them
* Step 8: Use the following commands to read the files
```
cat christmas.sh
cat cookies_and_milk.txt
```
It looks like the `christmas.sh` file creates a Christmas tree graphic in the terminal
* Step 9: Use the following command to run the `christmas.sh` script
```
./christmas.sh
```
It's a pretty tree! We can use the `ctrl+x` keyboard shortcut to quit out of the script when we're ready
* Step 10: Exit the server with the following command:
```
exit
```
