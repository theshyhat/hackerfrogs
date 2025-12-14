# URL
https://tryhackme.com/room/container-security-aoc2025-z0x3v6n9m2
# Concept
Docker container operations
# Method of solve
## Q1 - What exact command lists running Docker containers?
The answer is `docker ps`
## Q2 - What file is used to define the instructions for building a Docker image?
The answer is `dockerfile`
## Q3 - What's the flag?
* on the CLI machine, use this command to interact with the `deployer` container
```
docker exec -it deployer bash
```
* there is a reset script in the top level directory, and we run this command to run it:
```
/recovery_script.sh
```
* lastly, we can read the flag
```
cat /flag.txt
```
## Q4 - Bonus Question: There is a secret code contained within the news site running on port 5002; this code also happens to be the password for the deployer user! They should definitely change their password. Can you find it?
* in the AttackBox, navigate to the following webpage in the AttackBox's Firefox browser:
```
http://<MACHINE_IP>:5002
```
Notice that there are three words highlighted in the article on the webpage. Put these three words together to answer the question.
