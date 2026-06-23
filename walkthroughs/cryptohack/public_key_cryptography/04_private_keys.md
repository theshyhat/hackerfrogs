# URL
https://cryptohack.org/courses/public-key/rsa_starter_4/
# Concept
* RSA private keys
* calculating private key values
# Method of solve
* The private key `d` is used to decrypt ciphertexts created with the corresponding public key
* The private key is the secret piece of information, or "trapdoor", which allows us to quickly invert the encryption function
* If RSA is implemented well, if you do not have the private key the fastest way to decrypt the ciphertext is to factorise the modulus which is very hard to do for large integers
* In RSA, the private key is the modular multiplicative inverse of the exponent `e` modulo `ϕ(N)`, Euler's totient of `N`
  * we can express this as `e` to the power of `-1`, modulo `ϕ(N)`
  * let's do an example where `e = 3` and the value of `N` is `15`, where `p = 3` and `q = 5`
    * we're solving for `x`, where `3x` modulo `8` equals `1`
    * we can start plugging in values for `x`, then multiply by `3`, then divide by `8`, and compare the remainder to `1`
    * we arrive at the conclusion that `x` is `3`, because `(3 * 3) % 8 = 1`
    * which means in our example, `3` is the private key
    * in totality, given that `N` is `15` (p = 3 and q = 5), and the `e` value is `3`:
      * the public key is `N,e`, which in this case is `15,3`
      * the private key is `N,d`, which in this case is `15,3`
* for this challenge, we're asked to calculate the `d` value, given that `p` = `857504083339712752489993810777` and `q` = `1029224947942998075080348647219` and `e` = `65537`
* we can use this Python script:
```Python
def rsa_private_exponent(p, q, e):
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    return d

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
print(rsa_private_exponent(p, q, e))
```



