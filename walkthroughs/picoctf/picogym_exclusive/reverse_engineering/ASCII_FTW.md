> This challenge requires us to look at the disassembly of the main function using a debugger. In our case, we'll use the Radare2 debugger
```
r2 -d asciiftw
aaa
afl
pdf @ main
```
> From here, copy the disassembly with the ASCII characters and save the output to a file, flag.txt
```
cat flag.txt | cut -d"'" -f2 | tr -d '\n'
```
