# URL
https://training.olicyber.it/challenges#challenge-247
# Concept
* extracting file contents from an HTTP packet
# Method of solve
* find the HTTP packet that has the flag.png file
* right-click and select `follow TCP stream`
* in the viewer, select `Show as Raw`
* highlight everything in the server's first response, then paste it into CyberChef
* in CyberChef, use the recipe `From Hex`
* in the input, clip off all the beginning hexes until you read the magic bytes for the PNG file `89 50 4E 47`
* and then clip off all the ending footer data starting from `--------`, the last byte in the output should be a `0d`
* save the file in the output window as `flag.png`
* the flag is in the image
* DONE!

