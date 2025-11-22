# URL
https://training.olicyber.it/challenges#challenge-345
# Concept
* receiving a cookie from one endpoint
* supplying that cookie to another endpoint
# Method of solve
* the code that deploys the app is this:
```
import json
import sqlite3
from os import environ
from uuid import uuid4
from textwrap import dedent
from http import HTTPStatus
from flask import Flask, request, Response


app = Flask(__name__)

with sqlite3.connect("challenge.db") as db:
    db.execute("CREATE TABLE IF NOT EXISTS tokens(token TEXT PRIMARY KEY)")


@app.route("/token")
def token():
    token = str(uuid4())
    with sqlite3.connect("challenge.db") as db:
        db.execute("INSERT INTO tokens(token) VALUES (?)", (token,))
    response = Response("", status=HTTPStatus.NO_CONTENT)
    response.set_cookie("token", token)
    return response


@app.route("/flag")
def flag():
    try:
        token = request.cookies["token"]
    except KeyError:
        return Response("Missing token cookie. Unauthorized", mimetype="text/plain", status=HTTPStatus.UNAUTHORIZED)

    with sqlite3.connect("challenge.db") as db:
        row = db.execute("SELECT NULL FROM tokens WHERE token=?", (token,))

    if row is None:
        return Response("Bad token cookie. Unauthorized", mimetype="text/plain", status=HTTPStatus.UNAUTHORIZED)

    return Response(environ["FLAG"], mimetype="text/plain", status=HTTPStatus.OK)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```
* according to the code, the `/token` endpoint assigns a cookie, `token` to us with a random string name
* at the `/flag` endpoint, it checks whether you have a valid cookie or not, and if you do, it returns the flag
* the following curl commands will complete the challenge:
```
curl -v http://web-06.challs.olicyber.it/token
```
* note the cookie, `token` and supply that cookie and its value to the next request
```
curl -b "token=previous_command_cookie_value" -v http://web-06.challs.olicyber.it/flag
```

