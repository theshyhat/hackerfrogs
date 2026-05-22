# URL
https://training.olicyber.it/challenges#challenge-246
# Concept
* using a pre-master secret log file to decipher TLS in PCAP files
# Method of solve
* we download both the PCAP file and the pre-master secret log file
* open up Wireshark and select:
```
Edit -> Preferences -> Protocols -> TLS -> Pre-Master Secret Log Filename
```
* then select the file
* all of the TLS packets should be decrypted
* use the following filter to see only the HTTP packets with a GET method:
```
http2.headers.method == GET
```
* follow the conversation for HTTP2, then select view `Show as ASCII`, and the flag should be at the top of the convo
* Finis

