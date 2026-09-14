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
