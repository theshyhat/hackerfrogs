# URL
https://play.picoctf.org/practice/challenge/396
# Concept
* examining memory register values
# Method of solve
* the challenge instructs us to get the value of the `eax` register at the end of the `main` function
* download the binary file
```
r2 -d ./debugger0_c # open it up in radare2
aaa                 # analyze the binary
afl | head          # get a list of the binary's functions
pdf @ main          # disassemble the main function
db 0x0040111c       # set a breakpoint for after the target value is loaded into the var_4h variable
dc                  # run the program until the breakpoint
afv                 # list out the addresses of variables
px4 @ rbp-0x4       # get the first 4 bytes in hex units at the variable's memory address
```
* because this binary was compiled with little endian byte order, the 
* the flag, with the PicoCTF flag wrapper is: `picoCTF{0x6bc96222}`
