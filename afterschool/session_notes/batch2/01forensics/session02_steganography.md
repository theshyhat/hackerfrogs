# HackerFrogs AfterSchool - Forensics
# Session Topic: Steganography
# Challenge 1: TryHackMe - Mom, are we going to be okay?
## TryHackMe Link (Task 4)
https://tryhackme.com/r/room/ctfcollectionvol1
### YouTube Walkthrough Link
https://youtu.be/Wqtn8iJj3qE?t=740
### Method of Solve
* Step 1: Click on the green `Join Room` button to get access to the materials in the room
* Step 2: At the top of the webpage, click on the `Start AttackBox` button. It should take about 2 minutes for the AttackBox to finish initializing
* Step 3: Under the `Task 4` header, click on the `Download Task Files` button
* Step 4: In the resulting picture file, copy the full address, then click on the back button in your web browser
* Step 5: Click open the `Hide/Show the control bar` located at the at the center of the web page (between the Tryhackme page and the AttackBox desktop), then click on the `Clipboard` button
* Step 6: Click into the clipboard and paste in the address of the picture file, then click on the `Hide/Show the control bar`
* Step 7: Start the AttackBox's Firefox web browser by clicking on the orange shortcut icon at the top of the AttackBox desktop interface
* Step 8: Paste in the address of the picture file in the web browser to access it in the browser
* Step 9: Right-click on the image, and select `Save image as` to save it to the downloads folder
* Step 10: In the AttackBox, open a terminal window by clicking on the shortcut icon at the top of the desktop
* Step 11: Enter the Downloads directory, then
```
cd Downloads
steghide info -sf Extinction_1577976250757.jpg
steghide extract -sf Extinction_1577976250757.jpg
```
# Challenge 2: Steghide Embedding Tutorial
## TryHackMe Link
https://tryhackme.com/r/room/ctfcollectionvol1
### Method of solve
> This tutorial assumes that we still have access to the TryHackMe Attack Box system
* Step 1: Navigate to this page
```
https://github.com/theshyhat/hackerfrogs/blob/main/afterschool/04_digital_forensics/steganography.sh
```
* Step 2: Click on the `Copy raw file` button (beside the `Raw` button)
* Step 3: Back in the Attack Box, click into the Clipboard and paste in the contents of the steganography.sh file, then close the Clipboard
* Step 4: In an Attack Box terminal, edit a file using `nano` named `steganography.sh`
```
nano steganography.sh
```
* Step 5: Paste in the contents of the clipboard in the Nano text editor
`ctrl+shift+v`
* Step 6: Save the file
`ctrl+x` `y` `enter`
* Step 7: Create a secret message text file to embed into a Jpg file
```
echo "The secret message is HackerFrogs Rule!" > secret.txt
```
* Step 8: Use `steghide` to embed the `secret.txt` into `hackerfrog.jpg` file with 
```
steghide embed -cf hackerfrog.jpg -p password123 -ef secret.txt
```
* Step 9: Delete the `secret.txt` file
```
rm secret.txt
```
* Step 10: Extract the `secret.txt` file from the `hackerfrog.jpg` file
```
steghide extract -sf hackerfrog.jpg
```
* Step 11: Read the `secret.txt` file
```
cat secret.txt
```
