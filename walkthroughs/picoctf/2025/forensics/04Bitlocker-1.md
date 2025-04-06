> We download the file, and we need to extract the password hash from the .dd file:
```
bitlocker2john -i bitlocker-1.dd > bitlocker.hash
john --wordlist=/usr/share/wordlists/rockyou.txt bitlocker.hash
```
> While the password is cracking, we can install the software to mount the drive and access the disk image:
```
sudo apt install libbde-utils
sudo mkdir /mnt/bitlocker
sudo bdemount -p 'jacqueline' bitlocker-1.dd /mnt/bitlocker
```
> From here, it's more convenient to become root to access the disk image:
```
sudo su
cd /mnt/bitlocker
strings bde1 | grep pico
```
Finis
