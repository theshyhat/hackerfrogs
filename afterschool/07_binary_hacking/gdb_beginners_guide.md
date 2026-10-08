# Concept
* this guide is meant to record some beginner's commands for the GDB program to perform basic debugging tasks and aid in doing reverse engineering exercises
# Starting Commands
* setting the disassembly flavor
  * the disassembly flavor in GDB is set to AT&T by default, and it's not fun to look at
  * so we should run this command to set the disassembly flavor to Intel
  * `set disassembly-flavor intel`
# Running the program
* this command runs the program as usual
  * `run`
  * if you want to restart / reset the program just use `run` again
  * if you want to run the program with arguments, you can use:
  * `run arg1 arg2`
  * if we're in the middle of execution we can use the following command to continue:
    * `c` or `continue`
# Looking at memory locations
* this lets us see the memory register values:
  * `info registers`
  * to be more specific you can use:
  * `p $reg_name` <-- for example `p $eax`, `p` is short for `print`
    * you can also specify decimal or hex output, `p/x` or `p/d`
  * you can also use `e` or `examine`, which lets us look at the contents of the memory address
    * for example: `x/4i $eip` <-- examine the contents of the memory address of `eip` and the 3 instructions that follow
# Setting Breakpoints
* the basic command to set breakpoints in the program is:
  * `b *<address>` or `break`, and you also have to give a memory address as an argument
    * e.g., `b *0x56556311`
  * deleting breakpoints can be done with `delete #`, where `#` is the breakpoint number, which you can retrieve with `info b`
  * we can delete all breakpoints by using the `delete` command by itself
  * we can list all set breakpoints with `info breakpoints` or `info b`
# Stepping Through The Program
* this command will step to the next instruction, and also dive into functions:
  * `step`
* this command will step to the next instruction, but not dive into functions:
  * `next`
* this command will continue program execution until the end of the current function:
  * `finish`
* and this command will continue program execution until the end of the program (or breakpoint is hit)
  * `continue` or `c`
# Program variables
* we can use this command to get all of the variable names in the program:
  * `info variables` or `info var`
# Program functions
* this command will retrieve function names in the program:
  * `info functions` or `info func` or `info fun`



