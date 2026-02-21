# URL
https://ctflearn.com/challenge/971
# Concept
* picture file forensics
* hex dump (xxd)
# Method of solve
* download the file
* if you hexdump with `xxd`, you'll notice that the flag is spelled out in the beginning of the file with two unprintable bytes between each letter
```Bash
xxd 971 | head
```
* stream contributer `Snollygoster` provided this fun one-liner that can pull out the flag:
```Bash
strings -n 1 971 | sed '4,26p' -n | tr -d ' \n'
```
