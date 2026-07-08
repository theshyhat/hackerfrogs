# URL
https://training.olicyber.it/challenges#challenge-328
# Concept
* base64 encoding
* large decimal integer to bytes conversion
# Method of solve
* we're asked to decode two objects to get the flag in this challenge:
  * the base64-encoded string `ZmxhZ3t3NDF0XzF0c19hbGxfYjE=`
  * and the large decimal interger `664813035583918006462745898431981286737635929725`
## CyberChef
### Part 1
* In the `Input` window, paste the base64 string
* Apply the `To Base64` operation, by searching it in the `Operations` search bar, then drag it into the `Recipe` window
* the flag for the challenge can be found in the `Output` window
### Part 2
* In the `Input` window, paste the large decimal number
* Apply the `To Base` operation, by searching it in the `Operations` search bar, then drag it into the `Recipe` window
* In the `To Base` operation, adjust the `Radix` value, setting it to `16`
* Apply the `From Hex` operation, by searching it in the `Operations` search bar, then drag it into the `Recipe` window, below the `To Base` operation
* the flag for the challenge can be found in the `Output` window
## Linux
### Part 1
```Bash
echo 'ZmxhZ3t3NDF0XzF0c19hbGxfYjE=' | base64 -d
```
### Part 2
```Bash
echo "obase=16; 664813035583918006462745898431981286737635929725" | bc | xxd -r -p
```
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
