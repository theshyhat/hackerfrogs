# URL
https://hackropole.fr/en/challenges/pwn/fcsc2022-pwn-depassement-de-tampon/
# Concept
* buffer overflow
* SP (stack pointer) injection
* ret2win
# Method of solve
* when we look at the binary in the debugger, we see that there is a conspicuous function that isn't referenced in the `main` function called `sym.shell`:
```
r2 -d ./pwn
aaa
afl
pdf @ sym.shell
```
* this function opens up an interactive shell using the `system` call, so it's likely the concept behind this challenge is a `ret2win` condition
  * that is, use a buffer overflow exploit in the program to execute a function not regularly accessible through normal program execution (in this case, `sym.shell`)
* typical buffer overflow challenges have us controlling overflow into the IP register after a certain amount of memory overflow
  * in this case, it's through user input provided by the C `fgets` function
    * `fgets` is supposed to be memory-safe, but can still be vulnerable to buffer overflow if used incorrectly
      * specifically, `fgets` is unsafe if it is (accidentally or deliberately) coded where the maximum number of bytes to write is larger than the buffer it's writing to
* in this challenge, however, no matter how much we overflow the buffer, our data never reaches the `IP` register
* we do see that after 52 bytes, our user input is placed in the `SP` register
* we can exploit the fact that the address in the `SP` register will be jumped to at the end of a function in x86 programs
* * so our payload is essentially:
    * send 52 bytes to reach the offset of the `SP` register, then fill the register with the address of the `sym.shell` function
    * the address of the `sym.shell` function is available through using the `radare2` `afl` command after binary analysis
  * this pwntools script will solve the challenge
```Python
from pwn import *
import sys
# io = process('./pwn')
io = remote('localhost', 4000)
payload = b"C"*56 + p64(0x004011a2)
io.send(payload)
io.interactive()
```
