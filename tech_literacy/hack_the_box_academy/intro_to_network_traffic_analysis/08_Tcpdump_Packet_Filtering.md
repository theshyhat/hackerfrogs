# URL
https://academy.hackthebox.com/app/module/81/section/785
# Concept
Packet filtering
# Notes
## Help TCPdump Filters
```
host                 <- host will filter visible traffic to show anything involving the designated host. Bi-directional
src / dest           <- src and dest are modifiers. We can use them to designate a source or destination host or port.
net                  <- net will show us any traffic sourcing from or destined to the network designated. It uses / notation.
proto                <- will filter for a specific protocol type. (ether, TCP, UDP, and ICMP as examples)
port                 <- port is bi-directional. It will show any traffic with the specified port as the source or destination.
portrange            <- portrange allows us to specify a range of ports. (0-1024)
less / greater "< >" <- less and greater can be used to look for a packet or protocol option of a specific size.
and / &&             <- and && can be used to concatenate two different filters together. for example, src host AND port
or                   <- or allows for a match on either of two conditions. It does not have to meet both. It can be tricky.
not                  <- not is a modifier saying anything but x. For example, not UDP.
```
## Protocol RFC Links
* [IP Protocol](https://tools.ietf.org/html/rfc791) - RFC 791 describes IP and its functionality.
* [ICMP Protocol](https://tools.ietf.org/html/rfc792) - RFC 792 describes ICMP and its functionality.
* [TCP Protocol](https://tools.ietf.org/html/rfc793) - RFC 793 describes the TCP protocol and how it functions.
* [UDP Protocol](https://tools.ietf.org/html/rfc768) - RFC 768 describes UDP and how it operates.
* [RFC Quick Links](https://en.wikipedia.org/wiki/List_of_RFCs#Topical_list) - This Wikipedia article contains a large list of protocols tied to the RFC that explains their implementation.
* 




