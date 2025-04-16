# url
https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-subtly-different-responses
# objective
Login to the web app after brute forcing a valid credential set
# method of solve
1) Use the Burp Suite browser and try to login to the app via the My Account link.
2) Locate the POST request in the Burp Suite HTTP History tab
3) Save the request by right-clicking and selecting "copy to file", saving the file as `request.txt`
4) Modify the request.txt file contents, setting the username value to `FUZZ`
5) Use Ffuf to determine a valid username. In this example, we need to filter on responses that don't include the message `Invalid username or password.`
```
ffuf -mc all -request request.txt -w ./usernames.txt -fr "Invalid username or password\."
```
6) Note that only one request is returned. Substitute that name in for `FUZZ` and set the password value to `FUZZ` in request.txt
7) Use Ffuf to determine a valid password. We need to filter on either the lines returned, or the status code
```
ffuf -mc all -request request.txt -w ./passwords.txt
ffuf -mc all -request request.txt -w ./passwords.txt -fl 65 | grep -v "Lines: 66"
ffuf -mc all -request request.txt -w ./passwords.txt -fs 200
```
8) Use the credential set to login to the application
> Finis
