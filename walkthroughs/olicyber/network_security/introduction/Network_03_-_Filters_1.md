# URL
https://training.olicyber.it/challenges#challenge-240
# Concept
* using Wireshark packet filters
# Method of solve
* this challenge wants us to filter all the packets by the `HTTP` protocol
* after loading up the file, we can type in `HTTP` in the display filter, then hit enter to filter out everything but HTTP packets
* click on the first packet in the list, and open up the `Hypertext Transfer Protocol` tab
* the flag is in the HTTP request header: `Flag-String`
