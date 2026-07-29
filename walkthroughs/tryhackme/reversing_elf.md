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
##
##
##



