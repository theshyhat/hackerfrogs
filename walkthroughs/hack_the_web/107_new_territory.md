# URL
https://hack.arrrg.de/challenge/107
# Category
Network Hacking
# Concept
* port scanning
# Method of solve
* the challenge is asking us to fuzz ports in the `40000-41000` range, and find the port that is serving something on this domain: `arrrg.de`
* we can use the `nmap` program to scan on that port range:
```
nmap -vv -T2 -sV -p40000-41000 arrrg.de
```
* the answer is `unberührt`
