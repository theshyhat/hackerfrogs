# username
bandit27
# password
upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB
# level description
* There is a git repository at ssh://bandit27-git@localhost/home/bandit27-git/repo via the port 2220. The password for the user bandit27-git is the same as for the user bandit27.
* Clone the repository and find the password for the next level.
# method of solve
* there is a github repo hosted on the ssh service on the localhost, so we have to use ssh to access it
* use this command (we need to be located in a publicly writable directory first)
```
git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
```
* after that, the password is in the README file in the repo
```
cd repo
cat README
```
