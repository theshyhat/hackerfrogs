# HackerFrogs AfterSchool - Forensics
# Session Topic: Network Forensics - Part 1
If you don't have an account at TryHackMe, create one at this link: https://tryhackme.com/signup
# Challenge 1: TryHackMe - Where Is All This Data Going
## TryHackMe Link (Task 14)
https://tryhackme.com/room/adventofcyber3
### YouTube Walkthrough Link
https://youtu.be/3WLYKpNulX8?t=838
### Method of Solve
#### Part 1: Accessing the TryHackMe AttackBox and Opening the Pcap File in Wireshark
* Step 1: Click on the `Task 14` header on the TryHackme page
* Step 2: Navigate to the top of the webpage, and click on the `Start AttackBox` button located underneath the `Advent of Cyber 3 (2021)` header
* Step 3: After the AttackBox desktop finishes loading, click into the terminal message and press enter to close the window
* Step 4: In the AttackBox desktop, click on the following folders in order: `root's Home`, `Rooms`, `AoC3`, `Day9`, `AoC3.pcap`
#### Part 2: Inspecting the HTTP Packets to Answer the First Question
* Step 1: Click on the diplay filter search bar at the top of the Wirshark interface and type in `http.request.method==GET` to filter out all of the packets except HTTP GET requests
* Step 2: Look at the `Info` column for the packets and observe that the common endpoint for the HTTP requests is the `/login` directory
* Step 3: Submit `login` as the answer for the first question
#### Part 3: Inspecting the HTTP Packets to Answer the Second Question
* Step 1: Click on the diplay filter search bar at the top of the Wirshark interface and type in `http.request.method==POST` to filter out all of the packets except HTTP POST requests
* Step 2: In the packet details window (lower-left window), observe that the bottom-most tab `HTML Form URL Encoded` has a password `Christmas2021!`
* Step 3: Submit `Christmas2021!` as the answer for the second question
#### Part 4: Inspecting the HTTP Packets to Answer the Third Question
* Step 1: In the packet details window, observe that the `Hypertext Transfer Protocol` tab includes the `User-Agent` header, with a value of `TryHackMe-UserAgent-THM{d8ab1be969825f2c5c937aec23d55bc9}`
* Step 2: Copy the value by right-clicking on the row, then select `copy`, then `value`
* Step 3: Submit `TryHackMe-UserAgent-THM{d8ab1be969825f2c5c937aec23d55bc9}` as the answer for the third question
#### Part 5: Inspecting the DNS Packets to Answer the Fourth Question
* Step 1: Click on the diplay filter search bar at the top of the Wirshark interface and type in `dns.txt` to filter out all of the packets except DNS TXT requests
* Step 2: In the packet hex window (lower-right), observe that there appears to be a flag at the end of the data. Double-click that data, and see that the same value has been highlighted in the packet details window (lower-left)
* Step 3: Right-click the highlighted row in the packet details window and select `copy`, then `value`
* Step 4: Submit `THM{dd63a80bf9fdd21aabbf70af7438c257}` as the answer for the fourth question
#### Part 6: Inspecting the FTP Packets to Answer the Fifth Question
* Step 1: Click on the diplay filter search bar at the top of the Wirshark interface and type in `ftp` to filter out all of the packets except FTP requests
* Step 2: Observe that the end of the packet hex window contains a password. Double-click it, and then copy the value from the packet details window
* Step 3: Submit `TryH@ckM3!` as the answer for the fifth question
#### Part 7: Inspecting the FTP Packets to Answer the Sixth Question
* Step 1: This question makes reference to the `secret.txt` file. Locate the FTP packet that contains `secret.txt` in the `Info` column and click on it
* Step 2: In the packet details window, observe the  `Request command` parameter and its value `STOR`
* Step 3: Submit `STOR` as the answer for the sixth question
#### Part 7: Inspecting the FTP-data Packets to Answer the Seventh Question
* Step 1: Click on the diplay filter search bar at the top of the Wirshark interface and type in `ftp-data` to filter out all of the packets except FTP-data requests
* Step 2: Observe that there's only one packet, and that the contents of the packet contains a flag. Double-click the flag value, then copy the value in the packet details window
* Step 3: Submit `123^-^321` as the answer for the seventh question
