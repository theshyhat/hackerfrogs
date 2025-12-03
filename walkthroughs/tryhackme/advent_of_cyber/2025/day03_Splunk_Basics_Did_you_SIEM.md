# URL
https://tryhackme.com/room/splunkforloganalysis-aoc2025-x8fj2k4rqp
# Concept
* Splunk log search
# Method of solve
* the first thing we do is click on the green `Search and reporting` button on the top-left corner of the webpage
* then, in the `New search` field at the top of the page, type in `index=main`
* then, click on the button to the left of the green magnifying glass and select `All time`
* under the left-hand side menu, select `user_agent` under the `INTERESTING FIELDS` section
* in the resulting window, select the `Havij/1.17 (Automated SQL Injection)` value
## Q1 - What is the attacker IP found attacking and compromising the web server?
* note that all of the IP addresses in the results are from `198.51.100.55`
## Q2 - Which day was the peak traffic in the logs? (Format: YYYY-MM-DD)
* in the `New search` field, type in in `index=main`
* near the top of the interface, notice that there is a bar graph
* the largest bar in the graph is for `2025-10-12`
## Q3 - What is the count of Havij user_agent events found in the logs?
* under the left-hand side menu, select `user_agent` under the `INTERESTING FIELDS` section
* in the resulting window, observe that the `Havij/1.17 (Automated SQL Injection)` value is has a `Count` of `993`
## Q4 - How many path traversal attempts to access sensitive files on the server were observed?
* note that we have an IP address associated with malicious activity, `198.51.100.55`
* we can get only webtraffic from that IP with this search query:
```
index=main sourcetype=web_traffic "198.51.100.55"
```
* then we can further filter those events with the following to get potential path traversal attacks:
```
AND path="*..\/..\/*"
```
* after that's done, we note that it reads `658` events under the search bar
## Q5 - Examine the firewall logs. How many bytes were transferred to the C2 server IP from the compromised web server?
* the material tells us that the compromised webserver's IP is `10.10.1.5`
* we know that the malicious IP is `198.51.100.55`
* so we can combine these into one search
```
sourcetype=firewall_logs src_ip="10.10.1.5" AND dest_ip="198.51.100.55"
```
* we also need to filter on events which the firewall allowed in:
```
AND action="ALLOWED"
```
* we then see there are many events that were allowed through the firewall, but the question is asking how many bytes were transferred, so can tack this on to get the total bytes of all of the events:
```
| stats sum(bytes_transferred) by src_ip
```
* the whole search string looks like this:
```
sourcetype=firewall_logs src_ip="10.10.1.5" AND dest_ip="198.51.100.55" AND action="ALLOWED" | stats sum(bytes_transferred) by src_ip
```
* and the answer we get from this search is `126167`
