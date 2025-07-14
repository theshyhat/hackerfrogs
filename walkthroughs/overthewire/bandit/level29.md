# username
bandit29
# password
4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7
# objective
* There is a git repository at ssh://bandit29-git@localhost/home/bandit29-git/repo via the port 2220. The password for the user bandit29-git is the same as for the user bandit29.
* Clone the repository and find the password for the next level.
# method of solve
* we need to git clone this level's repo as well
```
git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
```
* we look at the git logs for the master branch, and they indicate that the README.md file was redacted
* we need to take a look at the different branches for the repo
```
git branch -a
```
* This output indicates there more than one branch that we can look at. We want to checkout the dev branch
* We can switch branches in Git with the following command
```
git checkout dev
```
* We can now take a look at the logs for this branch
```
git log -p
```
* The password is here
