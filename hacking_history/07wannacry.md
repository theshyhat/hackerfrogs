# Hacking History - Target 07: WannaCry
## Research Date: 2024-07-24
## What happened?
In May 2017, a cryptoworm called WannaCry was unleashed on the internet, and targetted systems that had not applies a particular security patch for Windows that had released the previous month. The worm was a ransomware virus that encrypted all of the data on affected systems and demanded payment in Bitcoin to decrypt the files.
## When was the hack discovered?
The attack began at 07:44 UTC on 12 May 2017 and was halted a few hours later at 15:03 UTC. (7 hours)
## How long do we think the hackers were operating before the hack was discovered?
The hackers were not operating before the hack was discovered.
## Who was the target of the hack?
Anyone who had not applied the security patch issued by Microsoft.
## How was the target initially compromised? What other hacking methods were employed?
The targets were initially comprimosed through the EternalBlue exploit, which attacked systems through the SMB protocol, specifically, the 1.0 version of the protocol. The DoublePulsar backdoor, also developed by the NSA, was used as a persistence method.
## What was the impact of the hack?
Systems all over the world, but most notably, the network of the British National Health Service, were affected, and caused these organizations to experience loss of productivity. Estimates are that it affected more than 230,000 computers in over 150 countries. (G)
## Was the hacker identified? How confident are we of attribution?
Attribution was laid to the North Korean Lazarus hacker group. We are highly confident to the attribution of this group.
## Was the hacker punished? If so, how?
No. The hacker was not punished.
## What is this hacker doing now? Did they engage in other known hacks?
We don't know what this hacker is doing now. It is believed that the Lazarus group was also involved in the Sony Pictures hack of 2014.
## What was the response to the hack?
The researcher, Marcus Hutchins, aka Malwaretech, discovered the kill switch to the malware and deployed it, stopping the spread of the attack. A decryptor was created for the malware after about a week of research. However, it was not an easy fix. (Claude)
## What makes this hack famous?
- the attack used an exploit stolen from the NSA (EternalBlue)
- it demonstrated the fact that the NSA was hording exploits to use to attack enemies instead of contacting the publishers of vulnerable software to help secure the software from attacks.
- use of worm-like propogation
- showed the importance of applying security patches to systems ASAP
- showed that importance of creating security patches for OS versions that have gone end-of-life
- it affected a very soft target in the form of the NHS, including many hospitals
## Lessons Learned?
- patch your stuff
- the NSA is hording exploits to use on its enemies
