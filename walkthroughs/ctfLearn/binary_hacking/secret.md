# URL
https://ctflearn.com/challenge/1514
# Concept

# Source Code
```C
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/time.h>
#include <stdint.h>

void print_flag(){
    char flag[64];
    FILE *f = fopen("./flag.txt", "rt");
    if (f == NULL){
        puts("Missing flag file");
        return;
    }

    fgets(flag, sizeof(flag), f);
    printf("Here is your prize: %s\n", flag);
    fclose(f);
}

uint32_t get_seed(){
        uint32_t random;
        getrandom(&random, sizeof(random), 0);
        return random;
}

void guess_me(){
    char secret_password[33], user_input[33];
    memset(user_input, '-', 33);
    memset(secret_password, 0, 33);

    srand(get_seed());
    for(int i = 0; i < 32; i++){
        secret_password[i] = (rand() % 6) + 97;
    }

    read(STDIN_FILENO, user_input, 32);

    int input_len = strlen(user_input);
    if(input_len > 1){
        if(strncmp(secret_password, user_input, input_len)){
            puts("No flag for you!");
        }else{
            print_flag();
        }
    }else{
        puts("Password is too short!");
    }
}

int main(int argc, char *argv[]){
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    guess_me();

    return 0;
}
```
# Method of solve



