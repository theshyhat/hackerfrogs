# URL
https://hack.arrrg.de/challenge/100
# Category
Web App Hacking
# Concept
* User Agent HTTP headers
# Method of solve
* spoofing HTTP headers, specifically, the `User-Agent` header
* use `curl` to spoof the `User-Agent` header to get the answer to the challenge
```
curl -b "connect.sid=s%3AUPwsbqPvo_3vmC_m8_aVc7tV1aWUL5JK.myej%2B9UzZ7B0hy907w7jfyrBKvxH4aLq%2BBWHPwZ%2Bujc;htw_language_preference=en" -v https://hack.arrrg.de/challenge/100 -A "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)"
```
