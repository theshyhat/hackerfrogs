# URL
https://hackropole.fr/en/challenges/crypto/fcsc2020-crypto-smic-2/
# Concept
* RSA cryptosystem - simulation of decryption
# Method of solve
* we're given these values:
```
e = 65537
n = 632459103267572196107100983820469021721602147490918660274601
c = 63775417045544543594281416329767355155835033510382720735973
```
* in the absence of a public key, we may be able to decrypt the ciphertext if we can factorize the `n` value
* we're able to factorize it using the `factordb.com`, and obtain the `p` and `q` values used to create the `n` value
```Python
e = 65537
c = 63775417045544543594281416329767355155835033510382720735973
n = 632459103267572196107100983820469021721602147490918660274601
p = 650655447295098801102272374367
q = 972033825117160941379425504503
phi = (p-1) * (q-1)

d = pow(e,-1,phi)

m = pow(c,d,n)

print(m)
```
