# URL
https://hack.arrrg.de/challenge/310
# Category
Cryptography
# Concept
* cracking sha256 hashes (password hashes)
* cracking salted hashes
# Method of solve
* there's JavaScript code on the challenge webpage which indicateds a sha256 hash, and a salt
* the hash `9bcf0c8289a97d33021b4790659396d9f8af1085210d2186b8ec38efcdc31472`
* the salt `3NL/usjb4vEg`
* we can combine the hash and the salt by concatenating them together in the format `hash:salt`
* so the complete salted hash string looks like this:
```
9bcf0c8289a97d33021b4790659396d9f8af1085210d2186b8ec38efcdc31472:3NL/usjb4vEg
```
* We can feed this hash in a file to the Hashcat program
```
hashcat -m1420 ./hash /usr/share/wordlists/rockyou.txt
```
* we are using the famous `rockyou.txt` wordlist for cracking
* the answer is `idontknow`
