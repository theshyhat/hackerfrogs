// compile with:
// gcc if_1337_xor.c -o if_1337_xor
#include <stdio.h>

int main(void) {
    int user_input;

    int a = 0x10;
    int b = 0x529;
    int secret = a ^ b;

    printf("What is the elite hacker number? ");
    scanf("%d", &user_input);

    if (user_input == secret) {
        printf("CORRECT! You win!\n");
    } else {
        printf("That's not the number I want!\n");
    }

    return 0;
}
