# URL
https://portswigger.net/web-security/ssrf/lab-ssrf-with-blacklist-filter
# Concept
* SSRF
* bypassing SSRF filters
# Method of solve
* this is similar to the previous SSRF labs
* use the Burp Suite browser to access the vulnerable app
* go to any product page and press the `Check stock` button
* go to the Burp Suite HTTP history tab and send the POST request to `/product/stock` to the Burp Repeater tool
* modify the contents of the POST body to resemble the following
```
stockApi=http://lOcAlHoSt/ADMIN?productId%3D5%26storeId%3D1
```
* the way we evade the filter in this app is using Alternating Caps case, `lIkE tHiS`
* the reason why is works is because the deny-list is probably filtering on words like `localhost` or `LOCALHOST`, but doesn't have an entry for `lOcAlHoSt`
*  the same for the word `admin` or `ADMIN`, versus `aDmIn`
*  so we're able to acces the admin panel. All we need to do now is delete the `carlos` user, we can do by sending a POST request with the following POST body:
```
stockApi=http://lOcAlHoSt/ADMIN/delete?username=carlos%26productId%3D5%26storeId%3D1
```
