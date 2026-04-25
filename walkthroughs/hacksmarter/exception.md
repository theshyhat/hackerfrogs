# URL
https://www.hacksmarter.org/courses/df65d37c-ed63-4eca-8f78-5dede200ec8e/
# Concept
* enumerating chat app groups / messages
* 
# Method of solve
## Port Scanning + Starting Enum
* Nmap reports that port 22 (SSH), port 80 (HTTP) and port 3000 (HTTP) are open
* the app on port 80 seems to be a very generic chatbot app
* the app on port 3000 is `Rocket Chat`:
```
https://developer.rocket.chat/
```
* we can register a user, then login to the system
* in the General channel of the app, we see what we assume to be an admin user: `localh0ste`
  * this user exposes their email in the General chat `localh0ste@exception.local`
* the API also returns the version of the app when we send a GET request to the `/api/v1/info` endpoint
  * the version number is `3.12.1`
* there is a known exploit for this version of Rocket Chat:
```
searchsploit rocket chat 3.12.1
```
* this RCE script requires three arguments:
  * the target URL `-t`
  * the admin email `-a`
  * a regular user email `-u`



