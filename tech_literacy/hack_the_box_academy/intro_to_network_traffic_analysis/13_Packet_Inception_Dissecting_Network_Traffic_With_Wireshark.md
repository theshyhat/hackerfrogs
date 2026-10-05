# URL
https://academy.hackthebox.com/app/module/81/section/789
# Concept
Practice portion of the course, working with Wireshark
# Notes
## Task #1 - Open a pre-captured file (HTTP extraction)
## Task #2 - Filter the results.
* use the following display filter:
```
http
```
## Task #3 - Follow the stream and extract the item(s) found.
* right-click one of the HTTP packets, then click on `Follow Conversation` -> `HTTP Stream`
* look through the different streams, and search for term `Content-Type: image` in the search window
  * there are mentions of this content type in streams `4`, `5`, `10` and `14`
* we can extract these by using the `File` -> `Export Objects` -> `HTTP`, then `Content-Type` -> `image/jpeg`, then `Save-All`
## Real Live Task
* extract a file from an ftp transfer
* locate the TCP conversation from the ftp-data protocol packets
* enter the stream
* select `Show and Save Data as` `Raw`
* then `Save as` the original filename `flag.jpg`

