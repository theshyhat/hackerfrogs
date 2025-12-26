# URL
https://hack.arrrg.de/challenge/351
# Category
General
# Concept
* base64 encoding
# Method of solve
* the string is encoded using the base64 system
* we can copy the whole string and decode it using a Linux command like the following
```
echo -n '<paste in base64 string here>' | base64 -d
```
* or we can use this website to decode it: `https://www.base64decode.org/`
