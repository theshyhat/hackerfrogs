# URL
https://training.olicyber.it/challenges#challenge-282
# Concept
* inspecting memory registers at specific points in program execution
# Method of solve
* the first we want to is open up the binary with our debugger, radare2
```
r2 -d ./sw-12
```
* from there, we can analyze the binary and look at the disassembled `main` function with these commands
```
aaa
pdf @ main
```
* the instructions for the challenge ask us to look at the memory registers right before the `int3` instruction is executed
* we can set a breakpoint for that program address with the following command
```
db 0x55a70240215a
```
* after that, we can run the program until the breakpoint with this command:
```
dc
```
* after hitting the breakpoint, we can inspect the values in the memory registers with this command
```
dr
```
* the challenge instructs us to concatenate the values of the first 3 memory registers, but ommit the 0x portion of it, which results in this value:
```
15af56f2f4295e9d38
```
* the last thing we need to do is put the value inside of the flag wrapper, which is `flag{<value_goes_here>}`



