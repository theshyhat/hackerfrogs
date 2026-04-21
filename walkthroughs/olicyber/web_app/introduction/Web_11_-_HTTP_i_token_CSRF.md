# URL
https://training.olicyber.it/challenges#challenge-350
# Concept
* CSRF tokens in web apps
# Method of solve
* the challenge asks us to contact one URL to get a valid session cookie and a CSRF token, then use that cookie and token value to contact another URL to get pieces of the flag for the challenge
* the URLs in question are: `http://web-11.challs.olicyber.it/login` and `http://web-11.challs.olicyber.it/flag_piece`
* first we need to contact the login endpoint, and we can that `curl`:
```
curl -X POST -H "Content-Type: application/json" -d '{"username": "admin","password": "admin"}' -v http://web-11.challs.olicyber.it/login
```
* after that request, we receive a session cookie as well as a CSRF token value. We need to use both these pieces of data to access the flag piece endpoint
```
curl -b "session=09bc34eb-3564-4c6f-8519-12a88b25287a" -v 'http://web-11.challs.olicyber.it/flag_piece?csrf=92698dafe37579b9&index=0'
```
* note that both the CSRF token parameter and the index parameter must be sent in the URL to access the piece of the flag
* repeat this 3 times to get the entire flag
## Python Method
```Python
import requests

login_URL = 'http://web-11.challs.olicyber.it/login'
flag_URL = 'http://web-11.challs.olicyber.it/flag_piece'

credentials = {"username": "admin","password": "admin"}

with requests.Session() as s:
  # login with credentials with POST
  login_res = s.post(url=login_URL, json=credentials)
  print(f"Login request sent! Received the following response:\n{login_res.text}")
  # retrieve the CSRF token in the response
  csrf_token = login_res.json()["csrf"]
  # retrieve the flag by making 4 GET requests to the flag endpoint
  flag_parts = []

  for i in range(4):
    res = s.get(url=flag_URL, params={"index": i, "csrf": csrf_token})
    print(f"Sending request number {i} to flag endpoint:")
    print(f"Received the following response:\n{res.text}")
    # update the flag parts and the CSRF token
    flag_parts.append(res.json()["flag_piece"])
    csrf_token = res.json()["csrf"]

  # print the combined flag
  print("This is the flag:")
  print("".join(flag_parts))
```
