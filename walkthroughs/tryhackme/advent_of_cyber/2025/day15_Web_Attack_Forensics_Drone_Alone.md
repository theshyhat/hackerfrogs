# URL
https://tryhackme.com/room/webattackforensics-aoc2025-b4t7c1d5f8
# Concept
* using Splunk log analysis
* investigating a web app RCE on a Windows web server
# Method of solve
* in the AttackBox, open the AttackBox's Firefox web browser and navigate to the following webpage: `http://MACHINE_IP:8000`
* login to Splunk with the following credentials: `Blue:Pass1234`
* in the Splunk interface, make sure to change the timeframe of the events, click on the button to the left of the green magnifying glass and select `All time`
## Q1 - What is the reconnaissance executable file name?
* in the search field, paste in the following:
```
index=windows_sysmon *cmd.exe* *whoami*
```
* since the task info tells us that attackers use the whoami command to enumerate immediately after gaining access, the answer is `whoami.exe`
## Q2 - What executable did the attacker attempt to run through the command injection?
* in the search field, paste in the following:
```
index=windows_sysmon Image="*powershell.exe" (CommandLine="*enc*" OR CommandLine="*-EncodedCommand*" OR CommandLine="*Base64*")
```
* the attacker is using the RCE vulnerability to run Powershell commands, so `powershell.exe` is the answer
