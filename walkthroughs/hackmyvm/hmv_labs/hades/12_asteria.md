# username
asteria
# password
hawMVJCYrBgoDAMVhuwT
# mission contents
The user astraea believes in magic.
# method of solve
There's a `sihiri_old.php` file in the home directory. The contents are as follows:
```
<?php
$pass = hash('md5', $_GET['pass']);
$pass2 = hash('md5',"ASTRAEA_PASS");
if($pass == $pass2){
print("ASTRAEA_PASS");
}
else{
print("Incorrect ^^");
}
?>
```
The funny way that PHP handles data types, also known as the `type juggling` vulnerability, when applied to hash comparisons, this can result in magic hashes that match any md5 hash. More info can be found here:
`https://github.com/spaze/hashes/blob/master/md5.md`.
```
cat sihiri_old.php
curl http://localhost/sihiri.php?pass=240610708
```
