# URL
https://ringzer0ctf.com/challenges/1
# Concept
* SQL injection
* authentication bypass
# Method of solve
* there is a login page
* the app is vulnerable to SQL injection
* we can use the following SQL authentication bypass payload to login to app without a valid username or password
```
' or 1=1 -- -
```
