# URL
https://hackropole.fr/en/challenges/reverse/fcsc2023-reverse-aaarg/
# Concept
* binary read-only data
* extracting the .rodata section from a binary
# Method of solve
* in this challenge there's hidden data in the `.rodata` section that was no stripped out of the binary
## Using Linux tools
* to extract the `.rodata` section using Linux tools, you can use `objdump`
```
objdump -s -j ".rodata" aaarg 
```
* but this is messy. We can use Linux-fu to clean up the output and get the flag:
```
objdump -s -j ".rodata" aaarg | awk '{print $NF}' | tr -d "." | tr -d "\n"
```
## Using Radare2
* we can use the `iS` command to output all the symbols association with the binary
* we find the `.rodata` symbol and use its associated memory address
```
px 512 @ 0x00402000
```
