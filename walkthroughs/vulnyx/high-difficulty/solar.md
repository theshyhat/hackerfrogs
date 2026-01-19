# URL
https://vulnyx.com/#solar
# Concepts
* MQTT access through websockets
# Method of solve
## Port Scanning
* there are the following ports open:
  * 22 - SSH
  * 80 - HTTP
  * 443 - HTTPS
* the SSL certificate for the web app on port 443 specifies two different domains: `www.sunfriends.nyx` and `www.solar.nyx`
* we add both of these domains to the `/etc/hosts` file
### The Sunfriends App
* the landing page of this app contains a lot of forum threads with usernames:
```
calvin
Robert24
JulianAdm
GreenThumb
AnnaSolar
SolarGuy
EcoFriendly
John20
```
### The Solar App
* the landing page of this app is a login page
* if we try logging in as an arbitrary username, the app responds with `No user found with that username.`
* after checking the 8 user accounts we found on the `solarfriends` app, there are only three user accounts which are valid:
```
calvin
JulianAdm
Robert24
```
* we can then attempt to brute force the login of the solar app with `Hydra`:
```
hydra solar.nyx http-post-form -I -s 443 -S -u -L ./users.txt -P /usr/share/wordlists/rockyou.txt "/login.php:username=^USER^&password=^PASS^:Invalid"
```
## Initial Access

## Privilege Escalation
