# URL
https://learn.cylabacademy.org/library/706
# Concepts
* extracting filesystems from disk images
* Git commit history enumeration
# Method of solve
* first, list out the disk partitions on the disk image
```
mmls disk.img
```
* we can list out the files
```
fls -p -r -o 1140736 disk.img
```
* but to interact with the Git repo, we'll need to extract the filesystem to our local system
```
tsk_recover -f ext4 -e -o 1140736 -i raw -v disk.img .
```
* locate the Git repo, then enter the directory and use the Git log command to retrieve the commit histories
```
find . -name ".git"
cd ./home/ctf-player/Code/secrets/
git log -p
```
