# URL
https://training.olicyber.it/challenges#challenge-286
# Concept
* manually changing memory addresses in the middle of program execution
# Method of solve
* startup the binary with `radare2`
```
r2 -d ./sw-16       # start the debugger
aaa                 # analyze the binary
afl | head          # see the first few functions in the binary
db sym.imp.sleep    # set a breakpoint for the sleep function
dc                  # run the program, which stops when the sleep function runs
s obj.tochange      # go to the memory address of the tochange section
wx fe0fdcbadec0adde # write the desired bytes in hex (in little endian order)
dc                  # run the program, which will output the flag
```
