# HackerFrogs AfterSchool Forensics Session 8
## Session Topic: Memory Image File Forensics - Part 2
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
python3 vol.py -f workstation.vmem windows.pstree
```
* Step 2: In the resulting output, note this line:
The mysterygift.exe process has a PPID value of 5888, we can look at the PID associated with 5888 and see that the process, and the answer is `cmd.exe`
#### Part 3: Look at the Command History to Answer the Second Question
* Step 1: In the terminal use the following command to output a list of commands run on the terminal:
```
python3 vol.py -f workstation.vmem windows.cmdline
```
This outputs all of the commands run on the terminal. To hone in on the notepad.exe file, we can use the previous command with the grep command:
```
python3 vol.py -f workstation.vmem windows.cmdline | grep notepad
```
We see from the output that the notepad.exe file is running the `secretfile.txt` file, which is the answer.
#### Part 4: Look at Networking Information to Answer the Third Question
* Step 1: Use the following command to retrieve networking information from the memory image:
```
python3 vol.py -f workstation.vmem windows.netscan
```
This gets all of the networking information, but it's a lot. We should isolate port 80 with grep:
```
python3 vol.py -f workstation.vmem windows.netscan | grep 80
```
We see the process running on port 80 is `python.exe`, which is the answer
#### Part 5: Retrieve the Name of the Computer from the Windows Registry to Answer the Fourth Question
* Step 1: Use the following command to retrieve the computer name from the Windows registry
```
python3 vol.py -f workstation.vmem windows.registry.printkey --key "ControlSet001\\control\\ComputerName\\ComputerName"
```
In the output, we see the computer name `DESKTOP-3SD2BNH`, which is the answer
#### Part 6: Dump the MysteryGift Binary to Answer the Remaining Questions
* Step 1: Create a directory to dump the files into:
```
mkdir dump
```
* Step 2: In the terminal, use the following command to extract all of the files associated with the MysteryGift binary:
```
python3 vol.py -o dump -f workstation.vmem windows.dumpfiles --pid 2040
```
* Step 3: Use the md5sum command to get the file hash of the MysteryGift binary
```
md5sum <filename>
```
Note that we can count the number of files by piping the output of the `ls` command into the `wc` command
