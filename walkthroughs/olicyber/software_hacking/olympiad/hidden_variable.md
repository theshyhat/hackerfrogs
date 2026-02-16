# URL
https://training.olicyber.it/challenges#challenge-96
# Concept
* reverse engineering
* Unicode escape encoding
* UTF32LE Encoding
# Method of solve
* after downloading the binary and making it executable we run the binary, but it doesn't give us much
* running `strings` on the binary doesn't show us anything special either
* if we look at the binary in the Radare2 decompiler, we can see there's an additional string in the binary:
```
r2 -d hidden_variable
aaa
izz | less
```
* we see there's a `utf32le` string in the binary, which is the flag
* `utf-32` is a fixed-width encoding, which is related to `utf-8`
* we actually can use the `strings` command to look for `utf-32` strings in binaries, but we need to use some different arguments:
```
strings -e L <file_name>
```
* if we wanted to create our own binary that behaves like the one in the challenge, we can use this code:
```
#include <stdio.h>
#include <wchar.h>

wchar_t real_flag[] = L"flag{this_is_the_flag}";

int main(int argc, char **argv) {
    puts("The flag is \\u00e8 f_ag{.\\u0142\\u20ac\\u201c\\u00df#[");
    puts("The flag got corrupted! Where is\\u00f2 the original?");
    return 0;
}
```
* the `wchar_t` data type in C is used with wide characters in the `UTF32` and `UTF16` encoding schemes
