# URL
https://play.picoctf.org/practice/challenge/295
# Concept
* webpage content search
# Method of solve
* we can download the entire website with the `wget` tool
```
wget -mpEk http://saturn.picoctf.net:55514
```
* make sure to replace the port number with the one from your webpage instance
* after the command runs, you'll have a new directory in your current directory. Move into the directory, then use this `grep` command to look for the flag:
```
grep -r . -e "picoCTF{"
```
