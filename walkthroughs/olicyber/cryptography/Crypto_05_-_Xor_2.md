# URL
https://training.olicyber.it/challenges#challenge-330
# Concept
* XOR
* XOR brute force by bytes
# Method of solve
* the challenge gives us a ciphertext string along with an instruction to brute force the ciphertext with bytes
* in this case we supply a single byte as the key to bruteforce the XOR ciphertext
```
import binascii

# Ciphertext string
ciphertext = '104e137f425954137f74107f525511457f5468134d7f146c4c'

string = binascii.unhexlify(ciphertext)

l = [c for c in string]

for i in range(256):
     f = [chr(n^i) for n in l]
     a = "".join(f)
     print(f"Byte: {i} Message: {a}")
```
