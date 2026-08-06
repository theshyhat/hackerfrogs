# URL
https://hackropole.fr/en/challenges/pwn/fcsc2020-pwn-poney/
# Concept
* buffer overflow
* ret2win
* payload does not appear in IP during crash
# Method of solve
* when we examine the binary in Radare2, we see that there is function called `sym.win`
* but this function is not referenced in the `main` function
* this makes think that this is a ret2win challenge
  * this means we need to buffer overflow the program and insert the memory address of the `sym.win` function into the IP register (RIP)
* the first thing we need to do is figure out the correct offset of bytes to send to the program to enter the RIP register
* this assembly codes gives us a clue:
```asm
0x0040068d      4883ec20       sub rsp, 0x20
```
* this is setting aside some memory (0x20 bytes, or 32) for the user input
* this means the offset will be greater than 32 bytes
* if we send more than 40 bytes then the excess will appear in the `RSP` register before the main function ends
* set a breakpoint for the `ret` instruction at the end of the `main` function
* you will see that the `RSP` register will have our payload
* when the `ret` instruction runs, the contents of the `RSP` register will be popped into the `RIP` register
* the reason why we're paying attention to the `RSP` register instead of the `RIP` register is because in this program, for some reason, the `RIP` register shows different values at the time of program crash
* we need to send an offset of 40 bytes, then the address of the `sym.win` function
* this Python script will do the job:
```Python
from pwn import *
import sys
# io = process('./poney')
io = remote('localhost', 4000)
payload = b"C"*40 + p64(0x400676)
io.send(payload)
io.interactive()
```




