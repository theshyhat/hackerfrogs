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

# Convert the hex string to bytes
bytes = binascii.unhexlify(ciphertext)

# Turn the string variable into a list containing each character in the string as list contents
list_of_bytes = [element for element in bytes]

# Run through all possible bytes (0-255) and print the result of XOR between that byte and the list of bytes in the 
for num in range(256):
     XOR_loop = [chr(element^num) for element in list_of_bytes]
     message = "".join(XOR_loop)
     print(f"Byte: {num} Message: {message}")
```
