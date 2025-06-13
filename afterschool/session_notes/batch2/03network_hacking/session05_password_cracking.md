# HackerFrogs AfterSchool Network Hacking Session 5
## Session Topic: Password Cracking /w TryHackMe
# Challenge 1: TryHackMe Crack the Hash Room
## TryHackMe Link
https://tryhackme.com/room/crackthehash
### YouTube Walkthrough Link
https://youtu.be/Xn673x-FkF8?t=1004
### Method of Solve
* Step 1: go to the top of the webpage, and click on the "Start AttackBox" button located underneath the cloud icon with the santa hat on it
* Step 2: wait 2 minutes for the AttackBox to finish loading
* Step 3: after the AttackBox finishes loading, at the bottom-middle of the TryHackMe webpage click on the "View in full screen" button, which looks like two arrows pointing away from each other
* Step 4: in the AttackBox desktop, click on the terminal shortcut button to open a terminal
## Part 1: Setting Up the Hash Cracking Files
* Step 1: Copy the code below
```
#!/bin/bash
: '
This script is used with the HackerFrogs AfterSchool Network hacking course,
and is meant to help teach hash cracking with the John the Ripper program.
Here are instructions on how to complete the exercise:

Step 1: Run the script
cd /tmp
wget https://github.com/theshyhat/hackerfrogs/edit/main/afterschool/06_network_hacking/cracking_practice.sh
chmod +x cracking_practice.sh
./cracking_practice.sh

Step 2: Crack the zip file hash
zip2john zip_crack.zip > zip.hash
john --wordlist=/usr/share/wordlists/rockyou.txt zip.hash

Step 3: Crack the Linux password hash
unshadow hackerfrog.passwd hackerfrog.shadow > hackerfrog.hash
john --wordlist=/usr/share/wordlists/rockyou.txt hackerfrog.hash

Step 4: Crack the SSH key hash
ssh2john id_rsa > id_rsa.hash
john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.hash

'
useradd -m -s /bin/bash hackerfrog && echo "hackerfrog:hollywood" | chpasswd
echo 'frog{z1p_h@sh_cr4cked}' > zip_flag.txt
zip -P starwars zip_crack.zip zip_flag.txt
echo 'hackerfrog:x:1000:1000::/home/hackerfrog:/bin/bash' > hackerfrog.passwd
echo 'hackerfrog:$6$7M7YK/Hz6$JLORDQ8BtYLElqX5DEuVP6mSK7clZlOAD/t4MH4FwoQBkwsk41huec74BYmE5XzULrOmhw72ywQ1lhjafCt.q0:20105:0:99999:7:::' > hackerfrog.shadow
echo '-----BEGIN OPENSSH PRIVATE KEY-----                   
b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jdHIAAAAGYmNyeXB0AAAAGAAAABDWcnhzmm
R/3d0KNBMoYrcfAAAAEAAAAAEAAAEXAAAAB3NzaC1yc2EAAAADAQABAAABAQDYIe8H6sCq
/oDep7wmVjIILRA46qWK2DRk7PIy6fBr8qQaAnHsXYzHudCC+FzZ90hbd/w7G6bqcfwPbB
QjdA+4D06qxRGUyL5SZRnt+qeGN5z1dgBF69Gd1UjGIJ8AJBrKGOuMTbfeGhXaZN4V/7mb
epDVcNYruzb4QIKuS6NoVQX1DvAiDQNsMwoflmAUm5favqr6GNbBxHikWc/YbLLCLhtofI
nNZScbzSzYWsTpIWXjYUwissWjDbM/vTEEYc8LovrbFlS/eeLbI7XaF5XxLHJBoRT7fvLr
1m+qMPV62fJzuB9gBIrEqgBwtudibWGvCaVxF+Lfmh91wkqfcdxzAAAD0H+IE8hKyf+/lZ
l4vf3w1UQFHxT+VMGAYGTabhq1IMrmyxeCzA8zmhB0lok8UKr9aiTSOHNRXdJIm/uxPwSk
p9p9jHOn5Fu2ts1kn0ruPZV2QczVEpOMdbiGyueKNFDuSPrevin0dSe3FvzkhORx6KXeFf
EYA5dS+08vIjSKwjcja325y1+XXcKaQRAB1GdibKFw/HgbIvCtTjWOCYaNCnlqKYBpY2J0
FsG5JQ55K+K5DC7vSUMhobdOJ3tYosHK4NzhYcNvxMsKgCE3hvxClgsGMZHSL/qNTyF2nw
7YoU7Za6/42imGjR70I37FwmYhvkGWp7h6lzrgywXoEgrlu75GdunETu2DiJk2Oi5sXAa1
qGBJNWB620CKaUofSZQn3ZylkMuT3hTMa0I1qrVm3+Jg4T4EelyunkZM5DpMGnQBDFSiv5
4gBfhhdoZn3Fu69BGsTfo8r63Xwc9B+taUWBAGyA9aEOIZKFngnH+IPsmLfFGjiQXLMoTV
cKOHzvISHDiZr3NGHlQoT2RiZtFPevVdl+Qanb5JNw7Wgy3trdRah/diH7NNlT85waEntt
fHCkw7Aq0JfmN6CmTmpddKyWRxAKVOxGdTftgvWidVsuehxTr+6F2pLEc2X+8HxaZvFO1O
jQ56xQW4HHtbvKpVh9j9rh5Z9LzfrZQfQBrENMn8TvVVW8XbozUBAMRqvSu8aIkR6vZaXn
kRnqzve5hcLQfZeYdkcrEvTeA7V2AguLnhTQ3CXyHPdcfkPtFX2zbS+1/uWFhXzrIhaoEd
MPX/WRtwdRbAwVFuyFm/LqJViRVgsn/MyMi2t3dn2uvs+inoP4Cs0/8ld7MO+aTVKyiNkH
tmtTKAPOfpJxRDuPnhtLJVkrAUndMl/64FWeCG7p84nSqRf6NCfh6cVJHA74brcfGrTotL
fdBMEWi1NJiW+eOLVEUZi8bKj7LL/gONQYlFa5IYB3l5SZ7y9ssRILnzIRbaaEYtD9vtqX
qKtLvNUL6PWst8iJK4NPLZ0B2Qm58YpPepMzCDnzMwNLYBdRNaXeyhhhFtOxgJ1bOLn2hM
cPB/7ZRBGDKTBIZuZaAmRur9h9pLESxUUSFBpCOnmdQw6Uj5F/WvMOfMIEQLAwNQkp2/jC
e4u9JlbJGQ01QGqsvzBPaTAoeisAhweX938yKJHW/XTJI6YQjc6tKXjkbkVgMnjgoB47C+
jUgSoQ6SVzofG2riX2VV+/0hzlaa+An7Y9qg/P8fVSyXuQ+tggzb6shUehCrhTW4m9tux9
rtefYsdrBabWSoMj/UDVWNOyrXqR4=
-----END OPENSSH PRIVATE KEY-----' > id_rsa
rm zip_flag.txt
```
* Step 2: Go to your AttackBox desktop and click on the `control panel` button located at the middle-left-hand side of the screen, then click on the `clipboard` button, then paste in the code, then close 
* Step 3: In the AttackBox terminal, use the following command to start a Nano text editor
```
nano crack_practice.sh
```
* Step 4: In the text editor, paste in the code, then save the file by using the `ctrl+x` keyboard shortcut, then the `y` key, then the `enter` key
* Step 5: Make the crack_practice.sh file executable with the following command:
```
chmod +x crack_practice.sh
```
* Step 6: Run the crack_practice.sh script with the following command
```
./crack_practice.sh
```
There are should be a bunch of new files in the directory, including `hackerfrog.passwd`, and `zip_crack.zip`.
## Part 2: Cracking a Zip File Password
* Step 1: Use the following command to extract the hash from the zip file
```
zip2john zip_crack.zip > zip.hash
```
We now have a hash that can be cracked by the John the Ripper program.
* Step 2: Use the following command to crack the hash with John the Ripper
```
john --wordlist=/usr/share/wordlists/rockyou.txt zip.hash
```
Awesome! We found out the zip file password is `starwars`
* Step 3: Unzip the zip file with the following command, and use the `starwars` password when prompted
```
unzip zip_crack.zip
```
Let's read the HackerFrog flag file that we unzipped
* Step 4: Read the flag:
```
cat zip_flag.txt
```
## Part 3: Cracking Linux Password Hashes
* Step 1: Use the unshadow command to create a file that John the Ripper can use to crack the Linux user passwords
```
unshadow hackerfrog.passwd hackerfrog.shadow > hackerfrog.hash
```
* Step 2: Use John the Ripper to Crack the Hash
```
john hackerfrog.hash --wordlist=/usr/share/wordlists/rockyou.txt
```
This reveals the password for the hackerfrog user: `hollywood`
* Step 3: Use the following command to switch user accounts to the hackerfrog account, and provide the `hollywood` password when prompted
```
su hackerfrog
```
* Step 4: Confirm that we're now logged in as the hackerfrog account with this command
```
whoami
```
Awesome! We cracked the hackerfrog account and logged in as that account
* Step 5: Close the terminal window and open a new one to get root user access back
## Part 4: Cracking SSH Private Key Hashes
* Step 1: Use the following command to extract the SSH private key hash
```
python3 /opt/john/ssh2john.py id_rsa > key.hash
```
* Step 2: Crack the hash with John the Ripper
```
john key.hash --wordlist=/usr/share/wordlists/rockyou.txt
```
Awesome! We cracked the SSH private key hash and got the password, `tweetybird`
