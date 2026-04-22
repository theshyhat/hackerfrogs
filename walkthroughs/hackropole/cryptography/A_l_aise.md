# URL
https://hackropole.fr/en/challenges/crypto/fcsc2022-crypto-a-laise/
# Concept
* Vigenere cipher
# Method of solve
* we can use a tool like Cyberchef to solve this challenge:
```
https://cyberchef.io/#recipe=Vigen%C3%A8re_Decode('FCSC')&input=TWdkbnQgZndjdyBjeWdzdiEgUXF6dCBmZ2N2IGVreHVhcXMsIGt4IGF0dyBzZWhnaHYgbnYgZ2gKaHFtdHhnLCBva3FuIHRnIHlxIGFwa2tkdndjbGcgeWp3IHdzZnd0bHRnd3NmIGZneXlndHAKeXpnd2cgZ3d3IGdmZ3Jrd3UgZnR3IGpuZmFwbC4gVXdnIGRxbSBrcyBQc3B5Z2sgcXMKQ2h0bm4gMjlsaiBrcWogdm1nIHRnbGtmcG5weSBxayBhZ3d3IG9hdXhrZ3Au
```
* paste the ciphertext into the input field
* lookup the Vigenere decode operation from the left-hand side window
* drag it into the center window
* apply the key `FCSC`
* the flag is the name of the city mentioned in the message alone (no flag wrapper)

