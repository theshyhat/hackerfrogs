# URL
https://pwnable.kr/play.php
# SSH Command
ssh col@pwnable.kr -p2222 (pw:guest)
# Source Code
```
#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
                res += ip[i];
        }
        return res;
}

int main(int argc, char* argv[]){
        if(argc<2){
                printf("usage : %s [passcode]\n", argv[0]);
                return 0;
        }
        if(strlen(argv[1]) != 20){
                printf("passcode length should be 20 bytes\n");
                return 0;
        }

        if(hashcode == check_password( argv[1] )){
                setregid(getegid(), getegid());
                system("/bin/cat flag");
                return 0;
        }
        else
                printf("wrong passcode.\n");
        return 0;
}
```
# Concept
* hexadecimal math
* 32-bit integer math
* "hash" collisions
# Method of solve
* according to the code, we have to submit a 20-byte argument with the binary:
```
if(strlen(argv[1]) != 20){
  printf("passcode length should be 20 bytes\n");
  return 0;
}
```
* we see that the argument to the binary is used as the parameter to the `check_password` function and checked against the `hashcode` variable
* and if the check passes, then the contents of the flag is read
```
if(hashcode == check_password( argv[1] )){
  setregid(getegid(), getegid());
  system("/bin/cat flag");
  return 0;
}
```
* the value of `hashcode` is `0x21DD09EC`
* now let's see what the `check_password` function is:
```
unsigned long check_password(const char* p){
  int* ip = (int*)p;
  int i;
  int res=0;
  for(i=0; i<5; i++){
    res += ip[i];
  }
  return res;
}
```
* the parameter to the function is named `p`, which is the binary argument, and is treated as a pointer to characters
* a pointer, `ip` which is an array made up of the contents of `p`, cast to an interger array, which are four bytes per array element
* this means that `ip[0]` contains the first four bytes of the binary argument, `ip[1]` contains the next four bytes of the binary argument, etc, etc
* the `res` variable starts as an zero integer, is added to by the for loop, which adds the values of each element of the `ip` array to the `res` total
* `res` is then returned by the function
* to know which 20 bytes we need to sent as the argument to the binary and get the flag, we'll go over two possible solutions
## Payload 1 (ASCII-printable Characters)
* if we want to use only printable characters to solve this challenge, we can send this as the argument to the binary to solve the challenge
```
./col ',,,,,,,,,,,,,,,,<Y,q'
```
* when we inspect the 5 sets of characters used to form the final value, they are:
```
,,,, = 0x2c2c2c2c
,,,, = 0x2c2c2c2c
,,,, = 0x2c2c2c2c
,,,, = 0x2c2c2c2c
<Y,q = 0x712C593C
--------------------------------
      0x121DD09EC
```
* we notice that the result actually doesn't match the hashcode value `0x21DD09EC`, but we have to remember
* in C code, ints are 32-bit integers, which means that in hexadecimal base, all digits to the left of the first 8 digits (starting from right-side of the number) will be dropped, resulting in the value `0x21DD09EC`, which is the value of the `hashcode` variable
* if we take the sum of the hexadecimal values before the value `0x712C593C`, we get the hex value `0xB0B0B0B0`
  * if we subtract `0xB0B0B0B0` from the hashcode, `0x21DD09EC`, the result is `-0x8ED3A6C4`
  * we would assume that the final set of hex values to add to `0xB0B0B0B0` to arrive at the `hashcode`:`0x21DD09EC` would be a positive number, but the reality is...
  * `-0x8ED3A6C4` and `0x712C593C` are the same number in terms of 
## Payload 2 (Non-Printable Characters)
```
./col "$(printf '\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\xE8\x05\xD9\x1D')"
```
