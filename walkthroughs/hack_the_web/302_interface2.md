# URL
https://hack.arrrg.de/challenge/302
# Concept
* using the `DELETE` method with an `Authorization` header
# Method of solve
* we're given essentially the same task as the previous challenge
* except we need to send a specific HTTP header with our request:
```
curl -X 'DELETE' -b 'htw_language_preference=en' -H 'Authorization: HTW theshyhat%E2%9A%BB26b1803e19a62c6363d2dfca1310debb' https://hack.arrrg.de/chal/chal302
```
* the value of the Authorization header is going to be different for each user
