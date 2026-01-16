// compile with:
// gcc add_2_num_func.c -o add_2_num_func
#include <stdio.h>

/* Function that adds two integers */
int add_numbers(int a, int b) {
    printf("Adding the numbers %d and %d...\n", a, b);
    return a + b;
}

int main(void) {
    int x, y;

    printf("Enter the first number: ");
    scanf("%d", &x);

    printf("Enter the second number: ");
    scanf("%d", &y);

    int result = add_numbers(x, y);

    printf("The result is %d\n", result);

    return 0;
}
