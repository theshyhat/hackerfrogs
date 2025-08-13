# URL
https://hack.arrrg.de/challenge/108
# category
web app
# concept
* HTTP headers
* each HTTP request is sent with a bunch of HTTP headers to let the server know what kind of response it should send back
* this challenge wants us to modify a specific HTTP header to get the answer from the server
* the `Accept-Language` HTTP header lets the server know what language to send back to the web browser
# method of solve
* in this case, we can use the curl command to send an HTTP request to the Hack the Web website with modified HTTP headers
* The following curl command will get the response from the server with the answer for the challenge:
```
curl -v -H "Accept-Language: fr" -b "connect.sid=s%3AkSuCzl4D1epgxF16lNzRpMfilZkrWGij.ssQDi8rEAy53g9dpwgQdabTi4dChI3YzvDM5n5VsPG4; htw_language_preference=en" https://hack.arrrg.de/challenge/108
```
Note the modified `Accept-Language` header with the value `fr`
* the answer is `baguette`






