# URL
https://tryhackme.com/room/race-conditions-aoc2025-d7f0g3h6j9
# Concept
* app race condition vulnerabilities
# Method of solve
* on the AttackBox, open the Burp Suite program
* after the program has fully started up, click on the settings gear on the right-hand side of the screen
* search for the term `browser`, then under the `Browser running` heading, click on the checkbox labeled `Allow Burp's browser to run without a sandbox`
* close the settings window
* then in the `Proxy` --> `Intercept` tab, toggle the `Intercept on` button so that it reads `Intercept off`
* in the same tab, click on the `Open browser` button on the right-hand side of the screen
* in the web browser that opens up, navigate to the `http://<MACHINE_IP>` endpoint
* login to the app using the following credentials: `attacker:attacker@123`
## Q1 - What is the flag value once the stocks are negative for SleighToy Limited Edition?
* in the web app in the Burp Suite browser, purchase one of the `SleighToy` items
* in Burp Suite, navigate to the `Proxy` --> `HTTP History` tab, and click on the POST request to the `/process_checkout` endpoint
* right-click on the Request window and select `Send to Repeater`
* click on the `Repeater` tab
* right-click on the `1 x` tab at the top of the tab and click on `Move Tab to Group` --> `Create tab group`
* right-click on the `1 x` tab and select `Duplicate tab`, then choose `15 times`
* click on the drop-down on the `Send` button and select `Send group in parallel`
* click on the `Send button`
* go back to the Burp Suite web browser to retrieve the flag
## Q2 - Repeat the same steps as were done for ordering the SleighToy Limited Edition. What is the flag value once the stocks are negative for Bunny Plush (Blue)?
* do the same process as question 1, but for the `Bunny Plush` item
