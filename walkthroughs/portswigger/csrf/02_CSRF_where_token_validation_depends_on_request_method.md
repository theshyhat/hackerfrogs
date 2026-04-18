# URL
https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-validation-depends-on-request-method
# Concept
* bypassing CSRF where the method of the request determines if the CRSF token is used
# Method of solve
* open up the lab in the Burp Suite browser
* login to the app with our provided credentials `wiener:peter`
* go to the `My account` page
* and enter any email you like into the `email` field, then click on `Update email`
* go to Burp Suite and click on the `Proxy` -> `HTTP history` tab
* locate the POST request made to the `/my-account/change-email` endpoint
* right-click on the request window and select `Send to repeater`
* we are told that this app will ignore the CSRF token if the request is made with another HTTP method
* so we change the request method from POST to GET, and then include the email parameter as an URL parameter `?email=email_here`
* after the request has been modified, send the request and we should see that our email address for our user has been modified
* this confirms that the app fails to use the CSRF token if the request method is not POST
* so we can use the following payload for our exploit server body section
```
<img src="https://0a02007f03b4068282781a8c00cc00ce.web-security-academy.net/my-account/change-email?email=pwned@evil-user.net">
```
* note that we need to change the URL to reflect our lab environment and make sure the endpoint is `/my-account/change-email`, and lastly, that we include a URL parameter `?email=pwned@evil-user.net`
* click on `Send exploit to victim` and we should be done
