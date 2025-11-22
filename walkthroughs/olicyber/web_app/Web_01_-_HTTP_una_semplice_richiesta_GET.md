# URL
https://training.olicyber.it/challenges#challenge-340
# Concept
* using GET requests
# Method of solve
* just use a GET request to the URL in question: `http://web-01.challs.olicyber.it/`
## Curl
```
curl -v http://web-01.challs.olicyber.it/
```
## Python
```
import requests

URL = 'http://web-01.challs.olicyber.it/'
get_req = requests.get(URL)
req_text = get_req.text
print(req_text)
```


