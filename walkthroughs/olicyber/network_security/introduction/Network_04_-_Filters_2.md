# URL
https://training.olicyber.it/challenges#challenge-241
# Concept
* Wireshark display filters: DNS and source IP
# Method of solve
* we have to use the PCAP file from the previous challenge
* in the display filter, we need to apply a filter that:
  * only displays packets from a specific IP address and
  * displays only DNS packets
* the following display filter gets the job done: `ip.src == 192.168.100.3 and dns`
* there is only one packet that fits the description
* we can find the flag in the packet details pane, under the `Domain Name System` tab
  * under the `Queries` sub-tab
