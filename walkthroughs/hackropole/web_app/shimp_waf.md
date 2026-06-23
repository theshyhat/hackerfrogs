# URL
https://hackropole.fr/en/challenges/web/fcsc2026-web-shrimp-waf/
# Concept
* PHP filter bypass
# Method of solve
* after starting up the Docker container, navigate to the container's IP in our web browser
* on the landing page of the web app, there is a link that shows us the PHP code of the app
```php
<?php
if(isset($_GET["source"])) {
    die(highlight_file(__FILE__));
}

if (isset($_SERVER['QUERY_STRING']) &&
    stripos($_SERVER['QUERY_STRING'], 'shrimp_flag') !== false) {
    die('Blocked by Shrimp WAF 1.0');
}

if(isset($_GET["shrimp_flag"]) && $_GET["shrimp_flag"] === "Bye ShrimpWAF") {
    die(getenv("FLAG"));
}
?>
```
* this code indicates that we can obtain the flag if we supply a specific URL parameter (shrimp_flag) with a specific value (Bye ShrimpWAF)
```php
if(isset($_GET["shrimp_flag"]) && $_GET["shrimp_flag"] === "Bye ShrimpWAF") {
    die(getenv("FLAG"));
}
```
* the problem is that there is a filter in place that looks for the specific substring `shrimp_flag` in the GET request, and if it is present, then we receive an error message:
```php
if (isset($_SERVER['QUERY_STRING']) &&
    stripos($_SERVER['QUERY_STRING'], 'shrimp_flag') !== false) {
    die('Blocked by Shrimp WAF 1.0');
}
```
* the function that is doing the filtering is `stripos()`, which returns the position where the substring is found
* the way we can bypass the filter is by not including the literal subtring `shrimp_flag`
  * the way we do this is by replacing the underscore `_` in the string with a dot `.`
  * the reason why this works is because PHP converts dots and spaces in URL parameters into underscores during parsing
  * so we can send this URL to get the flag:
```
http://172.20.0.2/?shrimp.flag=Bye%20ShrimpWAF
```





