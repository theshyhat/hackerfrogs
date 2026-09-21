# URL
https://academy.hackthebox.com/app/module/81/section/773
# Concepts / Vocabulary
NTA - Network Traffic Analysis
# Notes
* NTA Use cases
  * `collecting` real-time traffic within the network to analyze upcoming threats.
  * `setting` a baseline for day-to-day network communications.
  * `identifying` and analyzing traffic from various network sources
  * `detecting` malware on the wire, such as ransomware, exploits, and non-standard interactions.
* a sign of `port scanning` is `SYN` packets being sent to ports that we never / rarely use on the network
* common NTA tools:
  * tcpdump
  * tshark
  * Wireshark
  * ngrep
  * tcpick
  * network taps (Gigamon, Niagra Taps)
  * network span ports
  * Elastic Stack
  * SIEMS
* the course will use a lot of BPF (Berkley Packet Filtering) syntax
* NTA workflow
  * `ingest` traffic
  * reduce noise by `filtering`
  * `analyze` and explore
  * `detect` and alert
  * `fix and monitor`
* 



