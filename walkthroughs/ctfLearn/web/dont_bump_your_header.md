# URL
https://ctflearn.com/challenge/109
# Concept
* HTTP headers
* the HTTP User-Agent header
* the HTTP Referer header
# Method of solve
* access the website and see that it is looking for a specific User-Agent header
* in the HTTP comments, we see the name of the header we're supposed to use
* use `curl` to send a request with the appropriate header:
```
curl -H "User-Agent: Sup3rS3cr3tAg3nt" -v http://165.227.106.113/header.php
```
* but that doesn't get us the flag. They're also looking for a website where we came from, which is supposed to be `awesomesauce.com`
* the correct way to do this is to use the `Referer` header, which is usually used for logging purposes or for analytics
* this the correct `curl` command below:
```
curl -H "User-Agent: Sup3rS3cr3tAg3nt" -H "Referer: awesomesauce.com" -v http://165.227.106.113/header.ph
```

