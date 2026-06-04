# URL
https://hackropole.fr/en/challenges/crypto/fcsc2025-crypto-carotte-radis-tomate/
# Concept
* deriving an AES key using inverse modulo (CRT theorum)
# Method of solve
* we download both of the files
* this is the content of the Python script:
```Python
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = os.urandom(32)
print("carotte = ", int.from_bytes(key) % 17488856370348678479)
print("radis   = ", int.from_bytes(key) % 16548497022403653709)
print("tomate  = ", int.from_bytes(key) % 17646308379662286151)
print("pomme   = ", int.from_bytes(key) % 14933475126425703583)
print("banane  = ", int.from_bytes(key) % 17256641469715966189)

flag = open("flag.txt", "rb").read()
E = AES.new(key, AES.MODE_ECB)
enc = E.encrypt(pad(flag, 16))
print(f"enc = {enc.hex()}")
```
* we know the method of encryption was AES in ECB mode
* we have the output of the script in the output.txt file:
```
carotte =  392278890668246705
radis   =  4588810924820033807
tomate  =  17164682861166542664
pomme   =  12928514648456294931
banane  =  5973470563196845286
enc = 2da1dbe8c3a739d9c4a0dc29a27377fe8abc1c0feacc9475019c5954bbbf74dcedce7ed3dc3ba34fa14a9181d4d7ec0133ca96012b0a9f4aa93c42c61acbeae7640dd101a6d2db9ad4f3b8ccfe285e0d
```
* if we know the outputs, then we can start to reconstruct the key based on the outputs from the 5 fruits and vegetable variables
* we need to get the modular inverse of the output results, using the Chinese Remainder Theorum, and this script is able to do that:
```Python
from sympy.ntheory.modular import crt

# Modulos
mods = [
    17488856370348678479,
    16548497022403653709,
    17646308379662286151,
    14933475126425703583,
    17256641469715966189
]

# Residues (your output values)
residues = [
    392278890668246705,
    4588810924820033807,
    17164682861166542664,
    12928514648456294931,
    5973470563196845286
]

# Reconstruct the key integer using CRT
k, N = crt(mods, residues)

# Convert to 32 bytes (big-endian)
key = int(k).to_bytes(32, byteorder='big')

print("Recovered key (hex):", key.hex())
print("Recovered key (bytes):", key)
```
This gives the key in hexadecimal format, which we feed into CyberChef to decrypt the flag:
```
https://cyberchef.io/#recipe=AES_Decrypt(%7B'option':'Hex','string':'816b392538ae5895093e0a8094a2b858a1c2bdc16587ebfbd80fd50f7e19204d'%7D,%7B'option':'Hex','string':'0000000000000000'%7D,'ECB','Hex','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)&input=MmRhMWRiZThjM2E3MzlkOWM0YTBkYzI5YTI3Mzc3ZmU4YWJjMWMwZmVhY2M5NDc1MDE5YzU5NTRiYmJmNzRkY2VkY2U3ZWQzZGMzYmEzNGZhMTRhOTE4MWQ0ZDdlYzAxMzNjYTk2MDEyYjBhOWY0YWE5M2M0MmM2MWFjYmVhZTc2NDBkZDEwMWE2ZDJkYjlhZDRmM2I4Y2NmZTI4NWUwZA
```

