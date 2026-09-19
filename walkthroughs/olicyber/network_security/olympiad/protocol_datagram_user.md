# URL
https://training.olicyber.it/challenges#challenge-30
# Concept
* UDP streams
* piecing together stream content
# Method of solve
* the title of the challenge implies we need to inspect UDP packets instead of TCP packets
* if we follow the UDP stream, the second stream (stream 1) contains the conversation, as well as the flag
* we can also isolate the bytes from the UDP stream if we know what number stream to look for (using `tshark`):
```
tshark -r chall.pcapng -Y "udp.stream eq 1" -T fields -e data | xxd -r -p
```




