# URL
https://play.picoctf.org/practice/challenge/180?category=1&difficulty=2&page=2&search=
# Category
Web App Hacking
# Concept
* insecure deserialization
# Method of solve
* there is a number of endpoints we need to discover on this app, including phps pages:
```
gobuster dir -u http://mercury.picoctf.net:8404/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,phps
```
* we discover `authenticate.php`, `authenticate.phps` and `index.php` and `index.phps`
