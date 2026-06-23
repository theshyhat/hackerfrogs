# URL
https://cryptohack.org/courses/public-key/rsa_starter_1/
# Concept
* understanding modular exponentiation
# Method of solve
* this challenge is all about understanding how to perform a modular exponentiation operation
* that is, raising a base number (x) to a specific power / exponent (y), then returning the modulus of the a third number (z)
* so the formula is `x` to the power of `y`, then modulo`z`
* this operation can be done very easily in Python using the `pow` function
```
pow(x,y,z)
```
* for example
```
pow(2, 10, 17) # should return 4
```
* to solve the challenge, submit the number returned when we run this operation
```
101 raised to the power of 17, modulo 22663
```
* this Python function will return the correct number:
```
pow(101, 17, 22663)
```





