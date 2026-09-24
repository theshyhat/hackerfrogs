# username / password
leviathan3 / f0n8h2iWLP
# concept
* finding the right function to follow
* comparing strings for strcmp function
# method of solve
* there is an SUID binary owned by the leviathan4 user called `level3` in the home directory
* when we run the binary, it's looking for a password
* when we try using the ltrace command, it seems like it's comparing some values, but neither of the values is the correct password
* the trick here is that the strcmp in the `dbg.main` function is not the one we're actually looking for
* the main function calls another function, `dbg.do_stuff` which has a strcmp, which is the real one:
```
add esp, 0x10
call dbg.do_stuff           ; level3.c:40
mov eax, 0        
```
* the strcmp in `dbg.do_stuff` is this:
```
lea eax, [var_117h]
push eax
lea eax, [var_10ch]
push eax
call sym.imp.strcmp
```
* so the two locations being compared are the `[var_117h]` and the `[var_10ch]` locations
  * `var_117h` is the password
  * and `var_10ch` is the user input
* if we note the previous instructions in the `dbg.do_stuff` function, we see the bytes of the actual password being loaded into memory:
```
mov dword [var_117h], 0x706c6e73 ; level3.c:10 ; 'snlp'                                         
mov dword [var_113h], 0x746e6972 ; 'rint'
mov dword [var_110h], 0xa6674 ; 'tf\n'
```
* so the password is `snlprintf`

