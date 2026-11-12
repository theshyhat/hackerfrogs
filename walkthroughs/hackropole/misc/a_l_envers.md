# URL
https://hackropole.fr/en/challenges/misc/fcsc2022-misc-a-l-envers/
# Concept
* receiving and sending data to an arbitrary port on a remote server
# Method of solve
* the challenge wants us to receive a string from the server and send that string back in reverse
* this Python script using Pwntools will get the job done:
```Python
#!/usr/bin/env python3
from pwn import *

p = remote("localhost", 4000)

def get_string(target_line):
    print(f"Received line: {target_line}")
    target_string = target_line.split()[1]
    return target_string

def rev_string(target_string):
    return target_string[::-1]

while True:
    the_string = p.recvline()
    print(f"Received line: {the_string}")
    if b">>>" in the_string:
        print("Found the pattern")
        target_string = get_string(the_string) 
    else:
        continue
    reverse = rev_string(target_string)
    if reverse:
        p.sendline(reverse)
    reverse = ""
```


