#include <stdio.h>
//compile this code on Linux with the following command:
//gcc -o r2test r2test.c
void checkAndDoubleHackerNumber() {
    int hacker_number = 1337;

    while (1) {
        if (hacker_number == 1337) {
            printf("Hacker Number is 1337. Doubling the value...\n");
            hacker_number *= 2;
        } else {
            printf("Hacker Number is not 1337! Exiting the loop.\n");
            break;
        }
    }
}

void helloWorld() {
    printf("Hello, World!\n");
}

int main() {
    checkAndDoubleHackerNumber();
    helloWorld();
    return 0;
}
