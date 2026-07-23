# URL
https://mega.nz/file/FIkxFADI#DBsaxhta2kI731hg_T1aBTojfhGUJHXEVI20GAScDFY
# Concept
* JWT hacking
  * JWT signing key cracking
* reused credentials
* sudo find
# Method of solve
## Beginning Scans
* there are only two ports open, `22` and `80`
* on the landing page of the website there are guest credentials on in HTML comments
* we use these to login, and we find there is an admin panel that we can't access
* we also find that our session cookie for the guest user is a JWT
* we are able to crack the JWT's signing key using John the Ripper
```
john jwt.cookie --wordlist=/usr/share/wordlists/rockyou.txt
```
* with this key, and a web app like `jwt.io`, we can spoof a cookie for the `administrator` user, with `admin` access
## Initial Access
* the admin dashboard has a `ping` function that uses OS commands in its operation
* giving this payload confirms that it's vulnerable to OS command injection:
```
172.17.0.1; whoami #
```
* and from here, we can upload a reverse shell binary and get direct access to the machine
## Privilege Escalation
* there is a `config.php` file in the web directory that contains a password for database access
* there is also a `bruce` user
* we combine these two to get access to the `bruce` account
* the bruce user has sudo permissions with the `find` commmand, which is a well-known vulnerable binary when run as sudo
```
sudo find . -exec /bin/bash \; -quit
```
* and now we're root

