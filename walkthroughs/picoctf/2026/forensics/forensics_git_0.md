# URL
https://learn.cylabacademy.org/library/705
# Method of solve
After downloading and unzipping the disk image file, we can use SleuthKit to scope it out
```
mmls disk.img
```
The partition with the offset 1140736 is the one we're looking for
```
fls -p -r -o 1140736 disk.img
```
We're told there is a git repo or something in here:
```
fls -p -r -o 1140736 disk.img | grep 'git'
```
From here, we can extract the entire partition with SleuthKit, then look inside afterwards
```
tsk_recover -f ext4 -e -o 1140736 -i raw -v disk.img .
```
Enter the directory with the Git repository, then:
```
git log
```
