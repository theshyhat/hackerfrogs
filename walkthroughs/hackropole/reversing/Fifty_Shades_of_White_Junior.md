# URL
https://hackropole.fr/en/challenges/reverse/fcsc2024-reverse-fifty-shades-of-white-1/
# Concept
* understanding how program execution and conditions work
## Lessons Learned
* look carefully at how functions pass data to each other
# Method of solve
* the first thing we note is that the license file has base64-encoded data in it
* when we decode the license body, we see this:
```
Name: Walter White Junior
Serial: 1d117c5a-297d-4ce6-9186-d4b84fb7f230
Type: 1
```
* this means we could modify this data, then base64 encode it to spoof an admin license key
* when we examine the program in Ghidra, we see there's a comparison made before the `showFlag()` function is run
```C
  else if (*(int *)(outputFromParse + 2) == 1) {
    printf("Valid license for %s!\n",*outputFromParse);
  }
  else if (*(int *)(outputFromParse + 2) == 0x539) {
    printf("Valid admin license for %s!\n",*outputFromParse);
    show_flag();
  }
```
* this tells us that there is one path if the value is `1`, and another if the value is `0x539`, which in decimal is `1337`
* since we know there is a value in the default license key which has the value `1`, the `Type` value, we suspect that this is what we need to modify
* we craft a license key file with the following contents:
```
----BEGIN WHITE LICENSE----
TmFtZTogV2FsdGVyIFdoaXRlIEp1bmlvcgpTZXJpYWw6IDFkMTE3YzVhLTI5N2QtNGNlNi05MTg2LWQ0Yjg0ZmI3ZjIzMApUeXBlOiAxMzM3Cg==
-----END WHITE LICENSE-----
```
* and that gets us the key
