# HackerFrogs AfterSchool Cryptography Session 1
## Session Topic: Encoding Systems /w Cryptohack
# Challenge 1: CryHack Finding Flags
## Cryptohack Link
https://cryptohack.org/courses/intro/fflags/
### YouTube Walkthrough Link
https://youtu.be/7P80uQLCc10?t=1217
### Method of Solve
* Step 1: copy the flag value `crypto{y0ur_f1rst_fl4g}`
* Step 2: paste the flag value and click on the `SUBMIT` button
# Challenge 2: CryHack Great Snakes
## Cryptohack Link
https://cryptohack.org/courses/intro/nc-intro/
## YouTube Walkthrough Link
https://youtu.be/7P80uQLCc10?t=1291
### Method of solve
* Step 1: Copy the code for the Python file. We've provided the code below for convenience:
```
#!/usr/bin/env python3

import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("Here is your flag:")
print("".join(chr(o ^ 0x32) for o in ords))
```
* Step 2: Access the following website to run the Pytho code: `https://www.online-python.com/`
* Step 3: Delete the code already in the editor window on the website, then paste in the Python code referenced in Step 1
* Step 4: Click on the `Run` button below the editor
* Step 5: Submit `crypto{z3n_0f_pyth0n}` as the flag
# Challenge 3: CryHack ASCII
## Cryptohack Link
https://cryptohack.org/courses/intro/enc1/
## YouTube Walkthrough Link
https://youtu.be/7P80uQLCc10?t=1655
### Method of solve
* Step 1: Copy the list of numbers, including the square brackets
* Step 2: Navigate to the online-python website, delete the code in the editor window, then replace it with the following code:
```
ascii_list = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
for i in ascii_list:
    print(chr(i), end="")
```
* Step 3: click on the `Run` button below the editor
* Step 4: submit `crypto{ASCII_pr1nt4bl3}` as the flag
# Challenge 4: CryHack Hex
## Cryptohack Link
https://cryptohack.org/courses/intro/enc2/
## YouTube Walkthrough Link
https://youtu.be/7P80uQLCc10?t=2435
### Method of solve
* Step 1: Copy the hexadecimal string
* Step 2: Navigate to the online-python website, delete the code in the editor window, then replace it with the following code:
```
hex_number = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
hex_bytes = bytes.fromhex(hex_number)
print(hex_bytes)
```
* Step 3: click on the `Run` button below the editor
* Step 4: submit `crypto{You_will_be_working_with_hex_strings_a_lot}` as the flag
# Challenge 5: CryHack Base64
## Cryptohack Link
https://cryptohack.org/courses/intro/enc3/
## YouTube Walkthrough Link
https://youtu.be/7P80uQLCc10?t=3093
### Method of solve
* Step 1: Copy the hexadecimal string
* Step 2: Navigate to the online-python website, delete the code in the editor window, then replace it with the following code:
```
import base64

hex_string = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
hex_bytes = bytes.fromhex(hex_string)
base64_decoded = base64.b64encode(hex_bytes)
print(base64_decoded)
```
* Step 3: click on the `Run` button below the editor
* Step 4: submit `crypto/Base+64+Encoding+is+Web+Safe/` as the flag
