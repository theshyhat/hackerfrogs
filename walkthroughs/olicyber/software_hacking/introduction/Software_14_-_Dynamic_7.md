# URL
https://training.olicyber.it/challenges#challenge-284
# Concept
* examining program memory locations at specific points of execution
# Method of solve
* the challenge wants us to execute the program until the `int3` in the `main` function, then take the value in the rbp-0x4 memory address and use the float value of the data and get only the decimal portion of the float and put it between the flag wrapper, then submit that as the flag
* we can solve the challenge by downloading the program and inspecting it with `radare2`:
```
r2 -d ./sw-14      # start the program
aaa                # analyze the binary
pdf @ main         # print disassembly function at main
db 0x5571b04aa130  # set a breakpoint at the specified hex memory address
dc                 # run the program until the break point
afv                # list out the program variables
px @ rbp-0x4       # prints out the contents of the specified memory address
```
* we see that the value in the memory address is `0x46f4d244`, but we want the float conversion of that data
* we can see the conversion of that data into many formats using this command:
```
? 0x46f4d244
```
* we see that the float value is `31337.132812500000000f`, and the challenge wants us to put the decimal portion only in between the flag wrapper
