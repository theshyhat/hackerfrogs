// compile with:
// gcc add_2_num_arg.c -o add_2_num_arg
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <num1> <num2>\n", argv[0]);
        return 1;
    }

    int a = atoi(argv[1]);
    int b = atoi(argv[2]);

    printf("Adding the numbers %d and %d...\n", a, b);

    int result = a + b;

    printf("The result is %d\n", result);

    return 0;
}
