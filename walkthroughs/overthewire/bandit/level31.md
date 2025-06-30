# name
bandit31
# password
fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy
# objective
* There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo via the port 2220. The password for the user bandit31-git is the same as for the user bandit31.
* Clone the repository and find the password for the next level.
* In the README file in the Git repo we see this message
```
This time your task is to push a file to the remote repository.

Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master
```
# method of solve
* create a writable directory to store the repo, enter the directory, then use the following command
```
git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo
```
* the `README.md` file has the contents described in the `objective` portion of this document, which means we need to commit and push a file to the repo to get the flag
```
echo 'May I come in?' >  key.txt
git add key.txt -f
git commit -m "Add key.txt file"
git push origin master
```
  
