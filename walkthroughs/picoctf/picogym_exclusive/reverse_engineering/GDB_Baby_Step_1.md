# URL
https://play.picoctf.org/practice/challenge/395
# Concept
* reading memory register values
# Method of solve
* the challenge instructs us to get the value of the `eax` register at the end of the `main` function
* download the binary file
```
r2 -d ./debugger0_a # open it up in radare2
aaa                 # analyze the binary
afl | head          # get a list of the binary's functions
pdf @ main          # disassemble the main function
db 0x55d2887be13e   # set a breakpoint for the end of the function
dc                  # run the program until the breakpoint
dr eax              # examine the eax register value
? 0x00086342        # get the conversion of the value in different units. we want the int32 one
```
* the flag, with the PicoCTF flag wrapper is: `picoCTF{549698}`
