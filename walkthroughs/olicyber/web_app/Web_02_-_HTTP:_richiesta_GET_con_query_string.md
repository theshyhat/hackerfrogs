# URL
https://training.olicyber.it/challenges#challenge-341
# Concept
* URL parameters
# Method of solve
* if we look at the Python script that is used to deploy the app, it looks like this:
```
from os import environ
from http import HTTPStatus
from flask import Flask, request, Response


app = Flask(__name__)


@app.route("/server-records")
def server_records():
    try:
        id = request.args["id"]
    except KeyError:
        return Response("Missing query parameter 'id'", mimetype="text/plain", status=HTTPStatus.BAD_REQUEST)
    if id.casefold() == "flag":
        return Response(environ["FLAG"], mimetype="text/plain", status=HTTPStatus.OK)
    else:
        return Response(f"Record '{id}' not found", mimetype="text/plain", status=HTTPStatus.NOT_FOUND)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```
* according to code, the app is looking for the `id` URL parameter, and returns a special string is the `id` parameter is set to `flag`
