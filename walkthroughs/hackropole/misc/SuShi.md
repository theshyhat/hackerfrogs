# URL
https://hackropole.fr/en/challenges/misc/fcsc2020-misc-sushi/
# Concept
* connecting to a server via SSH
# Method of solve
* this challenge teaches us to connect local Docker container via SSH
* after the Docker container is started, run the SSH command to connect via port 2222:
```
ssh -p 2222 ctf@localhost
```
* the password for our user is `ctf`
* once on the server, we take a look at the directory contents with:
```
ls -la
```
* and there is a `.flag` file here
```
cat .flag
```



