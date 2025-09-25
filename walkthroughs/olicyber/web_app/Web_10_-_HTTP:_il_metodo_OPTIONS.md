# URL
https://training.olicyber.it/challenges#challenge-349
# Concept
* the OPTIONS HTTP method
# Method of solve
* the challenge wants us to make a request to `http://web-10.challs.olicyber.it/` and figure out which HTTP methods are allowed
* we can do that by sending a curl request to the page with the OPTIONS HTTP method
```
curl -v -X OPTIONS http://web-10.challs.olicyber.it/
```
* the server output tells us that we can use these methods: `GET`, `OPTIONS`, `HEAD`
* the problem is that these methods don't get us the flag
* the webserver code looks like this:
```
import json
from os import environ
from uuid import uuid4
from textwrap import dedent
from http import HTTPStatus
from flask import Flask, request, Response


app = Flask(__name__)


@app.route("/", methods=("GET", "HEAD", "OPTIONS", "POST", "PUT", "PATCH", "DELETE"))
def root():
    method = request.headers.get("X-Method", "GET")
    print(method)
    if method not in ("GET", "HEAD", "OPTIONS"):
        response = Response("Internal server error", mimetype="text/plain", status=HTTPStatus.INTERNAL_SERVER_ERROR)
        response.headers["X-Flag"] = environ["FLAG"]
        return response
    if method == "GET":
        return Response("Unauthorized", mimetype="text/plain", status=HTTPStatus.UNAUTHORIZED)
    response = Response("", status=HTTPStatus.UNAUTHORIZED)
    if method == "OPTIONS":
        response.headers["Allow"] = "HEAD, OPTIONS, GET"
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```
* according to the code, if we send a HTTP method that is not one reported by the `OPTIONS` method, then we get the flag:
```
if method not in ("GET", "HEAD", "OPTIONS"):
        response = Response("Internal server error", mimetype="text/plain", status=HTTPStatus.INTERNAL_SERVER_ERROR)
        response.headers["X-Flag"] = environ["FLAG"]
        return response
```
* so we can send a POST request to get the flag:
```
curl -X POST -v http://web-10.challs.olicyber.it/
```
