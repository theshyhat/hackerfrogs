# URL
https://play.picoctf.org/practice/challenge/443
# concept
* no SQL injection
# method of solve
* the challenge gives us the source code for the app
* when we read the source code, we see that there is vulnerable code in the `server.js` file
* the vulnerable code is here:
```
const user = await User.findOne({
  email: email.startsWith("{") && email.endsWith("}") ? JSON.parse(email) : email,
  password: password.startsWith("{") && password.endsWith("}") ? JSON.parse(password) : password
});
```
* Problem 1: Arbitrary JSON Parsing
* The code checks if the email/password starts with { and ends with } and if so, parses it as JSON. This allows attackers to inject MongoDB query operators.
* Problem 2: No Input Validation
* There's no validation of the parsed JSON content, allowing direct injection of query operators.
* The payload that will bypass the login should be put into the password value is this:
```
"{\"$ne\": \"\"}"
```
* the key point of this payload is the `$ne` which returns not equal
* Which translates to "find a user where email is not empty and password is not empty" - likely matching all users in the database.
