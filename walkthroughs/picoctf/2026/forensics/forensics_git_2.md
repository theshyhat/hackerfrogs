# URL
https://learn.cylabacademy.org/library/707
# Concepts
* Git repo reconstruction
* Git commit recovery
# Method of solve
First, we get the locations of the partitions in the disk iamge:
```
mmls disk.img
```
Then we extract the filesystem:
```
tsk_recover -f ext4 -e -o 1140736 -i raw -v disk.img .
```
Now to locate the Git repo
```
find . -name ".git"
cd ./home/ctf-player/Code/killer-chat-app/
```
There is no ".git/refs" directory, so can re-create them
```
mkdir -p .git/refs/heads && mkdir -p .git/refs/tags
```
After creating these directories, we get a different error message when we try Git log:
```
git log -p
```
We need to get the commit hashes for the repo, which we can find in the `.git/logs/refs/heads/master` file:
```
cat .git/logs/refs/heads/master | cut -d' ' -f2
```
Now we can update the references in the repo:
```
git update-ref refs/heads/master 01533f718556a0e59f1467dae4fa462eed82c2a1
```
Finally, we can get the commit history and complete the challenge:
```
git log -p
```
