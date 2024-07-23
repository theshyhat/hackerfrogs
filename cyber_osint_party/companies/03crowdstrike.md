# Cyber OSINT Party: Target 03 - CrowdStrike
## Research date: 2024-06-26
## What are their services / products?
It provides cloud workload and endpoint security, threat intelligence, and cyberattack response services. (W) 
## Where are their offices?
Austin, Texas, United States of America (W) (G)
## What's their official name?
CrowdStrike Holdings, Inc. (W) (D&B)
## Who's their founder?
George Kurtz (CEO), Dmitri Alperovitch, Gregg Marston (W) George Kurtz (CEO), Dmitri Alperovitch (G). George Kurtz, Dmitri Alperovitch, and Gregg Marston (P)
## What's their current leadership?
George Kurtz (CEO) (G) (P)
## What year were they established?
2011 (W) (G) (P)
## Have they done business under other names?
No (W) (G) (P)
## Who are some other notable members of their org?
Dmitri Alperovitch (CTO), Gregg Marston, GERHARD WATZINGER (Chairman), ROXANNE AUSTIN (president and CEO) (O)
## How many employees work there?
8,429 (April 30, 2024) (W), 7,00 (G),  7,925 (2024) (P)
## What big news stories have they been involved in?
* Democratic National Committee cyberattacks. 2017 (W) (G)
* Sony Pictures hack (2014) (P)
* 2018 Winter Olympics cyberattack (P)
* 2024 CrowdStrike Falcon App Incident
## What are some examples of media appearances they've been involved in?
* CrowdStrike CEO George Kurtz goes one-on-one with Jim Cramer (Y)
https://www.youtube.com/watch?v=X4ZOqQHkbXU
* CrowdStrike: How to Triage a Detection (Y)
https://www.youtube.com/watch?v=yviFcaNe0v4
* Crowdstrike CEO talks strong Q1 earnings report, AI, and cybersecurity (Y)
https://www.youtube.com/watch?v=2jca2tFh7pk
## What is their official website and their social media accounts?
* Official Website
https://www.crowdstrike.com/
* YouTube Channel (O)
https://www.youtube.com/@CrowdStrike
* X / Twitter (O)
https://twitter.com/CrowdStrike
* Facebbook (O)
https://www.facebook.com/CrowdStrike/
* Instagram (O)
https://www.instagram.com/crowdstrike/?hl=en
* LinkedIn (O)
https://www.linkedin.com/company/crowdstrike

# CrowdStrike 2024 "Incident" (Falcon)
## Research Date: 2024-07-22
## What happened?
CrowdStrike's Falcon Sensor product, which is installed at the kernel level of Windows OS systems, received a update with buggy code, which caused the program to crash. Because the app operates at the kernel-level of the OS, the app crashes the system when it fails.
## What was the timeline for the incident?
July 19 at 04:09 - the bug was introduced
 06:48 - google reported the problem
 05:27 - CrowdStrike reverted the update
## How many systems were affected?
8.5 million computers (G) (BBC)
## What was the cause of the bug?
Update to the Falcon Sensor application
## How was the situation resolved?
CrowdStrike rolled back its update after 1 hour, 18 minutes of rolling the patch out. Anyone looking to manually uninstall the patch needed to boot the server in safe mode, which requires physical access to the system, and is time-consuming.
## What was the aftermath of the event?
Serveral industries, including airlines, financial companies (banks), hospitals, and retail outlets were not able to do business due to reliance on coputer networks and connectivity. CrowdStrike's stocks fell by 11% on the day, and Microsoft's stock fell by 1%.
## Lessons learned?
Although this was not a cyberattack, it shows that reliance on apps that function on the kernel level of the OS can be very vulnerable to supply-chain attacks, such as a malicious update. It also sheds light on the fact that piece of software that operates on the kenerel level has to be carefully thought out before allowing it be installed.
