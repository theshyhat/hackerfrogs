# HackerFrogs AfterSchool - Forensics
# Session Topic: Network Forensics - Part 2
If you don't have an account at TryHackMe, create one at this link: https://tryhackme.com/signup
# Challenge 1: TryHackMe - Carnage
## TryHackMe Link
https://tryhackme.com/room/c2carnage
### Method of Solve
#### Part 1: Accessing the TryHackMe Machine and Opening the Pcap File in Wireshark
* Step 1: Click on the `Task 1` header on the TryHackme page
* Step 2: Under the `Task 1` header
* Step 3: Click on the green `Start Machine` button
* Step 4: After the machine finishes loading, click on the following folders in order: `Analysis`, `carnage.pcap`
#### Part 2: Inspecting the Date and Time of the First Packet to Answer the First Question
* Step 1: Click on the diplay filter search bar at the top of the Wireshark interface and type in `http` to filter out all of the packets except HTTP requests
* Step 2: Click on the first packet in the packet list view (Source should be 10.9.23.102 and Destination should be 85.187.128.24)
* Step 3: Double-click on the first row in the packet details window, and right-click on the `Arrival Time` row, then select `copy` then `value`
* Step 4: Submit `2021-09-24 16:44:38` as the answer for the first question
#### Part 3: Look at the Export Objects Option to Answer the Second Question
* Step 1: In the top row of options in Wireshark, click on `File`, then `Export Objects`, then `HTTP`
* Step 2: In the resulting window, click on the `Content Type` drop-down menu and click on `application/octet stream`
* Step 3: Observe the name of the file under the Filename column
* Step 4: Submit `documents.zip` as the answer for the second question
#### Part 4: Keep the Export Objects Window Open to Answer the Third Question
* Step 1: In the `HTTP object list` window that we're currently looking at, observe the `Hostname` column for the documents.zip file
* Step 2: Submit `attirenepal.com` as the answer for the third question
#### Part 5: Inspect the Zip File HTTP Packet to Answer the Fourth Question
* Step 1: When we click on a file in the `HTTP object list` window, the corresponding packet is selected in the packet list window
* Step 2: In the packet bytes window, scroll down to the bottom of the output and observe the file name
* Step 3: Right-click the packets bytes data and select `Copy Bytes as Hex + ASCII Dump` then `as Printable Text`
* Step 4: Minimize the Wireshark program, then right-click on the Analysis directory window, then select `Create Document`, then `empty file`
* Step 5: Double click on the empty file, then paste in the contents copied from Wireshark, go to the end of the output and highlight the file name `chart-1530076591.xls`
* Step 4: Submit `chart-1530076591.xls` as the answer for the fourth question
#### Part 6: Continue Inspecting the Same Packet to Answer the Fifth Question
* Step 1: Go back to Wireshark, and in the packet details window, double-click on the `Hypertext Transfer Protocol` row
* Step 2: Observe the `server` row and it's value `LiteSpeed`
* Step 3: Submit `LiteSpeed` as the answer for the fifth question
#### Part 7: Continue Inspecting the Same Packet to Answer the Sixth Question
* Step 1: Observe the `x-powered-by` row, and its value `PHP/7.2.34`
* Step 2: Submit `PHP/7.2.34` as the answer for the sixth question
#### Part 8: Isolating IP Addresses to Answer the First Bonus Question
* Step 1: Click on the diplay filter search bar at the top of the Wirshark interface and type in `http && ip.src_host==10.9.23.102` to filter out all of the packets except HTTP requests with the source address 10.9.23.102
* Step 2: At the bottom of the Wireshark window, we see the number of Packets in the file, and the number that are displayed, and that is our answer `394`
#### Part 9: Searching Packet Contents to Answer the Second Bonus Question
* Step 1: Release the display filter by clicking on the `x` button located on the right-hand side of the display filter window
* Step 2: Use the ctrl+f keyboard shortcut to bring up the search bar
* Step 3: In the search bar click on the `Display filter` drop-down menu and select `String`
* Step 4: Click into the search bar and type in `finejewels`, then click the `Find` button to the right
* Step 5: Observe that the URL `finejewels.com.au` is present in the resulting packet bytes window
