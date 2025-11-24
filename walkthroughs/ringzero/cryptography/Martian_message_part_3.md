# URL
https://ringzer0ctf.com/challenges/26
# Concept
* base64 encoding
* XOR byte brute-forcing
# Method of solve
* we are given a ciphertext string
* there are two layers of transformation on this string
* the first layer is a base64 encoding
* when we base64 decode the ciphertext, the resulting string is XOR encoded
* we can use an XOR brute force between the ciphertext and all possible bytes from 0 to 255 and get an answer
* we can use this code
```
from pwn import xor

# Convert the ascii string to bytes
data = b"EOBD.7igq4;1ikb51ibOO0;:41R"

# Brute-force single-byte XOR
for key in range(256):  # Possible values for a single byte (0x00 to 0xFF)
    result = xor(data, key)
    try:
        # Attempt to decode the result as an ASCII string
        decoded = result.decode()
        if all(32 <= ord(c) <= 126 for c in decoded):  # Check for printable characters
            print(f"Key: {key}, Message: {decoded}")
    except UnicodeDecodeError:
        # Ignore decoding errors for non-ASCII results
        continue
```
