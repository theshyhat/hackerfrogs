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
* Step 2: Look at the first packet in the list, then look at the hex-content window in the lower-right portion of the Wireshark interface and right-click on the part of the text on the right-hand side that starts with the text `User-Agent` and select `Copy Bytes as Hex + ASCII Dump ...as ASCII Text`
* Step 3: Go back to the TryHackMe webpage and paste in the 
