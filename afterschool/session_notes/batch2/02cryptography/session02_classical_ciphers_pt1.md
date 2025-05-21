# HackerFrogs AfterSchool Cryptography Session 2
## Session Topic: Classical Cryptographic Ciphers Pt 1 /w PicoCTF
# Challenge 1: PicoCTF 13
## PicoCTF Link
https://play.picoctf.org/practice/challenge/62
### YouTube Walkthrough Link
https://youtu.be/f3LwYjpEUjI?t=1801
### Method of Solve
#### METHOD 1 (Using Linux)
* Step 1: copy the ciphertext string `cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}`
* Step 2: use the following command in the webshell terminal to decrypt the ciphertext string:
```
echo 'cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}' | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```
* Step 3: on the PicoCTF challenge page, submit the flag `picoCTF{not_too_bad_of_a_problem}`
#### METHOD 2 (Using Websites)
* Step 1: copy the ciphertext string `cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}`
* Step 2: access the following website `https://rot13.com/`
* Step 3: on the rot13 website, paste the ciphertext string into the first field
* Step 4: copy the decrypted plaintext string from the second field on the webpage
* Step 5: on the PicoCTF challenge page, submit the flag `picoCTF{not_too_bad_of_a_problem}`
# Challenge 2: PicoCTF Rotation
## PicoCTF Link
https://play.picoctf.org/practice/challenge/373
## YouTube Walkthrough Link
https://youtu.be/f3LwYjpEUjI?t=2430
### Method of solve
* Step 1: Use the following command in the webshell terminal to download the file with the ciphertext:
```
wget https://artifacts.picoctf.net/c/390/encrypted.txt
```
* Step 2: Read the ciphertext file:
```
cat encrypted.txt
```
* Step 3: Copy the ciphertext
* Step 4: in a web browser, navigate to the following website: `https://cryptii.com/pipes/caesar-cipher`
* Step 5: Paste in the ciphertext on the left-hand side field
* Step 6: Click on the `+` button on the page until the shift number is `18`, then copy the decrypted string on the right-hand side field
* Step 7: Submit `picoCTF{r0tat1on_d3crypt3d_429af00f}` as the flag
