# Binary Hacking CTF Buffer Overflow Workflow (x86)
> This document covers how to work with binary hacking challenges that involve buffer overflows
> We assume that we're working in Kali Linux or PicoCTF webshell environment
# Step 1: Inspect the Binary
> We can use the Rabin2 program to check the details of the binary program
```
rabin2 -I <binary_name>
```
> We should take note of the details like:
a) The architecture (x86 vs ARM, etc)
b) The endian byte order (little vs big)
c) The bit-type of the binary (32-bit vs 64-bit)
d) Memory protections (pic, nx, etc)
# Step 2: Identify Overflow Vulnerability
> Each binary will be different, but at some point, we should be able to provide user input
> Run the binary, and confirm that, if we send enough user input, it will crash
# Step 3: Determine Buffer Overflow Offset
> We need to discover the minimum amount of input to cause the binary to crash,
> and after that, determine how many bytes of input we need to send before we can can control
> the IP register (EIP or RIP, for 32-bit or 64-bit binaries, respectively)
a) Use the Ragg2 program to create a pattern of bytes to send to the binary
```
ragg2 -P <number_of_bytes> -r
```
b) Copy the output
c) Use Radare2 to debug the binary (the -A flag analyzes the binary upon startup)
```
r2 -d -A <binary_name>
```
d) Run the binary inside Radare2
```
dc
```
e) When the time to supply user input happens, paste in the ragg2 output and hit enter
> If a crash occurs, move to the next step
> If a crash doesn't occur, run Ragg2 with a larger number, copy the output, then reset the binary inside of Radare2
```
ood
dc
```
> If a crash still doesn't occur, keep running Ragg2 with increasingly larger numbers until it does
f) After the binary has crashed, we can see what data is in the memory registers with the following command
```
dr
```
> We are interested in the value inside the IP register (EIP or RIP, depending on the 32-bit or 64-bit binaries)
> The value of the IP register should contain part of the pattern created by the Ragg2 command. Copy the value for the next command
g) Use the following command to find the offset for buffer overflow
```
ragg2 -q <IP_register_value>
```
> The output will give you the offset in both little endian and big endian order
# Step 4: Figure Out What The Goal of Exercise Is
> Depending on the nature of the CTF challenge, the goal may be to either
a) Run a function located in the binary (a Ret2Win challenge)
> or
b) Run shellcode injected through buffer overflow
> Or perhaps something else. If source code has been provided, that will help alot
> We'll follow this guide up with others, detailing the workflow for ret2win challenges, shellcode challenges, and possible others.
Finis
