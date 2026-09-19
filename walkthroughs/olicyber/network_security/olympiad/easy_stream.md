# URL
https://training.olicyber.it/challenges#challenge-23
# Concept
* following HTTP streams
# Method of solve
* filter the packets by the HTTP protocol
  * the flag appears in stream number 10
* the other way to find the flag is to filter the packets by HTTP packets that contain the string `flag`:
```
http && frame contains "flag"
```


