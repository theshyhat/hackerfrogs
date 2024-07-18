# Hacking History - Target 05: Equifax Data Breach
## Research Date: 2024-07-17
## What happened?
Millions of users' data was breached and stolen from the American credit bureau, Equifax, in May and July 2017.
## When was the hack discovered?
May and July 2017
## How long do we think the hackers were operating before the hack was discovered?
Mid-May 2017 (6 weeks) (G) (Claude)
## Who was the target of the hack?
The Equifax credit bureau
## How was the target initially compromised? What other hacking methods were employed?
Because Equifax did not patch their deployment of Apache Struts in time, an exploit for Apache Struts was used to gain access. The organization had 2 months to patch their software, but failed to do so. Other methods were used for lateral movement, privilege escalation, and data exfiltration, but we are not sure what those methods were, specifically.
## What was the impact of the hack?
Private records of 147.9 million Americans along with 15.2 million British citizens and about 19,000 Canadian citizens were compromised in the breach. (W)
## Was the hacker identified? How confident are we of attribution?
The American govt attributed the hacks to 4 members of the Chinese People's Liberation Army. They said they were fairly confident of this, due to forensics investigation.
## Was the hacker punished? If so, how?
The hackers were not punished, but the indictments caused increased tension between America and China.
## What is this hacker doing now? Did they engage in other known hacks?
We do not know.
## What was the response to the hack?
The hackers do not appear to have released the stolen data on any known darknet forums, leading to the theory that they are still waiting to release it, or that it was used by a nation-state.
## What makes this hack famous?
* Scale of affected users (147 million users)
* Nature of data (potentially used for ID theft, financial fraud)
* Public Awareness and Trust (erosion of trust in credit bureaus)
## Lessons Learned?
* timely patch management (they did not patch for 2 months after a major security patch was issued)
* data encryption (most of the data was not encrypted, or encrypted, but the keys were on the same system...)
