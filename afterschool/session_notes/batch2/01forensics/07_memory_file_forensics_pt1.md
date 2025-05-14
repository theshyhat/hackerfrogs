# HackerFrogs AfterSchool Forensics Session 7
## Session Topic: Memory Image File Forensics - Part 1
# Challenge 1: TryHackMe Advent of Cyber 2022 - Task 16
## TryHackMe Link
https://tryhackme.com/room/adventofcyber4
### YouTube Walkthrough Link
https://youtu.be/iopPyFyeq04?t=785
### Method of Solve
#### Part 1: Accessing the TryHackMe Machine and Entering the Volatility Directory
* Step 1: Click on the `Task 16` header on the TryHackme page
* Step 2: Under the `Task 16` header, click on the green `Start Machine` button
* Step 3: In the terminal, use the following command to enter the `volatility` directory
```
cd volatility3
```
#### Part 2: Inspecting the Windows Info to Answer the First Question
* Step 1: In terminal, use the following command to retrieve the info for Windows version of the memory file:
```
python3 vol.py -f workstation.vmem windows.info
```
* Step 2: In the resulting output, note this line:
```
PE MajorOperatingSystemVersion 10
```
The version is 10.
* Step 3: Submit `10` as the answer for the first question
#### Part 3: Look For Running Processes to Answer the Second Question
* Step 1: In the terminal use the following command to output a list of running processes:
```
python3 vol.py -f workstation.vmem windows.pslist
```
This outputs all of the running processes, but it's a bit overwhelming. We should look and see if there's a `gift` process being run.
* Step 2: Use the following command to look for the `gift` text in the running processes:
```
python3 vol.py -f workstation.vmem windows.pslist | grep gift
```
Observe that there's a process called `mysterygift.exe` in the output
* Step 3: Submit `mysterygift.exe` as the answer for the second question
#### Part 4: Note the PID of the MysteryGift File to Answer the Third Question
* Step 1: In the previous output, the first number for the `mysterygift.exe` is the PID, and the second number if the PPID
The PID of the `mysterygift.exe` file is `2040`
* Step 2: Submit `2040` as the answer for the third question
#### Part 5: Dump the MysteryGift Binary to Answer the Fourth Question
* Step 1: Create a directory to dump the files into:
```
mkdir dump
```
* Step 2: In the terminal, use the following command to extract all of the files associated with the MysteryGift binary:
```
python3 vol.py -o dump -f workstation.vmem windows.dumpfiles --pid 2040
```
* Step 3: Enter the `dump` directory and count the number of files
```
cd dump
ls
```
Note that we can count the number of files by piping the output of the `ls` command into the `wc` command
```
ls | wc
```
There are `16` files
* Step 4: Submit `16` as the answer for the fourth question
