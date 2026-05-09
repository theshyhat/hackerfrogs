# URL
https://training.olicyber.it/challenges#challenge-245
# Concept
* extracting packet data
* data transformation:
  * hexadecimal to ASCII
  * ASCII to hexadecimal
  * hexadecimal to binary file
# Method of solve
* go into the Wireshark and isolate the packets that are both TCP and from either of the two specified IP addresses:
* `ip.addr == 192.168.100.1 or ip.addr == 192.168.100.2`
* and then observe there is a packet in the list that has a larger length
* click into the `packet details pane` and scroll to the bottom
* in the `Data` section at the bottom
* in the `File` tab, click on `Extract Packet Bytes`, then save the extracted bytes as a file
* when we look at the contents of the file, we see it's a Gzip file
```
mv extracted_bytes extracted.gz
gunzip extracted.gz
file extracted
```
* and now it's a tar archive
```
tar -xvf extracted
```
* and there's `flag.txt`

