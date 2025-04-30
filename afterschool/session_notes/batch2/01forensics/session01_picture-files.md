# HackerFrogs AfterSchool Forensics Session 1
## Session Topic Picture File Forensics
# Challenge 1: Pico Information
## Pico Link
https://play.picoctf.org/practice/challenge/186
### YouTube Walkthrough Link
https://youtu.be/Wqtn8iJj3qE?t=740
### Method of Solve
> Step 1: Create a directory to work inside of
```
mkdir information
cd information
```
> Step 2: Download the challenge file
```
wget https://mercury.picoctf.net/static/b4d62f6e431dc8e563309ea8c33a06b3/cat.jpg
```
> Step 3: Examine the file with the `exiftool` command
```
exiftool cat.jpg
```
Notice that the `License` value looks like a base64 encoded string
> Step 4: Decode the `License` value from the `exiftool` output
```
echo 'cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9' | base64 -d
```
> Step 5: Copy the flag value then submit it to the challenge webpage to complete the exercise.
# Challenge 2: Glory of the Garden
## PicoCTF Link
https://play.picoctf.org/practice/challenge/44
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
