# URL
https://tryhackme.com/room/networkservices-aoc2025-jnsoqbxgky
# Concept
* network service discovery and interaction
# Method of solve
* from the AttackBox, use the following `nmap` command to scan the ports on the remote server:
```
nmap -p- -vv --script=banner 10.67.164.114
```
* this let us know that there are the following ports / services available on the server
```
port    service
22      SSH
80      HTTP
21212   FTP
25251   Maintenance  
```
## Q1 - What evil message do you see on top of the website?
* open the Firefox web browser in the AttackBox and navigate to the `http://<IP_ADDRESS>` endpoint
* the message is at the top-left corner of the webpage
## Q2 - What is the first key part found on the FTP server?
* access the FTP server using the following FTP command:
```
ftp <IP_ADDRESS> 21212
```
* login as `anonymous`
* download a file from the server:
```
ls
get tbfc_qa_key1
exit
```
then read the file
```
cat tbfc_qa_key1
```
## Q3 - What is the second key part found in the TBFC app?
* use netcat to communicate with the maintenance service:
```
nc <IP_ADDRESS> 25251
help
get key
```
## Q4 - What is the third key part found in the DNS records?
* we can check if the server is serving DNS:
```
nc -sU -p53 <IP_ADDRESS>
```
* now we can use the `dig` tool to get more infomation about the DNS service
```
dig @<IP_ADDRESS> key3.tbfc.local TXT
```
## Q5 - Which port was the MySQL database running on?
* put the three keys together and use it to unlock the admin panel on the webpage
* on the web console, use the following command to see what internal services are running
```
ss -tulpn
```
* one of the ports running is the default port for MySQL: `3306`
## Q6 - Finally, what's the flag you found in the database?
* we can log into the local mysql service from the admin webpage with this command
```
mysql
```
* then we can look through the database with these commands
```
show databases;
use tbfcqa01;
show tables;
select * from flags; 
```
