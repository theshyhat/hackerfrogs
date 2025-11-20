# URL
https://ringzer0ctf.com/challenges/50
# Concept
* extracting public key from RSA private key
# Method of solve
* the first thing we do is take the contents for the private and turn into a file
* then we run openssl to extract the public key from the private key with this command:
```
openssl rsa -in private.pem -pubout -out public.pem
```
* then we have to follow the instructions from the challenge and get just the base64 blob of the public key and md5sum it
```
cat public.pem | grep -v -e "---" | tr -d '\n' | md5sum
```
* submit the md5 hash and we receive a flag
* submit the flag
