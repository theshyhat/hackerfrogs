# URL
https://ringzer0ctf.com/challenges/20
# Concept
* disk image forensics
# Method of solve
* download the task zip file and unzip it
* this resulting file represents a Linux filesystem image which can be mounted, but we shouldn't
* instead we inspect it using the `Sleuthkit` tools
* first we see what kind of filesystem is being used with the `fsstat` command:
```
fsstat 86b265d37d1fc10b721a2accae04a60d
```
* this lets us know that the filesystem being used is `ext2`, which we can feed into the next command, `fls`, which will let us know which files exist in the image:
```
fls -r -f ext2 86b265d37d1fc10b721a2accae04a60d
```
* from the output we see that there is a `secret.txt` file, but it doesn't have a valid inode number
* we can try to see if the deleted file exists in the `OrphanFile` directory, which contains unlinked files that have not been overwritten
```
icat -f ext2 86b265d37d1fc10b721a2accae04a60d 12
```
* that's it!
