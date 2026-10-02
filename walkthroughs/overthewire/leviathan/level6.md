# Password
redacted
# Concept
* how programs load values into memory
# Method of solve
* when we run the binary, it tells us we need to pass a 4-digit number along with it to run
* we debug the binary using radare2:
```
r2 -d ./leviathan6
aaaa
pdf @ main
```
* the program loads in a value into the `var_ch` variable
```
mov dword [var_ch], 0x1bd3
```
* later on in the program there's a comparison between the contents of `var_ch` and `eax`, which contains the first argument passed when running the binary:
```
cmp dword [var_ch], eax
```
* when we decode the hex value passed into memory back into decimal, we get the value `7123`
* and that is what we pass to the program:
```
./leviathan6 7123
```
* this gives an interactive shell with the `leviathan7` user
* read the password for `leviathan7`:
```
cat /etc/leviathan_pass/leviathan7
```
