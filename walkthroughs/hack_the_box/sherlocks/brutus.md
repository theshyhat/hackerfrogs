# URL
https://app.hackthebox.com/sherlocks/Brutus/play
# Description
```
In this very easy Sherlock, you will familiarize yourself with Unix auth.log and wtmp logs. We'll explore a scenario where a Confluence server was brute-forced via its SSH service. After gaining access to the server, the attacker performed additional activities, which we can track using auth.log. Although auth.log is primarily used for brute-force analysis, we will delve into the full potential of this artifact in our investigation, including aspects of privilege escalation, persistence, and even some visibility into command execution.
```
# Concept
* `auth.log` inspection
* identifying brute force attacks in logs
* inspection of `wtmp` files
# Method of solve
## Part 0 - Downloading and Unzipping the File
* Download the zip file
* Unzip the file. Note, that the stadnard zip program won't work, so we should use `7z`: `7z x Brutus.zip`. The zip password is `hacktheblue`
## Part 1 - Q1: Analyze the auth.log. What is the IP address used by the attacker to carry out a brute force attack?
* Grep IP addresses from the `auth.log` file. The address that appears the most is likely the address we're looking for:
```
grep -o -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' auth.log | sort | uniq -c
```
* the answer is `65.2.161.68`, which appears 214 times in the log
## Part 2 - Q2: The bruteforce attempts were successful and attacker gained access to an account on the server. What is the username of the account?
* the following command indicates that the brute-froce IP address successfully logs in a couple of times as the `root` account, which is the answer:
```
grep -e "65.2.161.68" auth.log | grep -e 'Accepted'
```
## Part 3 - Q3: Identify the UTC timestamp when the attacker logged in manually to the server and established a terminal session to carry out their objectives. The login time will be different than the authentication time, and can be found in the wtmp artifact.
* this command will retrieve the `root` user login from the `65.2.161.68` IP address, returning only the timestamp:
```
python utmp.py wtmp | grep "65.2.161.68" | grep "root" | cut -d '"' -f 20
```
* however this returns the time in localtime, and the answer we're looking for is in UTC format
* we can get our timezone and the offset from the UTC timezone with the following command:
```
date "+%Z %z"
```
* for example, if the output is `-0500` that means that our local time is 5 hours behind
* the answer, in the proper format: `2024-03-06 06:32:45`
## Part 4 - Q4: SSH login sessions are tracked and assigned a session number upon login. What is the session number assigned to the attacker's session for the user account from Question 2?
* in the logs, new SSH sessions IDs are on the same line as the string `New session`, and then we can grep out the time from the last question:
```
grep auth.log -e "New session" | grep "6:32"
```
## Part 5 - Q5: The attacker added a new user as part of their persistence strategy on the server and gave this new user account higher privileges. What is the name of this account?
* after the `root` user logs in, we see that there is a user with a conspicuous name that logs in next:
```
grep auth.log -e "New session"
```
## Part 6 - Q6: What is the MITRE ATT&CK sub-technique ID used for persistence by creating a new account?
* if we search the exact question, we are directed to this page:
```
https://attack.mitre.org/techniques/T1136/
```
* then we look up the sub-technique that pertains to creating a local account on the target
## Part 7 - Q7: What time did the attacker's first SSH session end according to auth.log?
* we can use this command to get only the `session closed` messages for ssh, then get only the `root` accounts entries:
```
grep auth.log -e "session closed" | grep ssh | grep root
```
## Part 8 - Q8: The attacker logged into their backdoor account and utilized their higher privileges to download a script. What is the full command executed using sudo?
* we can see the `wtmp` entries for sudo with the cyberjunkie account with this command:
```
grep auth.log -e "sudo: cyberjunkie"
```
