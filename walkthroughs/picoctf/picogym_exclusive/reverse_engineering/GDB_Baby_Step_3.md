# URL
https://play.picoctf.org/practice/challenge/397
# Concept
* examine the value of a variable at a specific point in program execution
# Method of solve
* the challenge instructs us to look at the value of the memory location where the `0x2262c96b` value is loaded into a memory address in the main function, then get the value that is loaded in
* download the binary file
```
r2 -d ./debugger0_b # open it up in radare2
aaa                 # analyze the binary
afl | head          # get a list of the binary's functions
pdf @ main          # disassemble the main function
db 0x00401142       # set a breakpoint for the end of the function
dc                  # run the program until the breakpoint
dr eax              # examine the eax register value
? 0x0004af4b        # get the conversion of the value in different units. we want the int32 one
```
* the flag, with the PicoCTF flag wrapper is: `picoCTF{307019}`
