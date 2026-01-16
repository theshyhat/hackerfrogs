// compile with:
// gcc loop.c -o loop
#include <stdio.h>

int main(void) {
    char word[5];  // 4 characters + null terminator

    printf("Enter a 4-character word: ");
    scanf("%4s", word);  // limit input to 4 characters

    printf("Your word is %s\n", word);

    for (int i = 0; i < 4; i++) {
        printf("Character %d is: %c\n", i + 1, word[i]);
    }

    return 0;
}
