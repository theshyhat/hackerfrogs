# URL
https://ringzer0ctf.com/challenges/49
# Concept
* decrypting RSA-encrypted files with a private key
# Method of solve
* we are given a zip file, and after unzipping it, we see two files, an encoded `flag.enc` file, and a `private.pem` file
* these two are meant to be used together, the pem file is used to decrypted the flag file, and we can do that with the following `openssl` command:
```
openssl pkeyutl -decrypt -inkey private.pem -in flag.enc -out flag.txt
```
