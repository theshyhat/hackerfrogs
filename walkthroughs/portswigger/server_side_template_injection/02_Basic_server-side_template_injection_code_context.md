# URL 
https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-basic-code-context
# Concept
* SSTi with code context
# Method of solve
* we are able to set our preferences after we login to the app
* one of the preferences is to set our user's nickname, which will be output on blog posts that our user publishes
* after setting our `Preferred Name` to `Nickname` in the app and clicking the button we can access that POST request in Burp Suite history
* it look a POST request to this endpoint: `POST /my-account/change-blog-post-author-display`
* in the POST data, we see a parameter called `blog-post-author-display`, and we can inject SSTI payloads into its value
* we are told that the templating engine being used is Tornado, which is a Python templating engine
* we can use this payload to confirm the SSTI vulnerability:
```
{{7*7}}
```
* because it works, we can move to an RCE payload
```
{{ __import__("os").popen("whoami").read() }}
```
* and because this works, we can delete the `carlos` user's file `morale.txt` with this payload to complete the lab
```
{{ __import__("os").popen("rm /home/carlos/morale.txt").read() }}
```
