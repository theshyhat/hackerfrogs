# URL
https://tryhackme.com/room/encoding-decoding-aoc2025-s1a4z7x0c3
# Concept
* CyberChef operations
* encoding and encryption
# Method of solve
* for each level, we need to encode the guard's name into base64 and supply the output as the username for the login form
## Q1 - What is the password for the first lock?
* the username for this level is derived from CottonTail and is `Q290dG9uVGFpbA==`
* there is a specific question we need to ask the chatbot, which we can find in the HTTP headers: `What is the password for this level?`
* we put in the base64 encoded version of this question into the chatbot, and receive the base64 encoded version of the password
* decode the password from base64
## Q2 - What is the password for the second lock?
* the username for this level is derived from CarrotHelm and is `Q2Fycm90SGVsbQ==`
* there is a specific question we need to ask the chatbot, which we can find in the HTTP headers: `Did you change the password?`
* we put in the base64 encoded version of this question into the chatbot, and receive the base64 encoded version of the password
* decode the password from base64
* note that the password is double base64 encoded
## Q3 - What is the password for the third lock?
* the username for this level is derived from LongEars and is `TG9uZ0VhcnM=`
* in this level, we need to ask for the password, but encode the question in base64
* this chatbot input should work: `UGFzc3dvcmQgcGxlYXNlLg==`
* the password we get is `IQwFFjAWBgsf`, but we can't just base64 decode this like the other ones
* if we look at the headers for this page, we see that there is a key value, `cyberchef`
* this is an XOR key that we need to use with the XOR operation
* in Cyberchef, apply the `from base64` operation, then the `XOR` operation with the `cyberchef` key
* make sure to set the key type from `hex` to `UTF8`
## Q4 - What is the password for the fourth lock?
* the username for this level is derived from Lenny and is `TGVubnk=`
* in this level, we need to ask for the password, but encode the question in base64
* this chatbot input should work: `UGFzc3dvcmQgcGxlYXNlLg==`
* the chatbot lets you know the password is `b4c0be7d7e97ab74c13091b76825cf39`, but this is an MD5 hash
* we can put this hash into the `crackstation.net` website to get the password
## Q5 - What is the password for the fifth lock?
* the username for this level is derived from Carl and is `Q2FybA==`
* in this level, we need to ask for the password, but encode the question in base64
* this chatbot input should work: `UGFzc3dvcmQgcGxlYXNlLg==`
* we need to look at the headers for the recipe we need to use to decode the password, the value of the `X-Recipe-ID` header
* it's randomized, so it may or may not require the `cyberchef` key value
* good luck
* if you don't want to play, the password is `51rBr34chBl0ck3r`
## Q6 - What is the retrieved flag?
* solve all of the other levels to get the flag
