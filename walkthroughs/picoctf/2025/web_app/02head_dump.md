> We are told that we're supposed to locate an endpoint that that generates files holding the server's memory. When we look at the webpage, there's a link that leads to API documentation. On that page, there's a /headdump endpoint which downloads a file...
```
curl http://verbal-sleep.picoctf.net:58649/heapdump | grep 'picoCTF{'
```
