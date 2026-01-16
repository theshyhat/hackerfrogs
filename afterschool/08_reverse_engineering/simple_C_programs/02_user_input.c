// compile with:
// gcc user_input.c -o user_input
#include <stdio.h>

int main(void) {
    // Define the name variable and its max size
    char name[64];
    printf("Enter your name: ");
    // Save user input to the input variable
    fgets(name, sizeof(name), stdin);
    // Use the input in a print command
    printf("Your name is %s\n", name);
    return 0;
}
