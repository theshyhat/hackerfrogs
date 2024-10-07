# HackerFrogs AfterSchool Linux OS Ops Session 5 Notes
## PicoCTF Challenges
### Big Zip
https://play.picoctf.org/practice/challenge/322?category=5&page=1&search=
#### YouTube Walkthrough
https://www.youtube.com/watch?v=DY0p5_Kk0Rw
#### Bash Script
```
#!/bin/bash
mkdir bigzip
cd bigzip
wget https://artifacts.picoctf.net/c/504/big-zip-files.zip
unzip big-zip-files.zip
grep -r pico .
cd ..
rm -r bigzip
```
### 

