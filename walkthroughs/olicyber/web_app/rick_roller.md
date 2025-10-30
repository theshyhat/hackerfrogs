# URL
https://training.olicyber.it/challenges#challenge-42
# Concept
* HTTP redirects
# Method of solve
* the landing page has a button that is supposed to "give you the flag"
* this button redirects you to the "Rick Roll" Youtube video
* what you need to do is inspect the redirect request when you navigate to that page:
```
curl -v http://roller.challs.olicyber.it/get_flag.php
```
