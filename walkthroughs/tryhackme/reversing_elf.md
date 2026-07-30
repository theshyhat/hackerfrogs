# URL
https://tryhackme.com/room/reverselfiles
# Concepts
* reverse engineering concepts
* strings
* 
# Method of solving
## Crackme1
* all you need to is run the binary and it gives you the flag
## Crackme2
* we need to get the super secret password, which we can find in the strings
```
strings ./crackme2
```
* then run the binary with the password as the argument
```
./crackme2 super_secret_password
```
## Crackme3
* when we look at the strings for this binary, we make some observations
  * there is what we suspect to be a base-64 encoded string among the strings
  * the base64 character set is one of the strings
    * `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/`
* we take the base64-encoded string and decode it
* we use with the binary to get the flag:
```
./crackme3 f0r_y0ur_5ec0nd_le55on_unbase64_4ll_7h3_7h1ng5
``` 
## Crackme4
* this crackme is using the strcmp function to validate the password
* the password is not in the strings for the binary
* we need to set a breakpoint for right before the password is compared in the binary
* then look in the memory registries for the password value
```
r2 -d ./crackme4 test
aaa
pdf @ main             # we see there's another function being used to compare passwords   
pdf @ sym.compare_pwd  # we see that the password is being compared with a strcmp function
db 0x004006d5          # set a breakpoint for the moment the comparison is made
px @ rax               # look in the memory registers for the password
```
## Crackme5
* in this binary, the strcmp function is being used to validate the password
* the password is being passed into the program as user input
* in radare2, we ID the point in program execution where the comparison is made
* we set a breakpoint for that instruction
* then examine the `rdi` and `rsi` memory registers to see what is being compared
```
r2 -d ./crackme5
aaa
afl
pdf @ main    # we see the comparison operation with the call to sym.strcmp
db 0x00400837 # set a breakpoint for the the strcmp function call    
dc            # run the binary, and supply a test password
test          # the test password
px @ rsi      # this register contains the string to compare against
```
## Crackme6
* in this binary, the password is being compared byte by byte instead of compared using a function like `strcmp`
* we need to examine the function doing the byte-by-byte comparison to obtain the password
```
r2 -d ./crackme6
aaa
pdf @ main                # observe that sym.compare_pwd is being called
pdf @ sym.compare_pwd     # another function sym.my_secure_test, is being called
pdf @ sym.my_secure_test  # note that the byte-by-byte comparisons tell us the password
```
## Crackme7
* in this challenge, we see a special message after a comparison instruction
* we need to figure what triggers the comparison instruction
```
r2 -d ./crackme7
aaa
pdf @ main         # there is a string printed out tell us "we won" and then runs a function to
                   # print the flag
                   # if we look at the memory location being compared, we see that it's
                   # the same memory location that is used to record our user input
                   # from the main menu of the program
db 0x08048665      # set the breakpoint for right before the comparison
dc                 # run the program, but put in the number being compared `31337` in the menu
px @ ebp-0xc       # we can see our user input in the this memory location
```
## Crackme8
* one thing we take note of when we look at the strings for this binary is that it's using the `atoi` function
  * this function converts ASCII characters to integers
* we also observe a `cmp` instruction that compares `eax` (likely our user input) to `0xcafef00d`
* if we convert those hex bytes to an integer, we get `-889262067`
* we submit this as the argument to the binary and get the flag
```
r2 -d ./crackme8
aaa
pdf @ main        # we observe that there's a cmp instruction with the hex bytes 0xcafef00d
                  # we also observe that there's an atoi function being used, likely on our                       # user input
                  # so we supply the integer equivalent of 0xcafef00d as an argument                              # (-889262067) to get the flag
```


