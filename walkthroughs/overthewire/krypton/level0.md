# Password
no password
# Concept
* base64 encoding
# Method of solve
* in this level, we're asked to decode the level 1 password, which is given to us as `S1JZUFRPTklTR1JFQVQ=`
* this is a base64-encoded string
* we can decode using a Linux command:
```
echo 'S1JZUFRPTklTR1JFQVQ=' | base64 -d
```
* the result is the password for the next level
