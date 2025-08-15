# C to x86 Assembly Observations
# Part 1: Function Prologue / Epilogue and Printf
If we create a program with C, then examine it in a debugger, we'll see some common patterns in the x86 assembly instructions

This is the code for the "Hello World" C program, which we save as `hello.c`
```
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}

```
We can use these commands in Linux to compile the program and run Radare2 to examine the program in the disassembler
```
gcc -o hello hello.c
r2 -d hello.c
```
After compiling and running it through the debugger, we see these are the instructions in the main function
```
push rbp
mov rbp, rsp
lea rax, str.Hello__World_
mov rdi, rax
call sym.imp.puts
mov eax, 0
pop rbp
ret
```
## Function Prologue and Epilogue
The first two instructions and the last two instructions in any function in x86 assembly are going to save the calling function's frame to the memory stack (`push rbp`), then, then setup a new stack frame in it's place (`mov rbp, rsp`).

The registers involved in this case are the `base pointer` (bp) which points to the 
