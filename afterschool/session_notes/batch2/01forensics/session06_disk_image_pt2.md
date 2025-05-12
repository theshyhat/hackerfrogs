# HackerFrogs AfterSchool Forensics Session 6
## Session Topic: Disk Image File Forensics - Part 2
# Challenge 1: TryHackMe Advent of Cyber 2023 - Task 30
## TryHackMe Link
https://tryhackme.com/room/adventofcyber2023
### YouTube Walkthrough Link
https://youtu.be/PcaYV96pdRY?t=749
### Method of Solve
#### Part 1: Accessing the TryHackMe Machine and Opening the File in Autopsy
* Step 1: Click on the `Task 30` header on the TryHackme page
* Step 2: Under the `Task 30` header, click on the green `Start Machine` button
* Step 3: After the machine finishes loading, click on the `Autopsy` shortcut icon on the desktop
* Step 4: After Autopsy finishes loading, click on the `Open Recent File` button, then double-click `Tracy McGreedy` in the list (there's only one file)
#### Part 2: Inspecting Photo Files to Answer the First Question
* Step 1: In the tree viewer window, click on `File Views`, then `File Types`, then `By Extension`, then `Images`
* Step 2: In the contents viewer window, click on the `Size` column to order the images by image size
* Step 3: In order, click on the files, and observe their contents in the details viewer window. The `board2.jpg` file displays the flag
* Step 4: Submit `THM{DIGITAL_FORENSICS}` as the answer for the first question
#### Part 3: Look at the Phone Contacts to Answer the Second Question
* Step 1: In the tree viewer window, click on `Data Artifacts`, then `Contacts`
* Step 2: Observe the names of the contacts under the `Name` column (Detective Frost-eau is the Snowman character)
* Step 3: Submit `Detective Carrot-Nose` as the answer for the second question
#### Part 4: Inspect the Messages to Answer the Third Question
* Step 1: In the tree viewer window, click on `Data Artifacts`, then `Messages`
* Step 2: In the contents viewer window, click on the first message, and observe that the contents of the message appear in the details viewer window
* Step 3: Scroll through the messages, and eventually we see a password
* Step 4: Submit `chee7AQu` as the answer for the third question
