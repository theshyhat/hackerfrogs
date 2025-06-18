# HackerFrogs AfterSchool Network Hacking Session 7
## Session Topic: File Transfers /w TryHackMe
# Challenge 1: TryHackMe Crack the Hash Room
## TryHackMe Link
https://tryhackme.com/room/c2carnage
### YouTube Walkthrough Link
https://youtu.be/Efr6szwDcvs?t=962
### Method of Solve
* Step 1: Click on the Task 1 header in the TryHackMe page, then click on the green "Start Machine" button
* Step 2: go to the top of the webpage, and click on the "Start AttackBox" button
* Step 3: wait 2 minutes for the AttackBox to finish loading
* Step 4: after the AttackBox finishes loading, at the bottom-middle of the TryHackMe webpage click on the "View in full screen" button, which looks like two arrows pointing away from each other
* Step 5: in the AttackBox desktop, click on the terminal shortcut button to open a terminal
* Step 6: in the Carnage desktop, click on the terminal shortcut button to open a terminal
## Part 1: Clipboard and Base64 File Transfer
We will move a picture file from the Carnage machine to the AttackBox machine.
* Step 1: In the Carnage terminal, use the following command to enter the Pictures directory:
```
cd Pictures
```
* Step 2: Use the following command to get the file contents of the `THM-Menu-Logo-2.png` picture file in Base64 encoding:
```
cat THM-Menu-Logo-2.png | base64
```
* Step 3: Highlight all of the output from the previous command, (be careful to not highlight any other data) then copy the data to your clipboard with either the `ctrl+shift+c` keyboard shortcut, or right-clicking, and selecting `copy`
* Step 4: In the AttackBox terminal, use the following command to create a file named `picture.b64` in the nano text editor
```
nano picture.b64
```
* Step 5: In the AttackBox desktop, click on the control bar button located on the left-middle edge of the window, then click on the `Clipboard` button, then paste the base64 data into the clipboard, then close the clipboard and the control bar
* Step 6: in the AttackBox terminal, paste in the base64 data, then save the file by using the `ctrl+x` keyboard shortcut, then `y`, then the `enter` key
* Step 7: Restore the picture file to its original form with the following command
```
base64 -d picture.b64 > picture.png
```
* Step 8: Use the following command open the `picture.png` file and confirm that the file copied correctly
```
xdg-open picture.png
```
## Part 2: Python HTTP Server and Wget File Transfer
In this transfer method, we'll be hosting files via the Python HTTP server and downloading the files using Wget
* Step 1: In the Carnage terminal, use the following Python command to start the HTTP server
```
python3 -m http.server 8888
```
* Step 2: In the AttackBox terminal, use the following wget command to download the picture file from the Carnage machine:
```
wget http://<IP_address>:8888/THM-Menu-Logo-2.png
```
Make sure to replace <IP_address> with the IP address of the Carnage machine (it can be located on the terminal in the following format `ubuntu@<IP_address>`)
* Step 3: Confirm that the file transferred successfully by using the following command
```
xdg-open THM-Menu-Logo-2.png
```
* Step 4: Delete the picture file in preparation for the next file transfer method
```
rm THM-Menu-Logo-2.png
```
## Part 3: Scp (SSH) File Transfer
* Step 1: In the Carnage machine terminal, use the following command to transfer the picture file 
```
scp root@<AttackBox_IP>:/root/picture.png .
```
When prompted for the password, look at the AttackBox's URL address bar, and look for the value of `password=SOMETHING&`. The password is the value between the `=` sign and the `&` sign. Paste that into the Carnage machine clipboard from the control bar, then paste it into the terminal to submit the password
* Step 2: Confirm the file transferred correctly by using the following command
```
xdg-open picture.png
```
