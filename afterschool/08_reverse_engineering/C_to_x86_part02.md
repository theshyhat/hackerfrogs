# C to x86 Assembly Observations
# Part 2: Variable Initialization and If Conditionals
If we create a program with C, then examine it in a debugger, we'll see some common patterns in the x86 assembly instructions

This is the code for the "if_1337" C program, which we save as `if_1337.c`
```
#include <stdio.h>

int main() {
    int x = 1337; // Set x to 1337

    if (x == 1337) {
        printf("The x variable is 1337\n");
    } else {
        printf("The x variable is not 1337\n");
    }

    return 0;
}
```
We can use these commands in Linux to compile the program and run Radare2 to examine the program in the disassembler
```
gcc -o if_1337 if_1337.c
r2 -d if_1337
```
After compiling and running it through the debugger, we see these are the instructions in the main function
```
│           ; var int64_t var_4h @ rbp-0x4
│           0x55b470ed8139      55             push rbp
│           0x55b470ed813a      4889e5         mov rbp, rsp
│           0x55b470ed813d      4883ec10       sub rsp, 0x10
│           0x55b470ed8141      c745fc3905..   mov dword [var_4h], 0x539 ; 1337
│           0x55b470ed8148      817dfc3905..   cmp dword [var_4h], 0x539
│       ┌─< 0x55b470ed814f      7511           jne 0x55b470ed8162
│       │   0x55b470ed8151      488d05ac0e..   lea rax, str.The_x_variable_is_1337 ; 0x55b470ed9004 ; "The x variable is 1337"                                                                                                
│       │   0x55b470ed8158      4889c7         mov rdi, rax
│       │   0x55b470ed815b      e8d0feffff     call sym.imp.puts       ; int puts(const char *s)
│      ┌──< 0x55b470ed8160      eb0f           jmp 0x55b470ed8171
│      │└─> 0x55b470ed8162      488d05b20e..   lea rax, str.The_x_variable_is_not_1337 ; 0x55b470ed901b ; "The x variable is not 1337"                                                                                        
│      │    0x55b470ed8169      4889c7         mov rdi, rax
│      │    0x55b470ed816c      e8bffeffff     call sym.imp.puts       ; int puts(const char *s)
│      │    ; CODE XREF from main @ 0x55b470ed8160(x)
│      └──> 0x55b470ed8171      b800000000     mov eax, 0
│           0x55b470ed8176      c9             leave
└           0x55b470ed8177      c3             ret
```
## Recognizing Variable Initialization
The following code sets a local variable:
```
sub rsp, 0x10
mov dword [var_4h], 0x539 ; 1337
```
The first instruction, `sub rsp, 0x10`, sets aside space for local variables on the stack. In this case, `0x10` (16) bytes.

The second instruction, `mov dword [var_4h], 0x539`, creates a local variable dword (2 bytes) with a value of `0x539` (1337 in decimal) to the `var_4h` variable.
## Recognizing If Conditionals
The following code will run one set of instructions or another, depending on the result of the `cmp` instruction:
```
│           0x55b470ed8148      817dfc3905..   cmp dword [var_4h], 0x539
│       ┌─< 0x55b470ed814f      7511           jne 0x55b470ed8162
│       │   0x55b470ed8151      488d05ac0e..   lea rax, str.The_x_variable_is_1337 ; 0x55b470ed9004 ; "The x variable is 1337"                                                                                                
│       │   0x55b470ed8158      4889c7         mov rdi, rax
│       │   0x55b470ed815b      e8d0feffff     call sym.imp.puts       ; int puts(const char *s)
│      ┌──< 0x55b470ed8160      eb0f           jmp 0x55b470ed8171
│      │└─> 0x55b470ed8162      488d05b20e..   lea rax, str.The_x_variable_is_not_1337 ; 0x55b470ed901b ; "The x variable is not 1337"                                                                                        
│      │    0x55b470ed8169      4889c7         mov rdi, rax
│      │    0x55b470ed816c      e8bffeffff     call sym.imp.puts       ; int puts(const char *s)
│      │    ; CODE XREF from main @ 0x55b470ed8160(x)
│      └──> 0x55b470ed8171      b800000000     mov eax, 0
```
The `cmp` instruction compares the contents of the `var_4h` variable with the value `0x539` (1337). If the comparison returns true, the `ZF` (zero flag) will be set to `1` (True), otherwirse it will be set to `0` (False).

The `jne` instruction will execute if the comparison is not the same.


