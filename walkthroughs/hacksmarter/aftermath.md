# URL

# Concept
* STMP username enumeration
* login brute force with CSRF bypass
# Method of solve
## Starting Scans
* open ports: `22,25,80`
* we've been provided a password list as well as a username list that we can use for enumeration / brute-forcing
* directory busting reveals an interesting endpoint:
```
dirsearch -u http://kali
```
* this reveals the `/roundcube/index.php` endpoint. We'll be looking at this later
## Initial Access
* we use a tool from the Metasploit framework to enumerate valid usernames on the SMTP service:
```
msfconsole
use auxiliary/scanner/smtp/smtp_enum
set rhosts 10.1.28.48
set USER_FILE names.txt
run
```
* this gives us two valid usernames, `kali`, and `maria`
* we know there's a Roundcube webmail endpoint, and now that we have reduced the valid usernames to two, we can attempt to brute-force the login
* since the login mechanism is CSRF protected, we can't do a normal login brute-force attack
### Roundcube Brute-Force With Tool 
* there's a specialized tool just for password spraying Roundcube
```
https://github.com/robotshell/cubeSpraying
```
* after cloning the repo, we run the tool
```
python cubeSpraying.py -v -u http://kali/roundcube/ -U ../users.txt -P ../passwords.txt
```
* we find the credentials `maria:1qaz2wsx`
### Roundcube Brute-Force With Python
* from looking at the login flow, the CSRF token is obtained from the GET request to the `index.php` endpoint as the `request_token` JSON value
* we need to extract that value and supply CSRF token as the `_token` value the following in the POST request for login at the `/roundcube/?_task=login` endpoint:
```
_token=CSRF_TOKEN&_task=login&_action=login&_timezone=Pacific%2FHonolulu&_url=&_user=USERNAME&_pass=PASSWORD
```
* this Python script will get the valid CSRF token from the `index.php` page, then make the POST request with that token to the `/roundcube/?_task=login` endpoint
* the script waits for 10 seconds between each request with the same username, to avoid lockouts
* we run the script with the URL of the `index.php` page, the username file, and the password file as arguments
### Roundcube Brute-Force With Burp Suite
* to perform the brute-force attack with Burp Suite, we need to:
1) Setup a macro to extract the CSRF token from the `index.php` endpoint
2) Create a session-handling rule that uses the macro when making requests to the authentication endpoint
3) Perform a Burp Intruder attack using the round usernames and the passwords
#### Setting up the Burp Suite Macro
1) Go to Burp Settings
2) Click on the `Sessions` tab on the left-hand menu
3) Scroll down to `Macros` and click `Add`
4) In the `Macro Recorder` window, select the GET request which contains the CSRF token, `/roundcube/index.php`, then click `OK` at the bottom of the window
5) In the `Macro Recorder` window, select the GET request, then click on the `Configure item` button on the right side of the window
6) In the new window, click `Add`
7) In the `Parameter Name` field, enter the name of the CSRF value we want to send with requests, in this case `_token`
8) In the response portion of the window, search for the CSRF token value itself and highlight it with the mouse (in this case it's right after the key `request_token` ), then click on the `OK` button at the bottom of the window
9) Click `OK` at the bottom of the next window down
10) Click `OK` on the next window down, the `Macro Edtitor`
#### Create a Session-handling Rule
1) In `Session -> Settings`, scroll up to the `Session handling rules` section, and click `Add`
2) In `Rule Actions`, click `Add`, then select `Run a macro` and click on the name of the macro you created, then click on the `OK` button at the bottom of the window
3) At the top of the window, click on the `Scope` tab, in the `URL Scope` section, click on `Use custom scope`, then under `Include in scope`, click `Add`
4) Paste in the URL where we will be sending the login post requests `http://kali/roundcube/`, then click `OK`
#### Perform a Burp Intruder Attack
1) In the `Proxy -> HTTP History` tab, click on the POST login request to Roundcube, then right-click and select `Send to Intruder`
2) In the request window, highlight the value after `_user=` and click on the `Add` button
3) highlight the value after `_pass=` and click on the `Add` button
4) At the top of the window, where it displays `Sniper Attack`, click on the text and select `Cluster Bomb Attack`
5) Copy all of the passwords from the `passwords.txt` file, then in the `Payloads` section of the window on the right, click on the `Paste` button under the `Payload configuration` section
6) At the top of the `Payloads` section, click on the `Payload position` dropdown window and select the item starting with `1`
7) In the `Payload configuration` section, click on the field beside the `Add` button and type in the first user name, `maria`, then click `Add`
8) Repeat the process above for the `kali` user
9) Click on the `Start attack button`
10) The attack will go very, very slowly, But eventually, we'll see one request with a response code of `302` instead of `403`. That payload combination are the correct credentials for the Roundcube app
11) 
