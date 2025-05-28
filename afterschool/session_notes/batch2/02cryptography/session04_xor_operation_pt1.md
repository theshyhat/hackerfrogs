# HackerFrogs AfterSchool Cryptography Session 4
## Session Topic: XOR Operations Pt 1 /w Cryptohack
# Challenge 1: CryHack XOR Starter
## Cryptohack Link
https://cryptohack.org/courses/intro/xor0/
### YouTube Walkthrough Link
https://www.youtube.com/watch?v=fAJC02o9j70
### Method of Solve
* Step 1: copy the code for the Python file. We've provided the code below for convenience:
```
def XOR(var1,var2):
    return bytes(a^var2 for a in var1)
    
encrypted_bytes = b"label"

key_integer = 13

xor_result = XOR(encrypted_bytes, key_integer).decode()

print(xor_result)
```
* Step 2: Access the following website to run the Python code: `https://www.online-python.com/`
* Step 3: Delete the code already in the editor window on the website, then paste in the Python code referenced in Step 1
* Step 4: Click on the `Run` button below the editor
* Step 5: Submit `crypto{aloha}` as the flag
# Challenge 2: XOR Properties
## Cryptohack Link
https://cryptohack.org/courses/intro/xor1/
## YouTube Walkthrough Link
https://www.youtube.com/watch?v=K09Z6wT-HK0&t
### Method of solve
* Step 1: Copy the code for the Python file. We've provided the code below for convenience:
```
def XOR(var1,var2):
    return bytes(a^b for a,b in zip(var1, var2))
    
# hex values converted to bytes
key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key2_xor_key1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
key2_xor_key3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
flag_xor_keys = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

# computing key2
key2 = XOR(key1, key2_xor_key1)
# computing key3
key3 = XOR(key2, key2_xor_key3)
# computing flag
flag = XOR(XOR(XOR(key1, key2), key3), flag_xor_keys)
# print it out 
print(flag.decode())
```
* Step 2: Access the following website to run the Python code: `https://www.online-python.com/`
* Step 3: Delete the code already in the editor window on the website, then paste in the Python code referenced in Step 1
* Step 4: Click on the `Run` button below the editor
* Step 5: Submit `crypto{x0r_i5_ass0c1at1v3}` as the flag
# Challenge 3: CryHack Favourite Byte
## Cryptohack Link
https://cryptohack.org/courses/intro/xorkey0/
## YouTube Walkthrough Link
https://www.youtube.com/watch?v=QwxOqnHYJfQ
### Method of solve
* Step 1: Copy the list of numbers, including the square brackets
* Step 2: Navigate to the online-python website, delete the code in the editor window, then replace it with the following code:
```
import binascii

string = binascii.unhexlify("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
l = [c for c in string]
for i in range(256):
     f = [chr(n^i) for n in l]
     a = "".join(f)
     print(f"Byte: {i} Message: {a}")
```
* Step 3: click on the `Run` button below the editor
* Step 4: submit `crypto{0x10_15_my_f4v0ur173_by7e}` as the flag
