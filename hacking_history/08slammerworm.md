# Hacking History - Target 08: Slammer Worm
## Research Date: 2024-07-24
## What happened?
SQL Slammer is a 2003 computer worm that caused a denial of service on some Internet hosts and dramatically slowed general Internet traffic. It also crashed routers around the world, causing even more slowdowns. It spread rapidly, infecting most of its 75,000 victims within 10 minutes.
## When was the hack discovered?
- 25 January 2003 attack launched
- 05:30 UTC attack is launched
- within 10 minutes 75000 systems are infected
## How long do we think the hackers were operating before the hack was discovered?
Attackers crafted this malware for approximately half a year after the vulnerability was disclosed, and a patch was provided.
## Who was the target of the hack?
Any systems running MS SQL Server or Data Engine.
## How was the target initially compromised? What other hacking methods were employed?
The target was compromised through communication using UDP port 1434. A buffer overflow vulnerability was used.
## What was the impact of the hack?
The malware spread very quickly, and it caused massive slowdown of the internet and crashes of the systems infected as well as routers.
## Was the hacker identified? How confident are we of attribution?
No.
## Was the hacker punished? If so, how?
No.
## What is this hacker doing now? Did they engage in other known hacks?
We don't know.
## What was the response to the hack?
- filtering was imposed for network traffic on UDP port 1434
- systems were disconnected from the internet
- security patches were applied to affected systems
- because the worm operated from computer memory, it was erased on reboot
## What makes this hack famous?
- the disruption was widespread
- the hacker was never caught
- the malware operated in-memory (touchless malware)
## Lessons Learned?
- patch your stuff
- any big vulnerability could potentially be used as part of a bigger piece of malware if people fail to apply security patches to their systems.
