# URL
https://academy.hackthebox.com/app/module/81/section/954
# Concepts
* network layers refresher
# Notes
* PDU - Protocol Data Unit
  * data packet made up of control information and data encapsulated from each layer of the OSI model
  * PDUs consist of:
    * data
    * segment / datagram
    * packet
    * frame
    * bit
* Addressing Mechanisms
  * MAC (Media Access Control) addressing - a 48-bit six octet address represented in hexadecimal format
    * operates at layer 2 of the OSI / TCP-IP model
  * IP (internet protocol) addressing - delivers data between hosts across network boundaries
    * IPv4 - four 32-bit octet values from 0 to 255: e.g., `127.0.0.1`
    * IPv6 - sixteen 128-bit octets represented in hexadecimal format
      * uses four types of addresses:
      * unicast - Addresses for a single interface.
      * anycast - Addresses for multiple interfaces, where only one of them receives the packet
      * multicast - Addresses for multiple interfaces, where all of them receive the same packet
      * broadcast - Does not exist and is realized with multicast addresses
    
