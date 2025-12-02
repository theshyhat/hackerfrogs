# URL
https://tryhackme.com/room/phishing-aoc2025-h2tkye9fzU
# Concept
* Phishing
# Method of solve
* we're going to assume we're working from the AttackBox for this challenge
* we need to use this command to enter the directory with the script we're going to run:
```
cd ~/Rooms/AoC2025/Day02
```
* now we can run the `server.py` program:
```
./server.py
```
* this sets up a web server on our AttackBox which can be used for phishing
* if we can send an email to an employee of the TBFC company with a link to this page, we could potentially capture their credentials
## Using the Social Engineer Tookit (SET)
* we can use the follwing command to start the tool on the command line:
```
setoolkit
```
* now we can select `1` to conduct `Social-Engineering Attacks`
* then select `5` to do a `Mass Mailer Attack`
* then select `1` to do `E-Mail Attack Single Email Address`
* input `factory@wareville.thm` as the email address
* then select `2` to `Use your own server or open relay`
* input `updates@flyingdeer.thm` as the sender address
* input `Flying Deer` as the sender name
* input nothing for the `Username for open-relay`
* input nothing for the `Password for open-relay`
* input `<YOUR_VICTIM_MACHINE_IP>` for `SMTP email server address`
* input `25` for `Port number for the SMTP server`
* input `no` for `Flag this message as high priority`
* select `n` for `Do you want to attach a file`
* select `n` for `Do you want to attach an inline file`
* input `Shipping Schedule Changes` for `Email subject`
* select `p` for `Send the message as HTML or plain`
* type in the following message as the phishing email body:
```
Hello! The current schedule needs to be changed to accomodate the new season. Please confirm the schedule at this webpage: http://10.66.99.88:8000
END
```
* make sure to type `END` on a newline by itself
## Q1 - What is the password used to access the TBFC portal?
* we should receive something similar to the following on our `server.py` program:
```
Captured -> username: admin    password: unranked-wisdom-anthem    from: 10.66.179.129
```
* note that the IP address is going to be different
## Q2 - What is the total number of toys expected for delivery?
* login to the company website at this address:
```
http://<IP_ADDRESS_NOTED_FROM_Q1_ANSWER>
```
* we're not logging in at the `admin` user, but rather the `factory` user
```
username factory : password unranked-wisdom-anthem
```
* after logged in, click on the `Urgent: Production & Shipping Request - 1984000 Units (Next 2 Weeks)` email
