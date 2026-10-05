# URL
https://academy.hackthebox.com/app/module/81/section/787
# Concept
Using filters with TCPdump captures
# Notes
## Task #1 - Read the PCap without filters
```
tcpdump -r TCPDump-lab-2.pcap
```
## Task #2 - Identify the type of traffic seen.
* ports utilized
* common protocols
```
tcpdump -l -nn tcp or udp -r TCPDump-lab-2.pcap | cut -d " " -f 3,5 | tr -d ":" | tr " " "\n" | cut -d "." -f 5 | sort | uniq | awk 'length($0) <= 4'
```
or
```
tcpdump -l -nn tcp or udp -r TCPDump-lab-2.pcap | cut -d " " -f 3,5 | tr -d ":" | tr " " "\n" | cut -d "." -f 5 | sort | uniq -c | sort -n
```
## Task #3 - Identify conversations.
* identify the following:
  * Are you noticing any common connections between a server and host? If so, who?
    * we use the following command to get the pairs of IPs that communicate with each other the most:
    * ```Bash
      tcpdump -l -nn tcp or udp -r TCPDump-lab-2.pcap | sed -E 's/(\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\b)\.[0-9]+/\1/g' | cut -d " " -f 3,5 | tr -d ":" | sort | uniq -c | sort -n
      ```
    * the pairs that communicate the most in this capture are `172.16.146.2 207.244.88.140` and `64.233.177.91 172.16.146.2`  
  * What are the client and server port numbers used in the first full TCP three-way handshake?
    * first ID the first `SYN-ACK`, then `ACK` using `tcpdump`:
    * ```Bash
      tcpdump -l -S -nn -r TCPDump-lab-2.pcap | head -50 | grep -e '\[S\.\]' -C 5
      ```
    * the `[S]` means SYN, and the `[S.]` means SYN-ACK, and the `[.]` means ACK
    * if we see the first instance of `[S.]` then `[.]`, the two servers are communicating over port numbers `43806` and `80`
  * Who are the servers in these conversations? How do we know?
    * the servers are `172.16.146.2` and `95.216.26.30`
    * we know because the IPs are and the ports are both recorded with the three-way handshake flags
  * Who are the receiving hosts?
    * the hosts receiving are the ones that communicate on high-numbered ephemeral ports (into the 30-50000 range)
## Task #4 - Interpret the capture in depth.
* answer these questions:
  * What is the timestamp of the first established conversation in the pcap file?
    * if we find the first successful three-way handshake, we can ID the timestamp: `05:34:01.401270`
  * What is the IP address/s of apache.org from the DNS server responses?
  * ```Bash
    tcpdump -l -S -nn port 53 -r TCPDump-lab-2.pcap | grep -i "apache.org"
    ```
  * the IP address are `95.216.26.30` and `207.244.88.140` 
  * What protocol is being utilized in that first conversation? (name/#)
    * port `80` and the protocol is `http`
## Task #5 - Filter out traffic.
* Who is the DNS server for this segment?
  * ```
    tcpdump -l -S -nn port 53 -r TCPDump-lab-2.pcap
    ```
  * if we observe which server is communicating over port 53, there's only one IP address `172.16.146.1` 
* What domain name/s were requested in the pcap file?
  * we can use this command:
  * ```
    tcpdump -l -S -nn port 53 -r TCPDump-lab-2.pcap | grep -i "CNAME" | cut -d " " -f 9 | tr -d "," | sort | uniq -c | sort -n
    ```
* What types of DNS records could be seen?
  * use this command:
  * ```Bash
    tcpdump -l -S -nn port 53 -r TCPDump-lab-2.pcap | cut -d " " -f 7,8
    ```
  * this lets us know that the DNS records being sent are `A`, `AAAA`, and `CNAME`
* What information does an A record provide?
  * `A` records map a domain to an IPv4 address
  * `AAAA` records map a domain to an IPv6 address
* Who is the responding DNS server in the pcap? (hostname or IP)
  * this command lets us know which servers were contacted over port 53 (DNS):
```
tcpdump -l -S -nn dst port 53 -r TCPDump-lab-2.pcap
```
  * and the answer is `172.16.146.1`
## Task 6 - Filter for TCP traffic.
* Filter out the view so that we only see the traffic pertaining to HTTP or HTTPS. What web pages were requested?
  * we can use this command to see all of the traffic going over port 80 (HTTP)
```
tcpdump -l -s 0 -S -A -nn port 80 -r TCPDump-lab-2.pcap
```
  * and we can use this command to see which domains were queried using DNS:
```
tcpdump -l -S -nn dst port 53 -r TCPDump-lab-2.pcap
```
* What are the most common HTTP request methods from this PCAP?
  * from the previous command that covered port 80, the most common request methods were `POST`
* What is the most common HTTP response from this PCAP?
  * likewise, from the same previous command, the most common response code for HTTP is `200`
## Task 7 - What can you determine about the server in the first conversation.
* What can be determined about the webserver in the first conversation?
  * we can identify the first two hosts that communicate and try to establish a three-way handshake by using this command, then noting the IP addresses of the source and destination
```
tcpdump -l -S -nn -A 'tcp[13] & 2 != 0' -r TCPDump-lab-2.pcap | head
```
  * then we can isolate the packets sent between these two hosts:
```
tcpdump -l -s 0 -S -nn -A src 151.139.128.14 and src port 80 -r TCPDump-lab-2.pcap
```

 
