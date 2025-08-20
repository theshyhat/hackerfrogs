# C to x86 Assembly Observations
# Part 3: Taking User Input and Saving User Input
If we create a program with C, then examine it in a debugger, we'll see some common patterns in the x86 assembly instructions

This is the code for the "user_input" C program, which we save as `user_input.c`
```
#include <stdio.h>

int main() {
    char name[100];
    
    printf("What is your name? ");
    scanf("%99s", name); // Limit input to 99 characters
    
    printf("Hello, %s! Nice to meet you!\n", name);
    
    return 0;
}
```
We can use these commands in Linux to compile the program and run Radare2 to examine the program in the disassembler
```
gcc -o user_input user_input.c
r2 -d user_input
```
After compiling and running it through the debugger, we see these are the instructions in the main function
```
│           ; var int64_t var_70h @ rbp-0x70
│           0x5570acc62149      55             push rbp
│           0x5570acc6214a      4889e5         mov rbp, rsp
│           0x5570acc6214d      4883ec70       sub rsp, 0x70
│           0x5570acc62151      488d05ac0e..   lea rax, str.What_is_your_name_ ; 0x5570acc63004 ; "What is your name? "                                                                                                       
│           0x5570acc62158      4889c7         mov rdi, rax
│           0x5570acc6215b      b800000000     mov eax, 0
│           0x5570acc62160      e8cbfeffff     call sym.imp.printf     ; int printf(const char *format)
│           0x5570acc62165      488d4590       lea rax, [var_70h]
│           0x5570acc62169      4889c6         mov rsi, rax
│           0x5570acc6216c      488d05a50e..   lea rax, str._99s       ; 0x5570acc63018 ; "%99s"
│           0x5570acc62173      4889c7         mov rdi, rax
│           0x5570acc62176      b800000000     mov eax, 0
│           0x5570acc6217b      e8c0feffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
│           0x5570acc62180      488d4590       lea rax, [var_70h]
│           0x5570acc62184      4889c6         mov rsi, rax
│           0x5570acc62187      488d058f0e..   lea rax, str.Hello___s__Nice_to_meet_you__n ; 0x5570acc6301d ; "Hello, %s! Nice to meet you!\n"                                                                                
│           0x5570acc6218e      4889c7         mov rdi, rax
│           0x5570acc62191      b800000000     mov eax, 0
│           0x5570acc62196      e895feffff     call sym.imp.printf     ; int printf(const char *format)
│           0x5570acc6219b      b800000000     mov eax, 0
│           0x5570acc621a0      c9             leave
└           0x5570acc621a1      c3             ret
```
## Recognizing User Input
The following code takes in user input and assigns it to a variable:
```
lea rax, [var_70h]
mov rsi, rax
lea rax, str._99s       ; 0x5570acc63018 ; "%99s"
mov rdi, rax
mov eax, 0
call sym.imp.__isoc99_scanf ; int scanf(const char *format)
```
The first instruction, `lea rax [var_70h]`, loads the address of the `var_70h` variable into the `rax` register.

The second instruction, `mov rsi, rax`, moves the `var_70h` address into the `rsi` register from the `rax` register. The `scanf` function requires the second argument to be loaded into `rsi`

The third instruction, `lea rax, str._99s`, loads the address of the `str._99s` variable into the `rax` register.

The fourth instruction, `mov rdi, rax`, moves the `str._99s` variable into the rdi register, via the `rax` register. The `scanf` function requires the first argument to be loaded into `rdi`

The fifth instruction, `mov eax, 0`, this sets the scanf function to not accept floating point number values.

The sixth instruction, `call sym.imp.__isoc99_scanf`, calls the scanf function, which records user input.
## Recognizing Use of User Input in Code
The following code will load in a variable and use it as part of a formatted string:
```
lea rax, [var_70h]
mov rsi, rax
lea rax, str.Hello___s__Nice_to_meet_you__n ; 0x5570acc6301d ; "Hello, %s! Nice to meet you!\n"                                                                                
mov rdi, rax
mov eax, 0
call sym.imp.printf
```
The first instruction, `lea rax, [var_70h]`, uses the same variable that recorded the user input, `var_70h`, and loads its address into `rax`

The second instruction, `mov rsi, rax`, loads the `var_70h` variable address into `rsi` via `rax`. The printf function uses the `rsi` register as the string to be substituted.

The third instruction, `lea rax, str.Hello___s__Nice_to_meet_you__n`, this contains the hard-coded string to be used in the printf function.

The fourth instruction, `mov rdi, rax`, loads the hard-coded string into the rdi register, which is where the printf function uses for the formatted string

The fifth instruction, `mov eax, 0`, indicates that no vector register or floating point numbers will be used in the printf function

The sixth instruction, `call sym.imp.printf`, is the function call itself.
