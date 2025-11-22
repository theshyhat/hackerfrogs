# URL
https://training.olicyber.it/challenges#challenge-346
# Concept
* HTTP methods
* HTTP head method
# Method of solve
* this is the code that deploys the app:
```
import json
from os import environ
from uuid import uuid4
from textwrap import dedent
from http import HTTPStatus
from flask import Flask, request, Response


app = Flask(__name__)


@app.route("/")
def root():
    response = Response("Unauthorized", mimetype="text/plain", status=HTTPStatus.UNAUTHORIZED)
    if request.headers.get("X-Method") == "HEAD":
        response.headers["X-Flag"] = environ["FLAG"]
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```
* according to the code, if we send a `HEAD` request to the server, instead of the usual `GET` request, then there will be a an additional response header sent back
* the extra response header will contain the flag
* this curl command will solve the challenge:
```
curl -v -X HEAD http://web-07.challs.olicyber.it/
```
