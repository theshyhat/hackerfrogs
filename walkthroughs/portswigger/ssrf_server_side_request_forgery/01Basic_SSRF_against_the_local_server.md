# URL
https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-localhost
# Concept
* simple SSRF attack through a POST URL parameter
# Method of solve
* load up the lab in Burp Suite browser
* nagivate to any product page
* click on the `Check Stock` button
* lookup the POST request in the Burp Suite HTTP history tab
* send the POST request to the Burp Suite Repeater tool
* change the POST body data to this:
```
stockApi=http://localhost/admin
```
* send the request, and we see that we have access to the admin panel
* send the request again with the following body data to solve the lab:
```
stockApi=http://localhost/admin/delete?username=carlos
```
