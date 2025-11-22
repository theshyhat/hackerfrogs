# URL
https://training.olicyber.it/challenges#challenge-347
# Concept
* sending POST requests
* sending specific data to a web server via POST request to get desired output
# Method of solve
* the challenge asks us to send a specific POST request to this endpoint
```
http://web-08.challs.olicyber.it/login
```
* we need to send the `username` and `password` parameters in the request, with values `admin` and `admin`, respectively
* we also need to send the correct MIME-type with the POST request, which will be `application/x-www-form-urlencoded`
* the curl request that fulfills all of the above criteria is as follows:
```
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "username=admin&password=admin" -v http://web-08.challs.olicyber.it/login
```
