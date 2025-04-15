# url
https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses
# objective
Login to the web app after brute forcing a valid credential set
# method of solve
1) Use the Burp Suite browser and try to login to the app via the My Account link.
2) Locate the POST request in the Burp Suite HTTP History tab
3) Save the request by right-clicking and selecting "copy to file", saving the file as `request.txt`
4) Modify the request.txt file contents, setting the username value to `FUZZ`
5) Use Ffuf to determine a valid username
```
ffuf -mc all -request request.txt -w ./usernames.txt
ffuf -mc all -request request.txt -w ./usernames.txt -fs 3140
```
6) Note that one request has a different response size, then substitute that name in for `FUZZ` and set the password value to `FUZZ`
7) Use Ffuf to determine a valid password
```
ffuf -mc all -request request.txt -w ./passwords.txt
ffuf -mc all -request request.txt -w ./passwords.txt -fs 3142
```
8) Use the credential set to login to the application
> Finis
