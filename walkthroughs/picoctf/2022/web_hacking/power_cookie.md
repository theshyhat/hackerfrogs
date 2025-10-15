# URL
https://play.picoctf.org/practice/challenge/288
# Concept
HTTP Cookies
# Method of solve
* log into the app by clicking on the "continue as guest"
* go into your web browser `Web Developer Tools`, then click on the `Storage` tab, then on the `Cookies` storage for the website
* there will be a `isAdmin` cookie, set to `0`. Set it to `1`, then reload the page
