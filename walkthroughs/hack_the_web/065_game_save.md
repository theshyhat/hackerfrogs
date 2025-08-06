# URL
https://hack.arrrg.de/challenge/65
# Category
Cryptography (Encoding)
# Concept
* base64 encoding and decoding
# Method of solve
* the amount of gold you have in this game is encoded as a base64 string
* we need to figure out the pattern for how much gold we have, then replace the amount with the 999999 gold that we require
* the initial base64 string is `eyJnb2xkIjoxfQ==`
* if we decode that string, it is `{"gold":1}`
* so we need to use a base64 encoding app or program to encode the following string
```
{"gold":999999}
```
* the answer is `eyJnb2xkIjo5OTk5OTl9`
