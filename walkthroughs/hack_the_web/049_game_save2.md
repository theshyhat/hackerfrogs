# URL
https://hack.arrrg.de/challenge/49
# Category
Cryptography
# Concept
* use a well-known encryption method to decrypt and edit data
* encrypt / decrypt using `AES-128 in ECB mode with PKCS padding`
# Method of solve
* we are given a hex string and a key
* we are told that the hex string was created using the AES-128 cipher in ECB with PKCS padding
* if we use the `openssl` program, we can decrypt the string, which we also have to reverse hex dump using the `xxd` program
* the string we are given is `cc76663b7d1e97ea2455b1c25676f44794fec90b0a9b823f916bf79387de4238`
* the key we are given is `786d229b0de877774a2f676d5bd895c3`
* the full one-liner that decrypts the string with `openssl` and `xxd` is this:
```
echo "cc76663b7d1e97ea2455b1c25676f44794fec90b0a9b823f916bf79387de4238" | xxd -r -p | openssl enc -d -aes-128-ecb -K "786d229b0de877774a2f676d5bd895c3"
```
* this lets us know that the decrypted data is this: `{"player":"John","gold":13}`
* the challenge states that we have to set our `gold` value to `999999`
* we can use the same encryption method with `openssl` and `xxd` to create the encrypted value:
```
echo -n '{"player":"John","gold":999999}' | openssl enc -aes-128-ecb -K "786d229b0de877774a2f676d5bd895c3" | xxd -p
```
