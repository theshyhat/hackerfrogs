# Vulnerabilities
* sensitive data included in web page source code
* user name disclosure via file names
* privilege esclation via binaries that run system commands
# Method of solve
* there is a password encoded in Brainf*ck on the index page in the HTTP comments
* in the /images directory there is a reference to a username `agua`
* once in, the `agua` user has sudo permissions with the `bettercap` program, which can run systems commands
* once running the `bettercap` program, use `!command` to run a command, e.g, `!whoami`
* we created a SUID binary version of the Bash command in the /tmp directory and used it to gain a root shell
```
cp /bin/bash /tmp/bash
chmod u+s /tmp/bash
/tmp/bash -p
```
