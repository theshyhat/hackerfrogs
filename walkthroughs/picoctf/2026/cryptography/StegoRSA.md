# URL
https://learn.cylabacademy.org/library/719
# Concept
* RSA encrypted message decyption via RSA private key
# Method of solve
```
exiftool image.jpg
```
the image file has an RSA private key in the EXIF metadata

pull out the hex bytes and convert it back into a key file
```
echo '<hex_bytes>' | xxd -r -p > key
```
Then use `openssl` to perform the decryption
```
openssl pkeyutl -decrypt -inkey key -in flag.enc -out flag.txt
```
