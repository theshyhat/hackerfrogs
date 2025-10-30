# URL
https://training.olicyber.it/challenges#challenge-41
# Concept
* different HTTP methods
* the `HEAD` HTTP method
# Method of solve
* the webpage doesn't give us the flag if we access it using the `GET` HTTP method
* if we send a `HEAD` method request, then the flag is included in the response headers
```
curl -X HEAD -v http://headache.challs.olicyber.it/
```
