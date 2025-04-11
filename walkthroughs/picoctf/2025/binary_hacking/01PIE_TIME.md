> When we run this program, it allows us to redirect the binary's execution to a specific memory address. This program has PIE enabled. We can confirm this with the rabin2 tool

```
rabin2 -I vuln
```

> We can then inspect the disassembly in R2

```
r2 -d vuln
aaa
afl
```

> We see that the sym.win and the main functions are located next to each to each other. We can use Python to find out where the addresses are in relation to each other

```
python3 -c "print(hex(0x5574350ce33d - 0x5574350ce2a7))"
```

> We find that the difference in addresses is 0x96. That means that we should be able to subtract 0x96 from the address reported by the binary when its run to discover the address of the sym.win function and run it. We can do that with Python.

```
python3 -c "print(hex(<main_hex_address> - 0x96))"
```

We feed this address to the binary when its run, and we win!

Finis
