# URL
https://pwnable.kr/play.php
# SSH Command
ssh fd@pwnable.kr -p2222 (pw:guest)
# Source Code
```
char buf[32];
int main(int argc, char* argv[], char* envp[]){
        if(argc<2){
                printf("pass argv[1] a number\n");
                return 0;
        }
        int fd = atoi( argv[1] ) - 0x1234;
        int len = 0;
        len = read(fd, buf, 32);
        if(!strcmp("LETMEWIN\n", buf)){
                printf("good job :)\n");
                setregid(getegid(), getegid());
                system("/bin/cat flag");
                exit(0);
        }
        printf("learn about Linux file IO\n");
        return 0;

}
```
# Concept
* understand what Linux (Unix) file descriptors are
# Method of solve
* the source code tells us that we have to give an argument to the binary's execution
```
int main(int argc, char* argv[], char* envp[]){
        if(argc<2){
                printf("pass argv[1] a number\n");
                return 0;
        }
```
* the next part of the code let us know that we have to set the `fd` variable to something specific:
```
int fd = atoi( argv[1] ) - 0x1234;
```
* so whatever argument we provide to the binary will have its value subtracted by `0x1234`, which is 4660 in decimal
* the *nix file descriptors are `stdin`, `stdout` and `stderr`, which are associated with the numbers, `0`, `1`, and `2`, respectively
* what we want to do is set the file descriptor (`fd`) to `stdin`, which is the number 0
* why? we need to set the file descriptor to stdin so we can enter the `LETMEWIN` string:
```
if(!strcmp("LETMEWIN\n", buf)){
                printf("good job :)\n");
                setregid(getegid(), getegid());
                system("/bin/cat flag");
                exit(0);
        }
```
* this code let us get the flag for the challenge
* if we did not set the `fd` variable to 0 by supplying 4460 as the argument to the binary command, we wouldn't be able to input the answer `LETMEWIN` and get the flag
* so the method of solve is:
```
./fd 4660
LETMEWIN
```


