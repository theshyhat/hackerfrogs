# URL
https://hackropole.fr/en/challenges/misc/fcsc2022-misc-wifi/
# Concept
* setting up Wireshark to decrypt Wifi packets
* following TCP streams
# Method of solve
* we're given the Wifi password for the corresponding PCAP file: `FCSC p0w3r is the answer`
* after we've opened the PCAP file in Wireshark, we first have to identify the SSID of the wifi network:
  * look at any of the `802.11` protocol packets
  * look at the `IEEE 802.11 Wireless Management` tab in the Packet Details pane
  * look at `Tagged Parameters` -> `Tag` -> `SSID`, and we see the value `FCSC-WiFi`
* with the SSID name and the password value, we are able to add the key/value to the Wireshark protocols to decrypt those packets sent over the Wifi network
  * In the top menu: `Edit` -> `Preferences` -> `Protocols` -> `IEEE 801.11` -> `Decryption Keys` -> `Edit` -> key type `wpa-pwd`, with value `FCSC p0w3r is the answer:FCSC-WiFi`
* finally, we can find the TCP packets and follow the conversation, which reveals the flag
