# URL
https://hackropole.fr/en/challenges/reverse/fcsc2021-reverse-guessy/
# Concept
* reverse engineering
  * XOR operations
  * byte-by-byte comparison
  * bit shift operations
# Method of solve
## Part 1 - Byte Comparisons
* in this part, we are only looking for the bytes that are being compared
* we can find the bytes in the `sym.validate` function
```asm
│           0x004014da      3c46           cmp al, 0x46                ; 'F' ; 70
│       ┌─< 0x004014dc      752d           jne 0x40150b
│       │   0x004014de      488b45f8       mov rax, qword [var_8h]
│       │   0x004014e2      4883c001       add rax, 1
│       │   0x004014e6      0fb600         movzx eax, byte [rax]
│       │   0x004014e9      3c43           cmp al, 0x43                ; 'C' ; 67
│      ┌──< 0x004014eb      751e           jne 0x40150b
│      ││   0x004014ed      488b45f8       mov rax, qword [var_8h]
│      ││   0x004014f1      4883c002       add rax, 2
│      ││   0x004014f5      0fb600         movzx eax, byte [rax]
│      ││   0x004014f8      3c53           cmp al, 0x53                ; 'S' ; 83
│     ┌───< 0x004014fa      750f           jne 0x40150b
│     │││   0x004014fc      488b45f8       mov rax, qword [var_8h]
│     │││   0x00401500      4883c003       add rax, 3
│     │││   0x00401504      0fb600         movzx eax, byte [rax]
│     │││   0x00401507      3c43           cmp al, 0x43                ; 'C' ; 67
│    ┌────< 0x00401509      740c           je 0x401517
│    │└└└─> 0x0040150b      bfb8224000     mov edi, str.Well_it_does_not_begin_well_for_you. ; 0x4022b8 ; "Well it does not begin well for you."                                                                              
│    │      0x00401510      e81bfbffff     call sym.imp.puts           ; int puts(const char *s)
│    │  ┌─< 0x00401515      eb34           jmp 0x40154b
│    └────> 0x00401517      488b45f8       mov rax, qword [var_8h]
│       │   0x0040151b      4883c004       add rax, 4
│       │   0x0040151f      0fb600         movzx eax, byte [rax]
│       │   0x00401522      3c7b           cmp al, 0x7b                ; '{' ; 123
```
* the string we're looking for is `FCSC{`
## Part 2 - More Byte Comparisons
* in this part, we continue to look for direct byte-by-byte comparisons in the `sym.difficult_part` function
```
│      │    0x004011fe      3c65           cmp al, 0x65                ; 'e' ; 101
│      │┌─< 0x00401200      7538           jne 0x40123a
│      ││   0x00401202      0fb645f1       movzx eax, byte [var_fh]
│      ││   0x00401206      3c37           cmp al, 0x37                ; '7' ; 55
│     ┌───< 0x00401208      7530           jne 0x40123a
│     │││   0x0040120a      0fb645f2       movzx eax, byte [var_eh]
│     │││   0x0040120e      3c35           cmp al, 0x35                ; '5' ; 53
│    ┌────< 0x00401210      7528           jne 0x40123a
│    ││││   0x00401212      0fb645f3       movzx eax, byte [var_dh]
│    ││││   0x00401216      3c35           cmp al, 0x35                ; '5' ; 53
│   ┌─────< 0x00401218      7520           jne 0x40123a
│   │││││   0x0040121a      0fb645f4       movzx eax, byte [var_ch]
│   │││││   0x0040121e      3c32           cmp al, 0x32                ; '2' ; 50
│  ┌──────< 0x00401220      7518           jne 0x40123a
│  ││││││   0x00401222      0fb645f5       movzx eax, byte [var_bh]
│  ││││││   0x00401226      3c63           cmp al, 0x63                ; 'c' ; 99
│ ┌───────< 0x00401228      7510           jne 0x40123a
│ │││││││   0x0040122a      0fb645f6       movzx eax, byte [var_ah]
│ │││││││   0x0040122e      3c66           cmp al, 0x66                ; 'f' ; 102
│ ────────< 0x00401230      7508           jne 0x40123a
│ │││││││   0x00401232      0fb645f7       movzx eax, byte [var_9h]
│ │││││││   0x00401236      3c36           cmp al, 0x36                ; '6' ; 54
```
## Part 3 - Comparing Doubled Bytes
* in this part, we're comparing a double of whatever bytes we send to the program
* so what we need to do send bytes that are half of what is indicated
```asm
│    │ ││   0x00401293      01c0           add eax, eax
│    │ ││   0x00401295      83f868         cmp eax, 0x68               ; 'h' ; 104
│    │┌───< 0x00401298      756c           jne 0x401306
│    ││││   0x0040129a      0fb645f1       movzx eax, byte [var_fh]
│    ││││   0x0040129e      0fbec0         movsx eax, al
│    ││││   0x004012a1      01c0           add eax, eax
│    ││││   0x004012a3      3dc6000000     cmp eax, 0xc6               ; 198
│   ┌─────< 0x004012a8      755c           jne 0x401306
│   │││││   0x004012aa      0fb645f2       movzx eax, byte [var_eh]
│   │││││   0x004012ae      0fbec0         movsx eax, al
│   │││││   0x004012b1      01c0           add eax, eax
│   │││││   0x004012b3      3dca000000     cmp eax, 0xca               ; 202
│  ┌──────< 0x004012b8      754c           jne 0x401306
│  ││││││   0x004012ba      0fb645f3       movzx eax, byte [var_dh]
│  ││││││   0x004012be      0fbec0         movsx eax, al
│  ││││││   0x004012c1      01c0           add eax, eax
│  ││││││   0x004012c3      83f864         cmp eax, 0x64               ; 'd' ; 100
│ ┌───────< 0x004012c6      753e           jne 0x401306
│ │││││││   0x004012c8      0fb645f4       movzx eax, byte [var_ch]
│ │││││││   0x004012cc      0fbec0         movsx eax, al
│ │││││││   0x004012cf      01c0           add eax, eax
│ │││││││   0x004012d1      3dca000000     cmp eax, 0xca               ; 202
│ ────────< 0x004012d6      752e           jne 0x401306
│ │││││││   0x004012d8      0fb645f5       movzx eax, byte [var_bh]
│ │││││││   0x004012dc      0fbec0         movsx eax, al
│ │││││││   0x004012df      01c0           add eax, eax
│ │││││││   0x004012e1      83f86a         cmp eax, 0x6a               ; 'j' ; 106
│ ────────< 0x004012e4      7520           jne 0x401306
│ │││││││   0x004012e6      0fb645f6       movzx eax, byte [var_ah]
│ │││││││   0x004012ea      0fbec0         movsx eax, al
│ │││││││   0x004012ed      01c0           add eax, eax
│ │││││││   0x004012ef      3dc2000000     cmp eax, 0xc2               ; 194
│ ────────< 0x004012f4      7510           jne 0x401306
│ │││││││   0x004012f6      0fb645f7       movzx eax, byte [var_9h]
│ │││││││   0x004012fa      0fbec0         movsx eax, al
│ │││││││   0x004012fd      01c0           add eax, eax
│ │││││││   0x004012ff      3dc8000000     cmp eax, 0xc8               ; 200
```
## Part 4 - Byte-By-Byte Comparison - Bit Shifted
* the bytes we need to send in this section are all bit-shifted to the left (multipled)
* to get the correct bytes to send, we need to bit-shift the expected values to the right (divided)
```
│  │ ││││   0x0040135f      c1e003         shl eax, 3
│  │ ││││   0x00401362      3d80010000     cmp eax, 0x180              ; 384
│  │┌─────< 0x00401367      7577           jne 0x4013e0
│  ││││││   0x00401369      0fb645f1       movzx eax, byte [var_fh]
│  ││││││   0x0040136d      0fbec0         movsx eax, al
│  ││││││   0x00401370      c1e003         shl eax, 3
│  ││││││   0x00401373      3d10030000     cmp eax, 0x310              ; 784
│ ┌───────< 0x00401378      7566           jne 0x4013e0
│ │││││││   0x0040137a      0fb645f2       movzx eax, byte [var_eh]
│ │││││││   0x0040137e      0fbec0         movsx eax, al
│ │││││││   0x00401381      c1e003         shl eax, 3
│ │││││││   0x00401384      3d10030000     cmp eax, 0x310              ; 784
│ ────────< 0x00401389      7555           jne 0x4013e0
│ │││││││   0x0040138b      0fb645f3       movzx eax, byte [var_dh]
│ │││││││   0x0040138f      0fbec0         movsx eax, al
│ │││││││   0x00401392      c1e003         shl eax, 3
│ │││││││   0x00401395      3d80010000     cmp eax, 0x180              ; 384
│ ────────< 0x0040139a      7544           jne 0x4013e0
│ │││││││   0x0040139c      0fb645f4       movzx eax, byte [var_ch]
│ │││││││   0x004013a0      0fbec0         movsx eax, al
│ │││││││   0x004013a3      c1e003         shl eax, 3
│ │││││││   0x004013a6      3dc8010000     cmp eax, 0x1c8              ; 456
│ ────────< 0x004013ab      7533           jne 0x4013e0
│ │││││││   0x004013ad      0fb645f5       movzx eax, byte [var_bh]
│ │││││││   0x004013b1      0fbec0         movsx eax, al
│ │││││││   0x004013b4      c1e003         shl eax, 3
│ │││││││   0x004013b7      3da8010000     cmp eax, 0x1a8              ; 424
│ ────────< 0x004013bc      7522           jne 0x4013e0
│ │││││││   0x004013be      0fb645f6       movzx eax, byte [var_ah]
│ │││││││   0x004013c2      0fbec0         movsx eax, al
│ │││││││   0x004013c5      c1e003         shl eax, 3
│ │││││││   0x004013c8      3da0010000     cmp eax, 0x1a0              ; 416
│ ────────< 0x004013cd      7511           jne 0x4013e0
│ │││││││   0x004013cf      0fb645f7       movzx eax, byte [var_9h]
│ │││││││   0x004013d3      0fbec0         movsx eax, al
│ │││││││   0x004013d6      c1e003         shl eax, 3
│ │││││││   0x004013d9      3d30030000     cmp eax, 0x330              ; 816
```
* this Python script will get the correct values and print them out:
```Python
numbers = [384, 784, 784, 384, 456, 424, 416, 816]

shifted_num = []

pass_str = ""

for i in numbers:
  shifted_num.append(i >> 3)

for i in shifted_num:
  pass_str += chr(i)

print(pass_str)
```
## Part 5 - Byte-By-Byte XOR Comparisons
* in this part we are doing an XOR operation byte-by-byte to get the expected values:
```asm
│  ││││││   0x0040143a      31d0           xor eax, edx
│  ││││││   0x0040143c      3c01           cmp al, 1                   ; r14
│ ┌───────< 0x0040143e      7560           jne 0x4014a0
│ │││││││   0x00401440      0fb655f1       movzx edx, byte [var_fh]
│ │││││││   0x00401444      0fb645e1       movzx eax, byte [var_1fh]
│ │││││││   0x00401448      31d0           xor eax, edx
│ │││││││   0x0040144a      3c54           cmp al, 0x54                ; 'T' ; 84
│ ────────< 0x0040144c      7552           jne 0x4014a0
│ │││││││   0x0040144e      0fb655f2       movzx edx, byte [var_eh]
│ │││││││   0x00401452      0fb645e2       movzx eax, byte [var_1eh]
│ │││││││   0x00401456      31d0           xor eax, edx
│ │││││││   0x00401458      3c55           cmp al, 0x55                ; 'U' ; 85
│ ────────< 0x0040145a      7544           jne 0x4014a0
│ │││││││   0x0040145c      0fb655f3       movzx edx, byte [var_dh]
│ │││││││   0x00401460      0fb645e3       movzx eax, byte [var_1dh]
│ │││││││   0x00401464      31d0           xor eax, edx
│ │││││││   0x00401466      3c51           cmp al, 0x51                ; 'Q' ; 81
│ ────────< 0x00401468      7536           jne 0x4014a0
│ │││││││   0x0040146a      0fb655f4       movzx edx, byte [var_ch]
│ │││││││   0x0040146e      0fb645e4       movzx eax, byte [var_1ch]
│ │││││││   0x00401472      31d0           xor eax, edx
│ │││││││   0x00401474      3c09           cmp al, 9                   ; 9
│ ────────< 0x00401476      7528           jne 0x4014a0
│ │││││││   0x00401478      0fb655f5       movzx edx, byte [var_bh]
│ │││││││   0x0040147c      0fb645e5       movzx eax, byte [var_1bh]
│ │││││││   0x00401480      31d0           xor eax, edx
│ │││││││   0x00401482      3c07           cmp al, 7                   ; 7
│ ────────< 0x00401484      751a           jne 0x4014a0
│ │││││││   0x00401486      0fb655f6       movzx edx, byte [var_ah]
│ │││││││   0x0040148a      0fb645e6       movzx eax, byte [var_1ah]
│ │││││││   0x0040148e      31d0           xor eax, edx
│ │││││││   0x00401490      3c57           cmp al, 0x57                ; 'W' ; 87
│ ────────< 0x00401492      750c           jne 0x4014a0
│ │││││││   0x00401494      0fb655f7       movzx edx, byte [var_9h]
│ │││││││   0x00401498      0fb645e7       movzx eax, byte [var_19h]
│ │││││││   0x0040149c      38c2           cmp dl, al
```
* this Python script will do the XOR operation on 7 of the 8 bytes:
```Python
from pwn import xor

# Define our variables for XOR operation
encrypted_bytes = b"0bb0954"

cipher_bytes = [1, 84, 85, 81, 9, 7, 87]

plain_bytes = []

plain_str = ""

# perform the XOR operation, then decode to ASCII characters
for i, j in zip(encrypted_bytes, cipher_bytes):
  plain_bytes.append(xor(i, j).decode())

for i in plain_bytes:
  plain_str += i

print(plain_str)
```
* there's one byte missing
* if we run the code until this point and look in the `rdx` register, we see that the final value is `f`
## Part 6 - Just the Closing Curly Brace
* just like the title says
* done
