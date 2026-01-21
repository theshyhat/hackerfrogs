# URL
https://hack.arrrg.de/challenge/305
# Concept
* identify an encoding method
* base85 encoding
# Method of solve
* we see a long string of encoded characters
* it's got too many characters in its character set to be base64
* there's a larger character set in another encoding method, called base85
* base85 includes all uppercase and lowercase letters, all numbers, and all standard ASCII special characters
* we can use a website like this one to decode the message:
`https://cryptii.com/pipes/ascii85-encoding`
* the message is double encoded with the same encoding
