# URL
https://training.olicyber.it/challenges#challenge-46
# Concept
* cookie spoofing
# Method of solve
* this app wants us to click on the cookie 10 million times
* we don't want to do that
* the number of times clicked is contained directly in the website cookie
* we can go into the browser storage and edit the cookie
* or we can use this curl command to send the cookie with the valid value and get the flag:
```
curl -v http://click-me.challs.olicyber.it/ -b "cookies=10000000"
```




