# HackerFrogs AfterSchool Forensics Session 6
## Session Topic: Disk Image File Forensics - Part 2
# Challenge 1: TryHackMe Advent of Cyber 2023 - Task 30
## TryHackMe Link
https://tryhackme.com/room/adventofcyber2023
### YouTube Walkthrough Link
https://youtu.be/PcaYV96pdRY?t=749
### Method of Solve
* Step 1: Create a directory to work inside of
```
mkdir /tmp/your_name_sk_intro
cd /tmp/your_name_sk_intro
```
* Step 2: Download the challenge file
```
wget https://artifacts.picoctf.net/c/164/disk.img.gz
```
* Step 3: Unzip the file
```
gunzip disk.img.gz
```
* Step 4: Use the mmls command to find the size of the Linux partition
```
mmls disk.img
```
The length of the Linux partition is the answer we want: `202752`
* Step 5: Go back to the PicoCTF challenge page and click on the `Launch Instance` button, then copy the command after the `Access checker program:` text
* Step 6: Run that command in the webshell and submit `202752` as the answer
* Step 7: Copy the flag value then submit it to the challenge webpage to complete the exercise.
# Challenge 2: Pico SleuthKit Apprentice
## PicoCTF Link
https://play.picoctf.org/practice/challenge/300
## YouTube Walkthrough Link
https://www.youtube.com/watch?v=1sFEUl8UpM0&t=234s
### Method of solve
* Step 1: Create a directory to work inside of
```
mkdir /tmp/your_name_sk_apprentice
cd /tmp/your_name_sk_apprentice
```
* Step 2: Download the challenge file
```
wget https://artifacts.picoctf.net/c/137/disk.flag.img.gz
```
* Step 3: Unzip the file
```
gunzip disk.flag.img.gz
```
* Step 4: Use the `mmls` command to get the offsets for the disk partitions in the image
```
mmls disk.flag.img
```
The partition we want to look at is at offset `360448`
* Step 5: Use the `fsstat` command to get detailed information about the disk partition
```
fsstat -o 360448 disk.flag.img
```
Observe that the file system type is `ext4`. We will need this information for the next step
* Step 6: Use the `fls` command to get the file contents of the disk partition
```
fls -f ext4 -o 360448 -r disk.flag.img
```
In the output, we see that there is a flag.txt file, and its node number `2082`
* Step 7: Read the flag.txt file with the `icat` command
```
icat -f ext4 -o 360448 disk.flag.img 2082
```
There's nothing in the file, because its been deleted.
* Step 8: Read the other flag file in the `root` directory
```
icat -f ext4 -o 360448 disk.flag.img 2371
```
* Step 9: Copy the flag value then submit it to the challenge webpage to complete the exercise.
# Challenge 3: Pico Operation Orchid
## PicoCTF Link
https://play.picoctf.org/practice/challenge/285
## YouTube Walkthrough Link
https://www.youtube.com/watch?v=rXY4BCtonJs&t=2s
### Method of solve
* Step 1: Create a directory to work inside of
```
mkdir /tmp/your_name_op_orchid
cd /tmp/your_name_op_orchid
```
* Step 2: Download the challenge file
```
wget https://artifacts.picoctf.net/c/212/disk.flag.img.gz
```
* Step 3: Unzip the file
```
gunzip disk.flag.img.gz
```
* Step 4: Confirm the file contents
```
file disk.flag.img
```
* Step 5: Get the locations of the filesystems in the image using the `mmls` command
```
mmls disk.flag.img
```
The disk partition we want to look at is in at the `411648` offset
* Step 6: Get the contents of the partition with the `fls` command
```
fls disk.flag.img -o 411648
```
We want to look at the root directory, and we note its node number, which is `472`
* Step 7: Look at the contents of the `root` directory using `fls`
```
fls disk.flag.img 472 -o 411648
```
* Step 8: Read the flag.txt file using the `icat` command
```
icat -o 411648 disk.flag.img 1876
```
Note that there's nothing here, since the file was deleted
* Step 9: Look at the `.ash_history` file to find out what happened to the `flag.txt` file
```
icat -o 411648 disk.flag.img 1875
```
We note here that the `openssl` program was used to encrypt the flag and turn it into a file called `flag.txt.nc`
* Step 10: Read the flag.txt.enc file and write it to our directory using the `icat` command
```
icat -o 411648 disk.flag.img 1782 > flag.txt.enc
```
* Step 11: Use `openssl` to decrypt the flag
```
openssl aes256 -d -salt -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567
```
* Step 12: Read the `flag.txt` file
```
cat flag.txt
```
* Step 13: Copy the flag value then submit it to the challenge webpage to complete the exercise.
