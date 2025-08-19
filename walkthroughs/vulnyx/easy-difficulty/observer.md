# URL
https://vulnyx.com/#observer
# Port Scans
There are a lot of ports open, but the only ones that matter are ports 22 and 80
# Initial Access
* On the landing page of the web app, there are user names
* We record all of the first names, because Linux usually doesn't use last names for usernames
* we use the usernames as passwords in a password spray attack:
```
ncrack -U users_linux.txt -P users_linux.txt -vv -T 5 ssh://192.168.10.11:22
```
* we find out that the `niscal` user is using their username as their password
* when we try logging in as the niscal user, we find that we get kicked out, and there's a message saying that the terminal is busy
* we are able to get access to the niscal user's account if we use SSH with X11:
```
ssh -X niscal@<IP_ADDRESS>
```
* when we do that, we see a username and password revealed to us `remo:REMOisGOD`
* we login to SSH as the remo user
# Privilege Escalation
* there's suspicious content in the remo user's environment variables
* turns out it is a base64-encoded SSH private key for the root user
