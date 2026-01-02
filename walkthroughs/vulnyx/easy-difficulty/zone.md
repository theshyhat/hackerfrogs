there are 3 ports open on the server, 80, 53, and 22

Port 80 contains a robots.txt file, which indicates a domain, securezone.nyx, which we can add to our /etc/hosts file

With port 53 is DNS and a domain name can try to zone transfer to determine which subdomains exist on the server:

dig axfr @10.0.2.59 securezone.nyx

We find that there are several subdomains that exist according to the DNS zone transfer records. We can add these to the /etc/hosts file. The one we want to pay attention to is the upl0ads subdomain

When we directory fuzz the upl0ads subdomain, we see that there is an uploads directory.

On investigation, we see that the landing page for the upl0ads subdomain is a file upload endpoint, but we don't know what file extensions are allowed.

We can use a script to enumerate which file extensions are allowed:

https://github.com/theshyhat/ctf_documents/blob/main/scripts/web_hacking/upload_extension_check.sh

The script is able to determine the allowed file extension, which is phar, a type of php file

So we obtain a php reverse shell file and adjust it, then rename it so that the file extension is .phar

We then upload the file to the app, and because we know there is an uploads directory, we can guess at the filepath for the uploaded reverse shell

We need to make sure to run bash before we start out netcat listener

bash
nc -nlvp 443

After gaining a shell on the box, we need to upgrade the shell fully

python -c 'import pty;pty.spawn("/bin/bash")'
ctrl-z
stty -a
stty raw -echo
fg
export SHELL=bash
export TERM=xterm-256color
stty rows X columsn Y
clear

We now have a full-featured shell to use

Using sudo -l, we find that the www-data user has sudo permissions with the ranger program as the hans user. Ranger is a text-based file manager

sudo -u hans ranger

Once in the program:
!/bin/bash

We now have a shell as the hans user. The hans user, has sudo access to the lynx program, which is a text-based web browsing program.

sudo lynx

Then ! will bring you to the shell, which is a root shell

Finish
