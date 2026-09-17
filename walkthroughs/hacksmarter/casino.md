# URL
https://www.hacksmarter.org/courses/cc04f9ec-35e3-4065-b972-9d0b84a7b371/
# Concept
* login brute-forcing
* SSTI (server-side template injection)
* SSH private key theft
* .bash_history enumeration
* special user group files
# Method of solve
## Starting Scans
* nmap tell us that ports `22` `80` and `2222` are open
* there is a login page on the landing page of the web app
* we're told that we have to login with a combination of a room number (from 101 onwards) and a last name
* we can gather a list of room numbers and another list of common surnames and attempt to brute-force the login page
  * this is assuming that we record the login POST request using Burpsuite and save the request data to a file (`wifi_login.txt`)
```
ffuf -request wifi_login.txt -w ./room_num.txt:FUZZ1 -w ./common-surnames.txt:FUZZ2 --request-proto HTTP -fs 5223
```
* this lets us know that the valid room number / surname combo is `107:Johnson`
## Initial Access
* once authenticated to the app, we notice that on the profile page, our username, which we can adjust, is reflected back to us
* this means we can test for SSTI (server-side template injection)
  * we give this payload `{{ 7 * 7}}`, and it does the math for us
  * we give this payload `{{ ''.__class__.__mro__[1].__subclasses__() }}`, and it returns the objects in the Python code
  * so we can run arbitrary commands through this payload: `{{ lipsum.__globals__["os"].popen('<OS COMMAND HERE>').read() }}`
* we use the SSTI to upload and run a reverse shell binary for us, giving us access as the `www-data` user
## Privilege Escalation
### As the www-data user
* there are two regular users on the system: `george` and `david`
* the `george` user has open permissions on the `.ssh` directory in his home folder, which contains a private key: `id_rsa`
  * we copy the contents of this key to our attacker machine and login as `george` through the SSH service on port 2222
### As the george user
* the `george` user has sensitive data in his `.bash_history` file, which includes the password for the `david` user
### As the david user
* the `david` user is part of a special group `adm`, which is a group that usually has access to log files
* one of the log files that belongs to the `adm` group exposes the password for the root user
* finis

