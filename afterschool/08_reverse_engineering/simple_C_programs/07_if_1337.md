// compile with:
// gcc if_1337.c -o if_1337
#include <stdio.h>

int main(void) {
    int number;

    printf("What is the elite hacker number? ");
    scanf("%d", &number);

    if (number == 1337) {
        printf("CORRECT! You win!\n");
    } else {
        printf("That's not the number I want!\n");
    }

    return 0;
}
