# URL
https://play.picoctf.org/practice/challenge/236
# concept
* JWT manipulation
* the `alg:none` vulnerability (CVE-2015-2951) The alg=none signature-bypass vulnerability
# method of solve
* we login as our test user with these credentials: `test:Test123!`
* we grab the cookie that is generated on login, which is a JWT
* we pass that cookie to the following website: `https://token.dev/`
* we modify the JWT by specifying `alg:none` and `"role": "admin"`
* because setting the `alg:none` deletes a chunk of the JWT, we need to append a dot `.` to the end of the JWT to make it valid
* feed the new JWT value to the web app
* done
