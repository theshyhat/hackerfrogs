# URL
https://cryptohack.org/courses/public-key/rsa_starter_2/
# Concept
* understanding how RSA public keys are calculated
# Method of solve
* RSA encryption is modular exponentiation of a message with an exponent `e` and a modulus `N` which is normally a product of two primes: `N=p*q`
* Together, the exponent and modulus form an RSA "public key" (N,e). The most common value for `e` is `0x10001` or `6553765537`.
* the challenges us to "encrypt" the number `12` with an `e` value of `65537` and a modulus `N` which is `p=17` multiplied by `q=23`, which is `17 * 23 = 391`
  * so the calculation is `12` (x) to the `65537` power (y) modulo `391` (z)
  * we can use the following Python function to calculate that:
  ```Python
  pow(12,65537,(17*23))
  ```


