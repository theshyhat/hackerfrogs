# Password
KRYPTONISGREAT
# Concept
* rot13
# Method of solve
* the password for the next level is in the kypton2 file located here:
```
/krypton/krypton1/krypton2
```
* we're told that this message has been encrypted using a rotation cipher
* the most common rotation cipher is ROT13, which is an implementation of the Caesar cipher:
* use this `tr` command to decrypt the message
```
cat /krypton/krypton1/krypton2 | tr "A-Z" "N-ZA-M"
```




