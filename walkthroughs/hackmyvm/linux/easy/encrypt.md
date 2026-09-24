# URL
https://hackmyvm.eu/machines/machine.php?vm=Encrypt
# Concepts
* inspecting SSL/TLS certificates
* taking note of Linux capabilities
# Method of solve
## Starting Scans
* we note that ports 22 and 443 are open
## Initial Access
* when we visit the webpage, we see that there are credentials embedded in the self-signed SSL certificate for the site
* we use those to login
## Privilege Escalation
* there is are extra capabilities associated with the ruby binary:
  * unfortunately the regular commands we'd use to enumerate capabilities are not available, so we use `linpeas`
```
/usr/bin/ruby3.3 cap_setuid=ep
```
* we can use ruby to escalate privileges, which is highlighted on this page:
  * `https://gtfobins.org/gtfobins/ruby/#shell`
* use this command to become root:
```
ruby -e 'Process::Sys.setuid(0); exec "/bin/sh"'
```
* finis


