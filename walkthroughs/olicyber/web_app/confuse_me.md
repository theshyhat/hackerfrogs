# URL
https://training.olicyber.it/challenges#challenge-54
# Concept
* PHP magic hashes
* PHP loose comparison operators
* PHP type juggling
# Method of solve
* the app code looks like this:
```
<?php

if (isset($_GET["s"])) {
  highlight_file("index.php");
  exit;
}

$flag = getenv("FLAG");

echo "
<html>
<body>
  <form>
  Input: <input name=input />
  </form>

  <a href='?s'>Sorgente disponibile qui</a>.<br/>
</body>
</html>
";

if (isset($_GET['input'])) {
  $user_input = $_GET['input'];
      
  if ($user_input == substr(md5($user_input), 0, 24)) {
    echo "Ce l'hai fatta! Ecco la flag: $flag";
  } else {
    echo "Nope nope nope";
  }
}
```
* the code is doing a loose comparison between the `$user_input` value and the md5 hash of the `$user_input` value
```
if ($user_input == substr(md5($user_input), 0, 24)) {
    echo "Ce l'hai fatta! Ecco la flag: $flag";
```
* due to loose comparison `==`, this app is vulnerable to PHP type juggling and magic hashes
* in order to have the comparison return true, we need a string value that also conforms to the `0e`, then numbers for the rest of the string, like other PHP magic strings
* this value: `0e215962017` qualifies
