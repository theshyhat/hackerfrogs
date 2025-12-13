# URL
https://play.picoctf.org/practice/challenge/506
# Concept
* disk image forensics
* extracting disk partitions from a multi-partition file
# Method of solve
* unzip the image
* we need to isolate the Linux partition from the other data in the image file
* we can get the relevant info with the `fdisk` command
```
fdisk -l disko-2.dd
```
* this lets us know that the offset for the Linux partition is `2048`, and the length of the partition is `51200`
* we also need to know the sector size, which is `512` bytes
* with this info we can run the `dd` command which extracts the Linux partition from the rest of the image:
```
sudo dd if=./disko-2.dd of=./disko2.img skip=2048 count=51200 bs=512
```
* now we can run `strings` to get the flag
```
strings disko2.img | grep pico
```


