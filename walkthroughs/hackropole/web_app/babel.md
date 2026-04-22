# URL
https://hackropole.fr/en/challenges/web/fcsc2020-web-babel-web/
# Concept
* PHP code analysis
* URL parameters / remote code execution
# Method of solve
* look at the landing page of the app
* look at its HTTP source - it contains a comment which references a URL parameter `?source=1`
* if we plug in that parameter, then we see the PHP source code for the page
* the app is using the `code` URL parameter as a PHP `system` function, which executes the parameter as an OS command
* using this, we can see that there is a `flag.php` file in the app's current directory
```
localhost:8000/index.php?code=ls -la
```
* using the same RCE method, we can read the `flag.php` file
```
http://localhost:8000/index.php?code=cat%20flag.php
```
* the flag is in the source, so view the source and we're finished



