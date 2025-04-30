# Challenge URL
https://play.picoctf.org/practice/challenge/376
# Vulnerability / Key Concept
XXE (External XML Entities)
# Method of Solve
> From the tags on the challenge, we know we're dealing with XXE, External XML Entities
> Since we will be looking for POST requests to find the XML in the request body, we need to use Burp Suite and send requests through the Burp browser and replay the POST requests
> When we access the landing page of the web, we see that there are some buttons we can press. We press one of the buttons and check out the HTTP history in Burp
> The POST request for the /data endpoint has XML content, and we can use this payload to create an additional entity named "example" and have it output the contents of the /etc/passwd file, which is the objective of the challenge:
```
<?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE foo [<!ENTITY example SYSTEM "/etc/passwd"> ]>
  <data>
    <ID>
      2&example;
    </ID>
  </data>
```
