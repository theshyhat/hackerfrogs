# SSH Command / Password
ssh bof@pwnable.kr -p2222 (pw: guest)
# Code
```
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void func(int key){
        char overflowme[32];
        printf("overflow me : ");
        gets(overflowme);       // smash me!
        if(key == 0xcafebabe){
                setregid(getegid(), getegid());
                system("/bin/sh");
        }
        else{
                printf("Nah..\n");
        }
}
int main(int argc, char* argv[]){
        func(0xdeadbeef);
        return 0;
}
```
# Concept
* stack buffer overflow
* variable overwrite to win
* overcoming stack smashing memory protection
# Method of solve
* this binary is an example of a `variable overwrite to win` challenge
* if the `key` variable is set to `0xcafebabe`, then the binary's running effective group ID is changed and a shell is opened:
```
if(key == 0xcafebabe){
  setregid(getegid(), getegid());
  system("/bin/sh");
}
```
* the method of overwriting the `key` variable is through the memory unsafe `gets` function, which is used to store user input:
```
void func(int key){
  char overflowme[32];
  printf("overflow me : ");
  gets(overflowme);       // smash me!
```
* we see that a char array for the `overflowme` variable is set to 32 characters
* the `gets` function is called and saves user input to the `overflowme` buffer, which has a maximum size of 32 characters
  * which means that user input in excess of 32 characters will overflow into 
