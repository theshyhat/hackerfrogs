# URL
https://play.picoctf.org/practice/challenge/505
# Concept
* disk image forensics
# Method of solve
* all we need to do is runs on the disk image and look for the flag pattern
```
strings disko-1.dd | grep picoCTF
```
