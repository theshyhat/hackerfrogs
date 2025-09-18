# URL
https://training.olicyber.it/challenges#challenge-47
# Concept
* PHP type juggling
# Method of solve
* the code for the blacklist is here:
```
<?php
	if(isset($_GET['richiesta'])) {
	  if (preg_match("/.*/i", $_GET['richiesta'], $match))  {
	    echo "No, mi dispiace non posso fare questo!";
		} else {
			echo "flag{TROVAMI}";
		}
	} else {
 	  echo "Fai una richiesta e provero a realizzarla";
	}
?>
```
* the PHP code is airtight, and we can't return anything because the regex will match everything we send to the app
* what we can do is use PHP type juggling to compare strings against arrays, and in earlier versions of PHP, this always returned true
* the string we're looking for is this:
`?richiesta[]=richiesta`
