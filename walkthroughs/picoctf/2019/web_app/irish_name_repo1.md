# URL
https://play.picoctf.org/practice/challenge/80
# Concept
* SQL injection
* SQL login bypass technique
# Method of solve
* there is a login page on the app
* if we send a single quote character, the app doesn't send back output
* we can give the SQL login bypass payload `or 1=1 -- ` and login to get the flag
