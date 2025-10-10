# URL
https://training.olicyber.it/challenges#challenge-283
# Concept
* translating register values into different formats
# Method of solve
* we can use radare2 to open the binary and inspect it:
```
r2 -d ./sw-13
aaa
pdf @ main
db 0x556f6984f133
dc
dr
```
* our instructions are to look at the value of the `rax` register, but in a signed integer format
* in radare, we can use the `? <some_data>` command to output the data provided in multiple formats. we grab the value in the `rax` register, then
```
? 0xfa3b194730d04f94
```
* in the output, we can see that the signed integer value is this: `-415710747049308268`
* the instructions tell us to provide that value, but without the `-` or `+` signs as the value of the flag
* we need to put the value in between the flag wrapper, which is `flag{<value_goes_here>}`


