# URL
https://training.olicyber.it/challenges#challenge-51
# Concept
* cookies
# Method of solve
* the application lets us register a user
* after logging in with our credentials we see that we receive a cookie
* the cookie is base64 encoded
* we can create our own cookie to get access as the admin:
```
echo -n '2025/09/18-1758164555-admin' | base64
```
