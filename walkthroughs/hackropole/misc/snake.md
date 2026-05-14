# URL
https://hackropole.fr/en/challenges/misc/fcsc2021-misc-snake/
# Concept
* running OS commands in a Python shell
# Method of solve
* when we connect the challenge, we see that we are within a interactive Python terminal
* so we can use a classic `netcat` shell upgrade technique to get an interactive OS terminal
```
import pty
pty.spawn("/bin/sh")
```
* the `flag.txt` file we need to read is in our current directory
* Finis






