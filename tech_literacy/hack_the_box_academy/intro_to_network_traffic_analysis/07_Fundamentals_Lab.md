# URL
https://academy.hackthebox.com/app/module/81/section/786
# Concept
* getting hands-on with tcpdump
# Notes
* tasks:
  * task 1 - confirm installation of tcpdump `which tcpdump`
  * task 2 - Which tcpdump switch is used to show us all possible interfaces we can listen to? `tcpdump -D`, then `tcpdump -i <interface name>`
  * task 3 - adding verbosity to our output and displaying contents in ASCII and Hex `-vX`
  * task 4 - grab our first full capture from the wire, and save it to a PCAP file. `-w <write_filename>`
  * task 5 - read the file into `tcpdump` (`-r`)and:
    * `-nn` <-- do not resolve hostnames or port numbers (first `n` is for IP address and second `n` is for port numbers
    * `-S` <-- show absolute (not relative) TCP sequence numbers
    * `-X` <-- printing packet contents in hex and ASCII format
    * put all together, it's `tcpdump -nnSXr <filename>`

    
