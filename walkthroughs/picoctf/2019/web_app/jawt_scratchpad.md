# URL
https://play.picoctf.org/practice/challenge/25
# Concept
* JSON Web Tokens
* tampering with the token
* cracking the secret key
# Method of solve
* on the landing page of the web app we can set our name
* after setting the name, there is a JWT in our cookies
* we can tamper with the JWT, but first we need to figure out the secret key
* we can crack the key with John the Ripper
```
john jwt.txt --wordlist=/usr/share/wordlists/rockyou.txt
```
* we found the secret key, `ilovepico`
* we can use the following website to create a new key
[JWT Dot IO](https://www.jwt.io/)
* we need to set the username to `admin` and sign with the secret key that we found
* paste the JWT into the web browser cookies and we're done
