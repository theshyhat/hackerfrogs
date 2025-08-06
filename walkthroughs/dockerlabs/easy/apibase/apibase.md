# Port Scans
* There are only two ports: 22 and 5000
* The app on port 5000 seems to be a Python webserver
# Web App Enum
* The landing page seems to indicate that there's a /add endpoint and a /users endpoint. When we look at the /add endpoint in BurpSuite, it looks like we need to send a post request to the /add endpoint.
```
username=shyhat&password=hackerfrogs
```
* Then we can send a get request to the /users endpoint and get info about our new user
```
/users?username=shyhat
```
* From here we can fuzz for the correct URL parameter
```
ffuf -u "http://172.17.0.2:5000/users?FUZZ=testing" -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -mc all -fs 35
```
# Initial Access
* The output includes passwords, so we should probably fuzz the endpoint /users endpoint with ffuf
```
ffuf -mc all -request users_fuzz.txt -w /usr/share/seclists/Usernames/xato-net-10-million-usernames.txt -request-proto http -fs 32
```
The username is `pingu`, and it looks like their password is `pinguinasio`
* Login with SSH
# Privilege Escalation
* In the home directory, there is a pcap file. We can move it to our machine with Scp
```
scp -P 22 pingu@172.17.0.2:/home/network.pcap .
```
* In the pcap, there's a password in the FTP traffic for the root user
* Finis
