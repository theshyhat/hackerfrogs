# URL
https://training.olicyber.it/challenges#challenge-239
# Concept
* looking at packet details
# Method of solve
* download the PCAP file and open in Wireshark
* look at packet number 4
* the first part of the flag is going to be the `source MAC address`
  * we can find this in the second tab down in the packet details pane `Ethernet II...`
  * the value of `Source` is the first part of the answer, the MAC address
* the second part of the flag is the length of the data
  * we can find this in the last tab in the packet details pane `Data`
* we put this together in the following format: `flag{Source_MAC_address/data_bytes_length}`
