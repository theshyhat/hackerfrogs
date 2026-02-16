# URL
https://training.olicyber.it/challenges#challenge-285
# Concept
* looking in specific memory addresses during program execution
# Method of solve
* the challenge wants us to look at the value of the `rbp-0x8` memory address when the `puts()` function is called in the program
* we can use the `radare2` program to solve the challenge with these commands:
```
r2 -d ./sw-15      # starts the r2 debugger
aaa                # analyzes the binary
afl                # list out all of the functions. note the memory address of the puts function
db 0x55a5aa1f6030  # set a breakpoint for the memory address of the puts function
dc                 # run the program until the breakpoint
px @ rbp-0x8       # look at the value inside of the variable location
```
* we take the hex value in the variable memory location and put the flag wrapper around it, then submit it as the flag
