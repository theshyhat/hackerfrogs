There's only port 80 open

Through dirbusting, we found there's an explorer endpoint

At the `explorer` endpoint, there's an old manager app being used called `extplorer`

We can login using default credentials `admin:admin`

The app has unrestricted file upload functionality

So we upload a webshell, and go to town

Once on the box, we see that we have the following sudo permissions

```
(ALL : ALL) SETENV: NOPASSWD: /usr/local/bin/slo-generator
```

This means we can set the environment variables for Python, which includes which directory it imports modules from. We need to know which Python modules it imports.

In this github repo, there's a lot of info about the tool

`https://github.com/google/slo-generator`

There are a number of different import files in this file:
https://github.com/google/slo-generator/blob/master/slo_generator/cli.py

This indicates to us that we should use a module like `click.py` or `logging.py`


Write the following to a file named `click.py`

```
import os
import sys
print("Hijacked click module!")
os.setuid(0)
os.setgid(0) 
os.system("/bin/bash -p")
```

Then run the following command
```
sudo PYTHONPATH=/tmp /usr/local/bin/slo-generator --help
```
the flag files are located in the following locations

/root
/home/ETSCTF
