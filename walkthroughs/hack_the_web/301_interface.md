# URL
https://hack.arrrg.de/challenge/301
# Concept
* different HTTP methods
* using the DELETE method
# Method of solve
* we need to use the `DELETE` HTTP method with a specific endpoint, `/chal/chal301` to get the answer:
```
curl -X 'DELETE' -b 'htw_language_preference=en' https://hack.arrrg.de/chal/chal301
```



