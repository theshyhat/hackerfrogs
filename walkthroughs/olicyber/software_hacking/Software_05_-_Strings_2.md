# URL
https://training.olicyber.it/challenges#challenge-259
# Concept
* more strings
# Method of solve
* we can use Radare2 to inspect the binary
```
r2 -d ./sw05
```
* from there, we can analyze and disassemble the `main` function
```
aaa
pdf @ main
```
* we can see the flag string in the instructions next to `lea rax, obj.flag`
