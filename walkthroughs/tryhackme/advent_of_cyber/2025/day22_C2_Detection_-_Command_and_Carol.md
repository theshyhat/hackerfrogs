# URL
https://tryhackme.com/room/detecting-c2-with-rita-aoc2025-m9n2b5v8c1
# Concept
* RITA framework
* PCAP Analysis
# Method of solve
* open a terminal, then give the following commands to start RITA:
```
zeek readpcap ~/pcaps/rita_challenge.pcap ~/zeek_logs/challenge
rita import --logs ~/zeek_logs/challenge/ --database challenge
rita view challenge
```
## Q1 - How many hosts are communicating with malhare.net?
* in the RITA sidebar (right-hand side), look at the `Prevalence` value
## Q2 - Which Threat Modifier tells us the number of hosts communicating to a certain destination?
* the answer is `prevalence`
## Q3 - What is the highest number of connections to rabbithole.malhare.net?
* among the hosts that connect to `rabbithole.malhare.net`, look at the `Connection count` value in the sidebar, and choose the highest value
## Q4 - Which search filter would you use to search for all entries that communicate to rabbithole.malhare.net with a beacon score greater than 70% and sorted by connection duration (descending)?
* the answer is `dst:rabbithole.malhare.net beacon:>=70 sort:duration-desc`
## Q5 - Which port did the host 10.0.0.13 use to connect to rabbithole.malhare.net?
* in the sidebar, look at the `Port:Proto:Service` value for the `10.0.0.13` host
