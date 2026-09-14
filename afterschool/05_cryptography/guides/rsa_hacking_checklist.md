# WORK IN PROGRESS
# RSA Security Flaws Checklist
## E value is small
### If E is 1
* the encryption doesn't do anything to the ciphertext if the E value is one
* the ciphertext and the plaintext will be the same
### If E is 3
* if E is 3 and:
  * the ciphertext is significantly smaller than N ((`ct` ** 3) < `n`)
  * there is no padding involved
* then the ciphertext will be vulnerable to a `cube root attack`
## If the P and Q Values are Known
## If N is Monoprime
## If N is Multiprime
## If N is Comprised of Close Primes P and Q


