# Radare2 Beginner's Guide
## to open the binary
r2 -d <binary_name>
## analyze the binary
aaa
## list functions
afl
## enter visual mode
V ('q' quits visual mode)
## print disassembly (we can also output to a file)
pdf @ address_or_function_name
pdf @main > main.dis
## run the program inside the debugger
dc
## set a breakpoint at a certain memory address
db memory_address
## show all breakpoints
db
## delete breakpoint at specific address
db- address
## step into the next instruction
ds
## reset the binary
ood
## examine memory address contents at specific address or register
px <number of bytes to output> @ <address or register>
## output the values of variables identified by analysis
afvd
## Notes
var_4h is typically stored at rbp-4 (common to x86-64 calling conventions)
## A limited number of Assembly instructions and their definitions
```
push - put a value on top of the memory stack
mov - put a value into a register
lea - load effective address (used to load in variables)
call - execute a function in the program
ret - exit the function and return to the point of the function call
nop - no operation
pop - remove the top value from the memory stack
endbr64 - marks the start of a function
sub - allocate memory to the stack (?)
cmp - compare a value
leave - clean up the memory stack before returning from a function
jz  - jump if the previous comparison value was equal to zero
jne - jump (not equal) = jump if not equal
jmp - unconditional jump
shl - double the value with left bit shift
inc - increment (add 1) the value by one byte
sub - subtract one value or memory register value from another
```
