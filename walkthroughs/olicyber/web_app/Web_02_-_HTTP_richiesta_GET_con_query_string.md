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
## Curl
* all we need to do supply the URL with the parameters plugged in:
```
http://web-02.challs.olicyber.it/server-records?id=flag
```
## Python
```
import requests

URL = 'http://web-02.challs.olicyber.it/server-records'

URL_params = {'id': 'flag'}

get_req = requests.get(URL, params=URL_params)
req_text = get_req.text
print(req_text)
```
