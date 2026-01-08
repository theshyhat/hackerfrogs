# URL
https://hack.arrrg.de/challenge/315
# Category
Cryptography
# Concept
* cracking sha256 hashes (password hashes)
* cracking salted hashes
* using a custom wordlist
# Method of solve
* there's JavaScript code on the challenge webpage which indicateds a sha256 hash, and a salt
* the hash `47fde76c898053a9db963df844bb936c26ab54867663f4d1505858d6c346eacc`
* the salt `3NL/usjb4vEg`
* we can combine the hash and the salt by concatenating them together in the format `hash:salt`
* so the complete salted hash string looks like this:
```
47fde76c898053a9db963df844bb936c26ab54867663f4d1505858d6c346eacc:3NL/usjb4vEg
```
* we are provided with user information in this challenge that can be used to create a custom word list
* we can use the `CUPP` custom word generating tool to achieve this
`https://github.com/Mebus/cupp`
* after generating the wordlist, we can use it with `Hashcat`
* We can feed this hash in a file to the Hashcat program
```
hashcat -m1420 ./mentalist.hash ./max.txt
```
