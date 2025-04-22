# URL
https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-modifying-serialized-data-types
# objective
This lab uses a serialization-based session mechanism and is vulnerable to authentication bypass as a result. To solve the lab, edit the serialized object in the session cookie to access the `administrator` account. Then, delete the user `carlos`. You have access to the crendentials `wiener:peter`.
# method of solve
1) Login to the application with your provided credentials `wiener:peter`
2) We've been told that the session cookie contains serialized information, so we copy the cookie from the Web developer tools
3) Paste the cookie into a terminal and decode it using base64 (note that we replace the %3d pattern with the equals sign, since cookies use URL encoding):
```
echo -n 'Tzo0OiJVc2VyIjoyOntzOjg6InVzZXJuYW1lIjtzOjY6IndpZW5lciI7czoxMjoiYWNjZXNzX3Rva2VuIjtzOjMyOiJnY2Y5aGExbzNlc2ptcXY1ZWQzajhicTRvZmR2ODNkZyI7fQ==' | base64 -d
```
The output is a serialized object, and we want to modify it to ID us as the `administrator` user, but we also need to set the access token to false:
4) Echo out the modified cookie value, then base64 encode it:
```
echo -n 'O:4:"User":2:{s:8:"username";s:13:"administrator";s:12:"access_token";i:0;}' | base64 -w 0
```
5) Take the output of the command and replace the cookie value in the web browser, then refresh the page
6) We are now logged in as the `administrator` user, so we can delete the `carlos` user account from the `Admin Panel` page to complete the lab
