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
### System Enumeration Script
```
#!/bin/bash
echo "Your username is `whoami`"
echo "The name of this host is `hostname`"
echo "These are the users on the system with shell login:"
cat /etc/passwd | grep -v nologin
```

