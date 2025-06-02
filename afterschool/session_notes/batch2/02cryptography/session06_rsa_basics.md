# HackerFrogs AfterSchool Cryptography Session 6
## Session Topic:  RSA Basics /w PicoCTF
# Challenge 1: PicoCTF Mini RSA
## PicoCTF Link
https://play.picoctf.org/practice/challenge/73
### YouTube Walkthrough Link
https://youtu.be/c9reYR6lCAg?t=1308
### Method of Solve
* Step 1: use the following command in the webshell terminal to start editing a file named `mini_rsa.py`:
```
nano mini_rsa.py
```
* Step 2: paste the following Python code into the text editor:
```
from sympy import integer_nthroot

# Given values
N = 29331922499794985782735976045591164936683059380558950386560160105740343201513369939006307531165922708949619162698623675349030430859547825708994708321803705309459438099340427770580064400911431856656901982789948285309956111848686906152664473350940486507451771223435835260168971210087470894448460745593956840586530527915802541450092946574694809584880896601317519794442862977471129319781313161842056501715040555964011899589002863730868679527184420789010551475067862907739054966183120621407246398518098981106431219207697870293412176440482900183550467375190239898455201170831410460483829448603477361305838743852756938687673
e = 3
c = 2205316413931134031074603746928247799030155221252519872650080519263755075355825243327515211479747536697517688468095325517209911688684309894900992899707504087647575997847717180766377832435022794675332132906451858990782325436498952049751141

# Compute the cube root of c
m, is_perfect_cube = integer_nthroot(c, e)

if is_perfect_cube:
    print("Decrypted plaintext (m):", m)

    byte_length = (m.bit_length() + 7) // 8
    m_bytes = m.to_bytes(byte_length, byteorder='big')
    
    # Decode the bytes to a string (assuming UTF-8 encoding)
    try:
        plaintext = m_bytes.decode('utf-8')
        print("Decrypted text:", plaintext)
    except UnicodeDecodeError:
        print("Failed to decode the bytes as UTF-8. The plaintext may use a different encoding or contain non-text data.")
else:
    print("The ciphertext is not a perfect cube. Further analysis is needed.")
```
* Step 3: Save the file by typing in `ctrl + x`, then `y`, then hit the enter key to confirm the filename.
* Step 4: Use the following command to run the Python script:
```
python rsa_mini.py
```
* Step 5: Copy the flag, which starts with `picoCTF`, and ends with `}`
* Step 6: on the PicoCTF challenge page, submit the flag `picoCTF{n33d_a_lArg3r_e_d0cd6eae}`
# Encrypting using RSA in Linux
```

```
