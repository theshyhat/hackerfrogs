# URL
https://vulnyx.com/download.php?vm=University
# Concepts
* password reset vulnerabilities
* web app version enumeration
* Keepass database hash cracking
* sudo git privilege escalation
# Method of solve
## Starting Scans
* there are only two ports open on the box, `22` and `80`
* the web app has a vulnerability in the `/administration` endpoint in the `Forgot password` function
  * when we try to reset the password for the `admin` user, the temporary password is sent back to the user in the response
  * this can be observed when we send the request in Burp Suite
* this gets us access to the base app as the `admin` user
* the admin dashboard also features a list of default passwords for different users in the `News` section of the page
* these credentials are for a second web app, `Moodle`, which is accessible from the `/moodle` endpoint
* we try all of the creds, and the ones for the `richard.feynman` user work for us
* we found version information for the Moodle app on this endpoint: `/moodle/lib/upgrade.txt`
  * this lets us know the version being used is `4.4`
## Initial Access
* we research with `searchsploit`, `moodle 4.4` and we find an authenticated RCE exploit script:
```
searchsploit -m 52350
python 52350.py --url http://university.nyx/moodle --username richard.feynman --password Feynman#Quantum26 --courseid "3" --cmid "10" --cmd "whoami"
```
* from here we can run a reverse shell payload with the RCE script to get direct access
## Privilege Escalation
* we are running as the `www-data` user, but there is a suspicious file in the `/opt` directory
* the file is called `passwords.kdbx`, and it is a KeePass database file
* we copy it over to our own box, then we use a cracking tool to extract the password:
```
https://github.com/r3nt0n/keepass4brute
```
* we use this command:
```
./keepass4brute.sh ../passwords.kdbx /usr/share/wordlists/rockyou.txt
```
* the tool lets us know the password for the kdbx file
* then we use the `keepassxc-cli` tool to interact with the database
```
keepassxc-cli open ../passwords.kdbx
ls
show ssh -s
```
* now we have credentials for the `marcos` user
* this user has sudo access with the `git` command, which has a well-known privilege escalation path:
```
https://gtfobins.org/gtfobins/git/#shell
```
* these commands will get us a root shell
```
ln -s /bin/sh git-x
sudo git --exec-path=. x
```
* we're done!
