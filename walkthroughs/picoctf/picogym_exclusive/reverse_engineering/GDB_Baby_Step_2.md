# URL
https://play.picoctf.org/practice/challenge/396
# Concept
* examining memory register values
# Method of solve
* the challenge instructs us to get the value of the `eax` register at the end of the `main` function
* download the binary file
```
r2 -d ./debugger0_b # open it up in radare2
aaa                 # analyze the binary
afl | head          # get a list of the binary's functions
pdf @ main          # disassemble the main function
db        # set a breakpoint for the end of the main function
dc                  # run the program until the breakpoint
dr eax              # examine the value of the eax register
? 0x0004af4b        # convert the value to a lot of different notations, we're looking for the int32 value
```
* the flag, with the PicoCTF flag wrapper is: `picoCTF{307019}`
