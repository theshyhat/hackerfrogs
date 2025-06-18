# HackerFrogs AfterSchool Network Hacking Session 6
## Session Topic: Brute Force Attacks /w TryHackMe
# Challenge 1: TryHackMe Crack the Hash Room
## TryHackMe Link
https://tryhackme.com/room/hydra
### YouTube Walkthrough Link
https://youtu.be/pA24wtu_vmo?t=1145
### Method of Solve
* Step 1: Click on the Task 3 header in the TryHackMe page, then click on the green "Start Machine" button
* Step 2: go to the top of the webpage, and click on the "Start AttackBox" button located underneath the cloud icon with the santa hat on it
* Step 3: wait 2 minutes for the AttackBox to finish loading
* Step 4: after the AttackBox finishes loading, at the bottom-middle of the TryHackMe webpage click on the "View in full screen" button, which looks like two arrows pointing away from each other
* Step 5: in the AttackBox desktop, click on the terminal shortcut button to open a terminal
## Part 1: Setting Up Burp Suite
* Step 1: On the AttackBox, start Burp Suite by clicking on the blue icon on the right-hand edge of the desktop
* Step 2: Click on the `settings` button located at the upper-right corner of the Burp Suite interface
* Step 3: In the settings menu, type the word `browser` into the search field at the top-left of the Settings window
* Step 4: Underneath the `Browser running` project setting, click on the checkbox labeled `Allow Burp's browser to run without a sandbox`
* Step 5: Close the settings window
* Step 6: In Burp Suite, click on the `Proxy` tab, located in-between the `Target` and `Intruder` tabs 
* Step 7: Click on the blue `Intercept on` button so that button reads `Intercept is off`
* Step 8: Click on the `Open browser` button to start the Burp Suite browser
## Part 2: Brute force attack the login page
* Step 1: Go back to the TryHackMe webpage, and go to the top of the page. Underneath the `Target Machine Information` header, note the IP address
* Step 2: In the AttackBox, use the Burp Suite browser to navigate to the following webpage `http://<IP_address>`
Make sure to replace <IP_address> with the IP address you noted in Step 1 (the Target Machine Information IP)
* Step 3: On the resulting webpage, try logging in with the following username and password: `molly` `test`
* Step 4: Go to Burp Suite and click on the `Proxy` tab, then the `HTTP history` tab
* Step 5: In the resulting list, scroll down to the bottom, and click on the row where the Method column is POST
* Step 6: In the window that appears in the lower-left corner, right-click and select `Copy to file`
* Step 7: Save the file as `request.txt`
* Step 8: In the AttackBox terminal, use the following command to edit the `request.txt` file
```
nano request.txt
```
* Step 9: in the text editor, scroll down to the bottom and replace the word `test` with `FUZZ`
* Step 10: Save the file by using the `ctrl+x` keyboard shortcut, then input `y`, then press the `enter` key
* Step 11: Use the following FFuF command to brute force the login page:
```
ffuf -request request.txt -w /usr/share/wordlists/rockyou.txt -request-proto http
```
Don't wait for the command to finish, and use the `ctrl+c` keyboard to quit out of the command. Note that all of the incorrect logins have `Size: 56`
* Step 12: Use the following FFuF command to filter out all output that returns `Size: 56`, so we only see successful logins
```
ffuf -request request.txt -w /usr/share/wordlists/rockyou.txt -request-proto http -fs 56
```
The correct password comes back very quickly, and it's `sunshine`
* Step 13: Use the username / password `molly` / `sunshine` to login to the webpage
## Part 3: Brute forcing the SSH login
* Step 1: In the AttackBox terminal, use the following command to brute force the SSH login using the Hydra program
```
hydra -l molly -P /usr/share/wordlists/rockyou.txt <IP_address> ssh
```
After a few moments, we should get the password, which is `butterfly`
* Step 2: Login to SSH as molly with the following command
```
ssh molly@<IP_address>
```
When prompted, use the password `butterfly`
