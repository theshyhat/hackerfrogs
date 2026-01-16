// compile with:
// gcc argument.c -o argument
#include <stdio.h>

int main(int argc, char **argv) {
    char *argument = argv[1];
    printf("The program argument is: %s\n", argument);
    return 0;
}
