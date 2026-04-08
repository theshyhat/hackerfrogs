# URL
https://training.olicyber.it/challenges#challenge-348
# Concept
* sending JSON data in a POST request
# Method of solve
* the challenge is asking us to send a specific POST request to this endpoint: `http://web-09.challs.olicyber.it/login`
* they also want us to submit `username:admin` and `password:admin`, but in a JSON format
* we can craft a payload in curl to send this data
```
curl -X POST -H "Content-Type: application/json" -d '{"username": "admin","password": "admin"}' -v http://web-09.challs.olicyber.it/login
```
## Python solution
```Python
import requests

URL = 'http://web-09.challs.olicyber.it/login'

data = {
  "username":"admin",
  "password":"admin" 
} 
 
headers = {   
  "Content-Type":"application/json"
}
 
# Make a post request to the endpoint
# and save the reponse body
post_req = requests.post(URL, json=data, headers=headers)
req_body = post_req.text

# Print the response body
print(req_body)
```
