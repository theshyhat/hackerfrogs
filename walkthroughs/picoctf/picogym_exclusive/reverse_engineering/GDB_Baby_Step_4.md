# URL
https://play.picoctf.org/practice/challenge/398
# Concept
* examine the value that is passed to multiplication in Assembly
* examining other functions
# Method of solve
* the challenge instructs us to look at the value that is multiplied by the EAX register, converted to decimal
* download the binary file
* the important value to observe is the final operand in the `imul` instruction 
```
r2 -d ./debugger0_d # open it up in radare2
aaa                 # analyze the binary
afl | head          # get a list of the binary's functions
pdf @ main          # disassemble the main function
pdf @ sym.func1     # disassemble the function we found in the main function
? 0x3269            # get the conversion of the value in different units. we want the int32 one
```
* the flag, with the PicoCTF flag wrapper is: `picoCTF{12905}`
