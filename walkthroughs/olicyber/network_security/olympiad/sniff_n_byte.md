# URL

# Concept
* following TCP streams
* hex to ASCII conversion
# Method of solve
* if we follow the TCP stream, we see one stream which contains a strings of hexadecimal bytes
* we can also find this packet if we search for the TCP PSH flag: `tcp.flags.push == 1`
* these bytes need to be cleaned up a bit and converted to ASCII:
```Bash
echo -n 'bytes' | sed 's/0x//g' | xxd -r -p
```





