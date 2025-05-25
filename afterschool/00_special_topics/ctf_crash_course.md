# BSides Vancouver 2025 Workshop
## Title: CTF Crash Course with PicoCTF
#### PicoCTF Registration Link
`https://play.picoctf.org/register`
### Part 1: Navigating the Linux Terminal
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
### Part 2: Python Programming for Beginners
#### Website for testing out Python code
`https://www.online-python.com/`
* running Python scripts
  * Pico - Runme.py https://play.picoctf.org/practice/challenge/250
    * key commands `wget` `python`
```
wget https://artifacts.picoctf.net/c/34/runme.py
ls
python runme.py
```
  * Pico - PW Crack 1 https://play.picoctf.org/practice/challenge/245
    * key commands `wget` `python` `cat`
```
wget https://artifacts.picoctf.net/c/10/level1.py
wget https://artifacts.picoctf.net/c/10/level1.flag.txt.enc
python level1.py
cat level1.py
python level1.py
```
The password is `691d`
  * Pico - Serpentine https://play.picoctf.org/practice/challenge/251
    * key commands `wget` `python` `nano`
```
wget https://artifacts.picoctf.net/c/35/serpentine.py
ls
python serpentine.py
nano serpentine.py
```
### Part 3: Intro to Cryptography
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
### Part 4: Beginner's Web App Security
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
  * Pico - Cookie Monster Secret Recipe https://play.picoctf.org/practice/challenge/469
### Part 5: Intro to Digital Forensics
* Picture File Forensics
  * Pico - Information https://play.picoctf.org/practice/challenge/186
  * Pico - Glory of the Garden https://play.picoctf.org/practice/challenge/44
* Disk Image Forensics
  * Pico - SleuthKit Apprentice https://play.picoctf.org/practice/challenge/300
### Part 6: Intro to Binary Hacking
* Program Logic Flaws
  * Pico RPS https://play.picoctf.org/practice/challenge/293
* Buffer Overflow Vulnerabilities
  * Pico Clutter Overflow https://play.picoctf.org/practice/challenge/216
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
