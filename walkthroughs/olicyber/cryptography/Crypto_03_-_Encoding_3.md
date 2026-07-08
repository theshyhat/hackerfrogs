# URL
https://training.olicyber.it/challenges#challenge-328
# Concept
* base64 encoding
* large decimal integer to bytes conversion
# Method of solve
* we're asked to decode two objects to get the flag in this challenge:
  * the base64-encoded string `ZmxhZ3t3NDF0XzF0c19hbGxfYjE=`
  * and the large decimal interger `664813035583918006462745898431981286737635929725`
## Python
```
from base64 import b64decode

b64_str = 'ZmxhZ3t3NDF0XzF0c19hbGxfYjE='
big_int = 664813035583918006462745898431981286737635929725

req_bytes = (big_int.bit_length() + 7) // 8

b64_decode = b64decode(b64_str)

int_bytes = big_int.to_bytes(req_bytes,byteorder='big')

print(b64_decode + int_bytes)
```
