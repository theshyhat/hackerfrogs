# username
bandit15
# password
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
# objective
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption.
# method of solve
We can use OpenSSL to send the password:
```
echo '8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo' | openssl s_client -quiet -connect localhost:30001
```

