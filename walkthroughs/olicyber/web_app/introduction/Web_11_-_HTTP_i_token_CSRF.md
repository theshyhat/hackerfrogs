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
