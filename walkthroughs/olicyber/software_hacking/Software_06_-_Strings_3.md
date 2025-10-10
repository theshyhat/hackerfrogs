# URL
https://training.olicyber.it/challenges#challenge-260
# Concept
* even more strings
* XOR encryption
# Method of solve
* inspect the binary using Radare2
```
r2 -d ./sw-06
```
* from there, 
```
│           0x00001205      55             push rbp
│           0x00001206      4889e5         mov rbp, rsp
│           0x00001209      4881ec2001..   sub rsp, 0x120
│           0x00001210      64488b0425..   mov rax, qword fs:[0x28]
│           0x00001219      488945f8       mov qword [canary], rax
│           0x0000121d      31c0           xor eax, eax
│           0x0000121f      488d85f0fe..   lea rax, [s1]
│           0x00001226      ba00010000     mov edx, 0x100              ; size_t n
│           0x0000122b      be00000000     mov esi, 0                  ; int c
│           0x00001230      4889c7         mov rdi, rax                ; void *s
│           0x00001233      e838feffff     call sym.imp.memset         ; void *memset(void *s, int c, size_t n)
│           ; CODE XREF from main @ 0x134c(x)
│       ┌─> 0x00001238      488d3de70d..   lea rdi, str._Qual_la_flag__: ; 0x2026 ; const char *format
│       ╎   0x0000123f      b800000000     mov eax, 0
│       ╎   0x00001244      e817feffff     call sym.imp.printf         ; int printf(const char *format)
│       ╎   0x00001249      488b15102e..   mov rdx, qword [obj.stdin]  ; obj.stdin__GLIBC_2.2.5
│       ╎                                                              ; [0x4060:8]=0 ; FILE *stream                                                                   
│       ╎   0x00001250      488d85f0fe..   lea rax, [s1]
│       ╎   0x00001257      be00010000     mov esi, 0x100              ; int size
│       ╎   0x0000125c      4889c7         mov rdi, rax                ; char *s
│       ╎   0x0000125f      e81cfeffff     call sym.imp.fgets          ; char *fgets(char *s, int size, FILE *stream)                                                                                                                                                                 
│       ╎   0x00001264      488d85f0fe..   lea rax, [s1]
│       ╎   0x0000126b      4889c7         mov rdi, rax                ; const char *s
│       ╎   0x0000126e      e8cdfdffff     call sym.imp.strlen         ; size_t strlen(const char *s)
│       ╎   0x00001273      488985e0fe..   mov qword [var_120h], rax
│       ╎   0x0000127a      4883bde0fe..   cmp qword [var_120h], 0
│      ┌──< 0x00001282      0f84b8000000   je 0x1340
│      │╎   0x00001288      488b85e0fe..   mov rax, qword [var_120h]
│      │╎   0x0000128f      4883e801       sub rax, 1
│      │╎   0x00001293      0fb68405f0..   movzx eax, byte [rbp + rax - 0x110]
│      │╎   0x0000129b      3c0a           cmp al, 0xa
│     ┌───< 0x0000129d      751c           jne 0x12bb
│     ││╎   0x0000129f      4883ade0fe..   sub qword [var_120h], 1
│     ││╎   0x000012a7      488d95f0fe..   lea rdx, [s1]
│     ││╎   0x000012ae      488b85e0fe..   mov rax, qword [var_120h]
│     ││╎   0x000012b5      4801d0         add rax, rdx
│     ││╎   0x000012b8      c60000         mov byte [rax], 0
│     ││╎   ; CODE XREF from main @ 0x129d(x)
│     └───> 0x000012bb      4883bde0fe..   cmp qword [var_120h], 0xe
│     ┌───< 0x000012c3      757b           jne 0x1340
│     ││╎   0x000012c5      48c785e8fe..   mov qword [var_118h], 0
│    ┌────< 0x000012d0      eb45           jmp 0x1317
│    │││╎   ; CODE XREF from main @ 0x131f(x)
│   ┌─────> 0x000012d2      488d95f0fe..   lea rdx, [s1]
│   ╎│││╎   0x000012d9      488b85e8fe..   mov rax, qword [var_118h]
│   ╎│││╎   0x000012e0      4801d0         add rax, rdx
│   ╎│││╎   0x000012e3      0fb610         movzx edx, byte [rax]
│   ╎│││╎   0x000012e6      488d0d2b0d..   lea rcx, obj.key            ; 0x2018
│   ╎│││╎   0x000012ed      488b85e8fe..   mov rax, qword [var_118h]
│   ╎│││╎   0x000012f4      4801c8         add rax, rcx
│   ╎│││╎   0x000012f7      0fb600         movzx eax, byte [rax]
│   ╎│││╎   0x000012fa      31c2           xor edx, eax
│   ╎│││╎   0x000012fc      488d8df0fe..   lea rcx, [s1]
│   ╎│││╎   0x00001303      488b85e8fe..   mov rax, qword [var_118h]
│   ╎│││╎   0x0000130a      4801c8         add rax, rcx
│   ╎│││╎   0x0000130d      8810           mov byte [rax], dl
│   ╎│││╎   0x0000130f      488385e8fe..   add qword [var_118h], 1
│   ╎│││╎   ; CODE XREF from main @ 0x12d0(x)
│   ╎└────> 0x00001317      4883bde8fe..   cmp qword [var_118h], 0xd
│   └─────< 0x0000131f      76b1           jbe 0x12d2
│     ││╎   0x00001321      488d85f0fe..   lea rax, [s1]
│     ││╎   0x00001328      ba0e000000     mov edx, 0xe                ; size_t n
│     ││╎   0x0000132d      488d35d40c..   lea rsi, obj.flag           ; 0x2008 ; const void *s2
│     ││╎   0x00001334      4889c7         mov rdi, rax                ; const void *s1
│     ││╎   0x00001337      e849feffff     call sym.memcmp             ; int memcmp(const void *s1, const void *s2, size_t n)                                                                                                 
│     ││╎   0x0000133c      85c0           test eax, eax
│    ┌────< 0x0000133e      7411           je 0x1351
│    │││╎   ; CODE XREFS from main @ 0x1282(x), 0x12c3(x)
│    │└└──> 0x00001340      488d3df80c..   lea rdi, str._Sbagliato__Prova_ancora ; 0x203f ; const char *s
│    │  ╎   0x00001347      e8e4fcffff     call sym.imp.puts           ; int puts(const char *s)
│    │  └─< 0x0000134c      e9e7feffff     jmp 0x1238
│    │      ; CODE XREF from main @ 0x133e(x)
│    └────> 0x00001351      90             nop
│           0x00001352      488d3d020d..   lea rdi, str._Giusto_       ; 0x205b ; const char *s
│           0x00001359      e8d2fcffff     call sym.imp.puts           ; int puts(const char *s)
│           0x0000135e      b800000000     mov eax, 0
│           0x00001363      488b75f8       mov rsi, qword [canary]
│           0x00001367      64482b3425..   sub rsi, qword fs:[0x28]
│       ┌─< 0x00001370      7405           je 0x1377
│       │   0x00001372      e8d9fcffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
│       │   ; CODE XREF from main @ 0x1370(x)
│       └─> 0x00001377      c9             leave
└           0x00001378      c3             ret

```
