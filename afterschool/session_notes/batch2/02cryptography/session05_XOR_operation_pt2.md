# HackerFrogs AfterSchool Cryptography Session 5
## Session Topic: XOR Operations Pt 2 /w CryptoHack and PicoCTF
# Challenge 1: ctfLearn Hextraordinary
## ctfLearn Link
https://ctflearn.com/challenge/158
### YouTube Walkthrough Link
https://youtu.be/Q2xp-f31_Sk?t=884
### Method of Solve
* Step 1: use the following command in the webshell terminal to start editing a file named `hextraordinary.py`:
```
hex1 = 0xc4115
hex2 = 0x4cf8

one_xor_two = hex1 ^ hex2
results_hex = hex(one_xor_two)

print("The flag to submit is CTFlearn{" + str(results_hex) + "}")
```
* Step 2: paste the following Python code into the text editor:
```
```
* Step 3: Save the file by typing in `ctrl + x`, then `y`, then hit the enter key to confirm the filename.
* Step 4: Use the following command to run the Python script:
```
python vigenere.py
```
* Step 5: Copy the flag, which starts with `picoCTF`, and ends with `}`
* Step 6: on the PicoCTF challenge page, submit the flag
#### METHOD 2 (Using Websites)
* Step 1: Copy the file link on the PicoCTF challenge page
* Step 2: in the webshell, use the following command to download the ciphertext file:
```
wget <file_address_here>
```
Replace `<file_address_here>` with the address you copied from the challenge page
* Step 3: Read the file with the following command:
```
cat cipher.txt
```
* Step 4: Copy the output
* Step 5: Access the following website `https://cryptii.com/pipes/vigenere-cipher`
* Step 6: On the `cryptii` website, paste the ciphertext string into the `Ciphertext` field
* Step 7: In the `KEY` field in the type in the key from the challenge page `cylab`
Observe that the decrypted flag appears in the `Plaintext` field on the webpage
* Step 8: Copy the flag from the `Plaintext` field. From `picoCTF` until `}`
* Step 9: On the PicoCTF challenge page, submit the flag
# Challenge 2: CryptHack You Either Know It XOR You Don't
## CryptHack Link
https://cryptohack.org/courses/intro/xorkey1/
## YouTube Walkthrough Link
https://www.youtube.com/watch?v=D8sXCtu4oys
### Method of solve
#### METHOD 1 (Python)
* Step 1: use the following command in the webshell terminal to start editing a file named `know_xor_dont.py`:
```
nano know_xor_dont.py
```
* Step 2: Copy and paste the following code into the nano editor:
```
from pwn import xor

encrypted_bytes = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
key_bytes = b"crypto{"

print(xor(encrypted_bytes, key_bytes).decode())
```
* Step 3: Save the file by typing in `ctrl + x`, then `y`, then hit the enter key to confirm the filename.
* Step 4: Use the following command to run the Python script:
```
python know_xor_dont.py
```
Note that in the output, it looks like there's something like `myXORkey`
* Step 5: Go back into the Python script with the `nano` text editor, and replace the current value of `key_bytes` with `myXORkey`
* Step 6: Run the Python script again
* Step 7: Copy the flag, which starts with `crypto`, and ends with `}`
* Step 8: Submit the flag `crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}`
# Challenge 3: PicoCTF Rail Fence
## PicoCTF Link
https://play.picoctf.org/practice/challenge/289
## YouTube Walkthrough Link
https://youtu.be/k0b6NBDcfTk?t=3393
### Method of solve
#### METHOD 1 (Python)
* Step 1: use the following command in the webshell terminal to start editing a file named `rail-fence.py`:
```
nano rail-fence.py
```
* Step 2: Copy and paste the following code into the nano editor:
```
```
* Step 3: Save the file by typing in `ctrl + x`, then `y`, then hit the enter key to confirm the filename.
* Step 4: Use the following command to run the Python script:
```
python rail-fence.py
```
* Step 5: Copy the flag, which starts with `picoCTF`, and ends with `}`
* Step 6: on the PicoCTF challenge page, submit the flag
