# URL
https://hack.arrrg.de/challenge/340
# Catgory
General
# Concept
* base8 counting versus base10 counting
# Method of solve
* the challenge wants us to convert an octal number to a decimal number
* the octal number is `2471`
* we can use a web to convert this number `https://www.rapidtables.com/convert/number/octal-to-decimal.html`
* we can also use this Bash command:
```
echo $((8#2471))
```
* we can also do manual conversion
```
When doing conversion from any base number to decimal:
* the first digit represents the number itself
* the second digit represents the base to the 1st power (8)
* the third digit represents the base to the 2nd power (8 x 8 = 64)
* the fourth digit represents the base to the 3rd power (8 x 8 x 8 = 512)
```
* we multiply the digits `2471` by differing powers of 8, then add them all together
* so the first digit is 1
* the second digit is 7 x 8 = 56
* the third digit is 4 x 64 = 256
* the fourth digit is 2 x 512 = 1024
* all put together: `1024 + 256 + 56 + 1 = 1337`
