# URL
https://labs.hackadvisor.io/en/challenges/pulseguard-rce-vm-sandbox-1
# Concept
* JavaScript VM module escape
* arbitrary JS injection
# Method of solve
* user the provided credentials to access the app `user@test.com / password123`
* observe that there are custom scripts in the `Monitors` section of the app
* we can create our own custom script monitor to read the flag file for the challenge, which we've been told is at `/root/flag.txt`
* go the Monitors tab and select "New Monitor"
* select "custom JavaScript" from the dropdown
* put the following code in the script:
```JavaScript
var result = this.constructor.constructor('return process.mainModule.require("fs").readFileSync("/root/flag.txt", "utf8")')();
console.log(result);
```
* click on `Create Monitor`
* click on the monitor
* click on `Run Now`
* you get the flag :D

