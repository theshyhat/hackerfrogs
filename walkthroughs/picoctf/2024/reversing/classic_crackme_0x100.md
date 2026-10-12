# URL
https://learn.cylabacademy.org/library/409?page=2&category=3&difficulty=2
# Concept
* x86 Linux ELF binary reversing
* input transformation (letter shift)
# Method of solve
* when we run this binary, we see that it's looking for a password which will output the flag
* when we look at the disassembly, we see that there's a string being loaded into memory:
```
movabs  rax, 0x726d6175786c706c ; main_sample.c:13 ; 'lplxuamr'
movabs  rdx, 0x73637a6872676573 ; 'segrhzcs'
mov     qword [output[0]], rax
mov     qword [output[8]], rdx
movabs  rax, 0x716572617478756b ; 'kuxtareq'
movabs  rdx, 0x69636c6f63716f62 ; 'boqcolci'
mov     qword [output[16]], rax
mov     qword [output[24]], rdx
movabs  rax, 0x7a706a6d7774666b ; 'kftwmjpz'
movabs  rdx, 0x7062767a636d6b6e ; 'nkmczvbp'
mov     qword [output[32]], rax
mov     qword [output[40]], rdx
mov     dword [output[47]], 0x766d70 ; 'pmv'
```
* this is the string that's going to be compared against later
  * note that the last write to the `output` array overwrites the last character from the previous string, so:
  * the last part of the string is `nkmczvbpmv`, not `nkmczvbppmv`
  * so the whole string that's being compared is `lplxuamrsegrhzcskuxtareqboqcolcikftwmjpznkmczvbpmv`
* our user input is recorded here:
```
lea     rax, [input[0]] ; main_sample.c:17
mov     rsi, rax
mov     edi, str.50s ; 0x402024 ; const char *format
mov     eax, 0
call    __isoc99_scanf ; sym.imp.__isoc99_scanf ; int scanf(const char *format)
```
* so our user input is written to the `input` variable, and is limited to 50 characters
* next, we see there's a transformation performed on our input (from the decompiler):
```
i = 0;
iVar1 = strlen(&output);
for (; i < 3; i = i + 1) {
  for (var_a4h._0_4_ = 0; (int32_t)var_a4h < iVar1; var_a4h._0_4_ = (int32_t)var_a4h + 1) {
    uVar2 = ((int32_t)var_a4h % 0xff >> 1 & 0x55U) + ((int32_t)var_a4h % 0xff & 0x55U);
    uVar2 = ((int32_t)uVar2 >> 2 & 0x33U) + (uVar2 & 0x33);
    iVar3 = ((int32_t)uVar2 >> 4) + input[(int32_t)var_a4h] + -0x61 + (uVar2 & 0xf);
    input[(int32_t)var_a4h] = (char)iVar3 + (char)(iVar3 / 0x1a) * -0x1a + 'a';
  }
}
```
* `iVar1` is the length of the output variable (50 bytes)
```
for (; i < 3; i = i + 1)
```
* this is a (outer) loop that will run 3 times, because `i` is initialized to `0`
```
for (var_a4h._0_4_ = 0; (int32_t)var_a4h < iVar1; var_a4h._0_4_ = (int32_t)var_a4h + 1)
```
* this is a (inner) loop that will run a number of times equal to the `iVar1` value (50 times)
```
uVar2 = ((int32_t)var_a4h % 0xff >> 1 & 0x55U) + ((int32_t)var_a4h % 0xff & 0x55U);
uVar2 = ((int32_t)uVar2 >> 2 & 0x33U) + (uVar2 & 0x33);
```
* `uVar2` is the number of `1`s when the index number of `var_a4h` (our user input) is represented as a binary number:
  * e.g., `uVar2` = 0 at index 0 (0 in binary (no 1s)), `uVar2` = 1 at index 1 (1 in binary (one 1s)), and `uVar2` = 3 at index 4 (111 in binary (three 1s))
```
iVar3 = ((int32_t)uVar2 >> 4) + input[(int32_t)var_a4h] + -0x61 + (uVar2 & 0xf);
```
* this part of the loop calculates the hexadecimal value of `input` index's character value, then adds the `uVar2` value (the number of binary 1s from the index number)
```
input[(int32_t)var_a4h] = (char)iVar3 + (char)(iVar3 / 0x1a) * -0x1a + 'a';
```
* lastly, the character at the `input` index is replaced by character calculated at the `iVar3` variable
* so the whole loop is a modified version of the `Caesar Cipher` where the shift number is dependent on the index number of the character in the string
* since we know the string that is being compared against, this Python script will output the password which will be accepted by the program:
```Python
target_str = 'lplxuamrsegrhzcskuxtareqboqcolcikftwmjpznkmczvbpmv'
decrypted_str = ""

for index,value in enumerate(target_str):
  decrypted_letter = value
  for i in range(3):
    shift_num = str(bin(index)).count("1")
    decrypted_letter = chr((ord(decrypted_letter) - 97 - shift_num) % 26 + 97)
    print(f"Shift: {shift_num}, Decrypted Letter: {decrypted_letter}")

  decrypted_str += decrypted_letter

print(decrypted_str)
```
