# Challenge URL
https://play.picoctf.org/practice/challenge/349
# Vulnerability / Key Concept
URL Redirection
# Method of Solve
>This challenge asks us to login with the following credentials
> username: test
> password: test!
```
curl -L -vv -d "username=test&password=test!" http://saturn.picoctf.net:5350
1/login
```
> We are redirected to two pages, and the ID parameter values look like base64 encoded strings
```
echo 'cGljb0NURntwcm94aWVzX2FsbF90aGVfd2F5X2JlNzE2ZDhlfQ==' | base64 -d
```
