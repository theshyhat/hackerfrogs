# URL
https://ctflearn.com/challenge/957
# Concept
* looking for text strings
* base64 encoding
# Method of solve
* use the `strings` command to pull out readable text:
```Bash
strings 957
```
* the output includes a base64-encoded string, that we can decode with the following command:
```Bash
echo 'Q1RGbGVhcm57KV8xbDB3M3kwVW0wMG15MTIzfQ==' | base64 -d
```

