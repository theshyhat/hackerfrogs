# URL
https://training.olicyber.it/challenges#challenge-34
# Concept
* reverse engineering
# Method of solve
* when we inspect the HTTP source for the login page, there reference to a `default.js` page
* there is the code which defines the correct username and password on this page
```
var username_field;
var password_field;

var s3cr37 = 'ML4czctKUzigEeuR';

window.onload = (event) => {
  username_field = document.getElementById('username');
  password_field = document.getElementById('password');
};

function login_check() {
  if (
    username_field.value === 'admin' &&
    AES_decrypt('U2FsdGVkX1/JEKDXgPl2RqtEgj0LMdp8/Q1FQelH7whIP49sq+WvNOeNjjXwmdrl', s3cr37) ===
      password_field.value
  ) {
    // Correct login!
```
* we can run this command in the web browser console
```
console.log(AES_decrypt('U2FsdGVkX1/JEKDXgPl2RqtEgj0LMdp8/Q1FQelH7whIP49sq+WvNOeNjjXwmdrl', s3cr37))
```

