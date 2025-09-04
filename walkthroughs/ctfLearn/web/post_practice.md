# URL
https://ctflearn.com/challenge/114
# Concept
* making POST requests
# Method of solve
* look at the specified webpage
* note that there are credentials in the HTTP ccomments
* use a curl command to make a POST request to the web app which includes those credentials
```
curl -X POST -v http://165.227.106.113/post.php -d "username=admin&password=71urlkufpsdnlkadsf"
```
