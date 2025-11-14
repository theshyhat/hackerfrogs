When we view the source code, the user input buffer is defined as 16 bytes. That means that after the 16th byte of input, we begin overflowing the buffer into other parts of memory.

From the disassembly, we see that 0x40 is moved into the var_8h variable at the 5th instruction, so that variable is where the NUM variable is stored

The program then accepts user input with the gets function. We know that the input buffer is only 16 bytes, and the goal is to overflow into the num variable

We can find out at which point the overflow reaches the num variable memory address with the following commands
```
ragg2 -P 250 -r
```
This creates a pattern that can be retrieved and referenced to get the offset to overflow into the num memory address

We create a breakpoint at the 7th instruction, immediately after we provide user input

Run the program
```
dc
```
Then at the point when we are prompted for input, paste in the ragg2 output string

Then, at the breakpoint, we use the following instruction to output the values of variables
```
afvd
```
In the var_8h variable, there is the following value
```
0x414b41414a414149
```
So we can find out the overflow offset to enter the num variable memory address with the following command
``` 
ragg2 -q 0x414b41414a414149
```
This tells us that the offset is 24, so we can send any 24 bytes, then for the 25th byte, send ASCII `A` (hex 0x41), to fulfill the program requirements to output the flag contents

We can send the following Perl command to overflow and overwrite the Num variable

perl -e 'print "A" x 24 . "A"' | ./local-target
