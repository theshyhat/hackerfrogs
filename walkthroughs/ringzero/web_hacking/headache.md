# URL
https://ringzer0ctf.com/challenges/43
# Concept
* HTTP methods
# Method of solve
* this challenge title implies that we have use the HTTP HEAD method to access the page
* we can use the `curl` program to access the webpage using the HEAD method
```
curl -b "PHPSESSID=<your_cookie_value_here>" -I HEAD -v https://ringzer0ctf.com/challenges/43
```
