# URL
https://play.picoctf.org/practice/challenge/8
# concept
* SQL injection, auth bypass
* strange input encryption
* the login page in this challenge is only looking for a password
* when we look at the POST request for the login, we see that our request includes a `debug` parameter, which is initially set to 0, so we can set it to 1 to see the SQL queries being sent
* when we can see the SQL queries that are sent, we see that all alphbetical input is being transformed before being used by the SQL database
* the transformation on the alphabet characters is ROT13, which we need to bear in mind while we're doing SQL injection
# method of solve
* send the standard SQL auth bypass payload, but encrypt the `or` portion of the payload with ROT13 beforehand
* so: `' or 1=1 -- ` becomes `' be 1=1 -- `
