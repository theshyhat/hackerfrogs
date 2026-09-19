# URL
https://training.olicyber.it/challenges#challenge-19
# Concept
* always look at the metadata
* always run strings on the PCAP file
# Method of solve
* this challenge is not about inspecting packets
* it's about inspecting metadata
* the flag can be found in Wireshark using the `Statistics` -> `Capture File Properties` menu, and can be found under `Comments`
* we can also get this info using `capinfos capture.pcapng`
* we can also get the flag using `strings` and `grep`


