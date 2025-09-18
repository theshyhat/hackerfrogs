# URL
https://training.olicyber.it/challenges#challenge-343
# Concept
* HTTP request headers
* HTTP Accept header
# Method of solve 
* the application uses the following code to deploy the app:
```
import json
from os import environ
from textwrap import dedent
from http import HTTPStatus
from flask import Flask, request, Response


app = Flask(__name__)

json_data = {
    "users": [
        {
            "name": "admin",
            "role": "admin",
            "registration_date": "2018-06-18T15:34:55Z",
        },
        {
            "name": "fruitfly",
            "role": "user",
            "registration_date": "2019-08-12T12:04:32Z",
        },
        {
            "name": "jim87",
            "role": "user",
            "registration_date": "2022-01-13T20:09:43Z",
        },
        {
            "name": "anonymous05",
            "role": "user",
            "registration_date": "2022-03-09T16:01:07Z",
        }
    ]
}

xml_data = dedent(f"""\
  <?xml version="1.0"?>

  <users>
    <user comment="{environ["FLAG"]}">
      <name>admin</name>
      <role>admin</role>
      <registration_date>2018-06-18T15:34:55Z</registration_date>
    </user>
    <user>
      <name>fruitfly</name>
      <role>user</role>
      <registration_date>2019-08-12T12:04:32Z</registration_date>
    </user>
    <user>
      <name>jim87</name>
      <role>user</role>
      <registration_date>2022-01-13T20:09:43Z</registration_date>
    </user>
    <user comment="Suspicious activity">
      <name>anonymous05</name>
      <role>user</role>
      <registration_date>2022-03-09T16:01:07Z</registration_date>
    </user>
  </users>
""")


@app.route("/users")
def users():
    content_type = request.accept_mimetypes.best_match(("application/json", "application/xml"))

    if content_type == "application/json":
        return Response(json.dumps(json_data, indent=2), mimetype="application/json", status=HTTPStatus.OK)
    elif content_type == "application/xml":
        return Response(xml_data, mimetype="application/xml", status=HTTPStatus.OK)
    else:
        return Response(
                "Not acceptable. Acceptable representations for this resource: application/json, application/xml",
                mimetype="text/plain",
                status=HTTPStatus.NOT_ACCEPTABLE)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```
* the code has one set of data that is returned if content type is set to JSON, and another set of data that is returned if the content type is set to XML. The flag is in the XML data
* the default content type is JSON
* we can use the following curl command to complete the challenge
```
curl -H "Accept: application/xml" -v http://web-04.challs.olicyber.it/users
```
