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
## YouTube Walkthrough Link
https://youtu.be/rloRz-PLiDk
### Method of solve
> Step 1: Create a directory to work inside of
```
mkdir garden
cd garden
```
> Step 2: Download the challenge file
```
wget https://jupiter.challenges.picoctf.org/static/d0e1ffb10fc0017c6a82c57900f3ffe3/garden.jpg
```
> Step 3: Search for text strings with the `strings` command
```
strings garden.jpg
```
> Step 4: Copy the flag value then submit it to the challenge webpage to complete the exercise.
# Challenge 3: Matroyshka Doll
## PicoCTF Link
https://play.picoctf.org/practice/challenge/129
## YouTube Walkthrough Link
https://youtu.be/dArlzDgjH-Y
### Method of solve
> Step 1: Create a directory to work inside of
```
mkdir m_doll
cd m_doll
```
> Step 2: Download the challenge file
```
wget https://mercury.picoctf.net/static/f6cc2560a70b1ea811c151accba5390f/dolls.jpg
```
> Step 3: Inspect the file with the `binwalk` command
```
binwalk dolls.jpg
```
Notice that there is an embedded file named `2_c.jpg`
> Step 4: Extract the file using `binwalk`
```
binwalk -e dolls.jpg
```
After the operation, there is a new directory created: `_dolls.jpg.extracted`
> Step 5: Enter the new directory and inspect the new file using `binwalk`
```
cd _dolls.jpg.extracted
ls
cd base_images
binwalk 2_c.jpg
```
There's another embedded file in here: `3_c.jpg`. If there are more embedded images inside that one, we can recursively extract them (extract them all at once) with `binwalk`.
> Step 6: Recursively extract any other images with `binwalk`
```
binwalk -e -M 2_c.jpg
```
> Step 7: Move through the directories created until we find the challenge flag
```
cd _2_c.jpg.extracted/
ls
cd base_images
ls
cd _3_c.jpg.extracted/
ls
cd base_images
ls
cd _4_c.jpg.extracted/
ls
```
> Step 8: Read the challenge flag
```
cat flag.txt
```
> Step 9: Copy the flag value then submit it to the challenge webpage to complete the exercise.
