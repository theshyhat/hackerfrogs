#!/bin/bash
/*
This script is used with the HackerFrogs AfterSchool Network hacking course,
and is meant to help teach hash cracking with the John the Ripper program.
Here are instructions on how to complete the exercise:

Step 1: Run the script
cd /tmp
wget https://github.com/theshyhat/hackerfrogs/edit/main/afterschool/06_network_hacking/cracking_practice.sh
chmod +x cracking_practice.sh
./cracking_practice.sh

Step 2: Crack the zip file hash
zip2john zip_crack.zip > zip.hash
john --wordlist=/usr/share/wordlists/rockyou.txt zip.hash

Step 3: Crack the Linux password hash
unshadow hackerfrog.passwd hackerfrog.shadow > hackerfrog.hash
john --wordlist=/usr/share/wordlists/rockyou.txt hackerfrog.hash

Step 4: Crack the SSH key hash
ssh2john id_rsa > id_rsa.hash
john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.hash

*/
echo 'frog{z1p_h@sh_cr4cked}' > zip_flag.txt
zip -P starwars zip_crack.zip zip_flag.txt
echo 'hackerfrog:x:1000:1000::/home/hackerfrog:/bin/bash' > hackerfrog.passwd
echo 'hackerfrog:$6$7M7YK/Hz6$JLORDQ8BtYLElqX5DEuVP6mSK7clZlOAD/t4MH4FwoQBkwsk41huec74BYmE5XzULrOmhw72ywQ1lhjafCt.q0:20105:0:99999:7:::' > hackerfrog.shadow
echo '-----BEGIN OPENSSH PRIVATE KEY-----                   
b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jdHIAAAAGYmNyeXB0AAAAGAAAABDWcnhzmm
R/3d0KNBMoYrcfAAAAEAAAAAEAAAEXAAAAB3NzaC1yc2EAAAADAQABAAABAQDYIe8H6sCq
/oDep7wmVjIILRA46qWK2DRk7PIy6fBr8qQaAnHsXYzHudCC+FzZ90hbd/w7G6bqcfwPbB
QjdA+4D06qxRGUyL5SZRnt+qeGN5z1dgBF69Gd1UjGIJ8AJBrKGOuMTbfeGhXaZN4V/7mb
epDVcNYruzb4QIKuS6NoVQX1DvAiDQNsMwoflmAUm5favqr6GNbBxHikWc/YbLLCLhtofI
nNZScbzSzYWsTpIWXjYUwissWjDbM/vTEEYc8LovrbFlS/eeLbI7XaF5XxLHJBoRT7fvLr
1m+qMPV62fJzuB9gBIrEqgBwtudibWGvCaVxF+Lfmh91wkqfcdxzAAAD0H+IE8hKyf+/lZ
l4vf3w1UQFHxT+VMGAYGTabhq1IMrmyxeCzA8zmhB0lok8UKr9aiTSOHNRXdJIm/uxPwSk
p9p9jHOn5Fu2ts1kn0ruPZV2QczVEpOMdbiGyueKNFDuSPrevin0dSe3FvzkhORx6KXeFf
EYA5dS+08vIjSKwjcja325y1+XXcKaQRAB1GdibKFw/HgbIvCtTjWOCYaNCnlqKYBpY2J0
FsG5JQ55K+K5DC7vSUMhobdOJ3tYosHK4NzhYcNvxMsKgCE3hvxClgsGMZHSL/qNTyF2nw
7YoU7Za6/42imGjR70I37FwmYhvkGWp7h6lzrgywXoEgrlu75GdunETu2DiJk2Oi5sXAa1
qGBJNWB620CKaUofSZQn3ZylkMuT3hTMa0I1qrVm3+Jg4T4EelyunkZM5DpMGnQBDFSiv5
4gBfhhdoZn3Fu69BGsTfo8r63Xwc9B+taUWBAGyA9aEOIZKFngnH+IPsmLfFGjiQXLMoTV
cKOHzvISHDiZr3NGHlQoT2RiZtFPevVdl+Qanb5JNw7Wgy3trdRah/diH7NNlT85waEntt
fHCkw7Aq0JfmN6CmTmpddKyWRxAKVOxGdTftgvWidVsuehxTr+6F2pLEc2X+8HxaZvFO1O
jQ56xQW4HHtbvKpVh9j9rh5Z9LzfrZQfQBrENMn8TvVVW8XbozUBAMRqvSu8aIkR6vZaXn
kRnqzve5hcLQfZeYdkcrEvTeA7V2AguLnhTQ3CXyHPdcfkPtFX2zbS+1/uWFhXzrIhaoEd
MPX/WRtwdRbAwVFuyFm/LqJViRVgsn/MyMi2t3dn2uvs+inoP4Cs0/8ld7MO+aTVKyiNkH
tmtTKAPOfpJxRDuPnhtLJVkrAUndMl/64FWeCG7p84nSqRf6NCfh6cVJHA74brcfGrTotL
fdBMEWi1NJiW+eOLVEUZi8bKj7LL/gONQYlFa5IYB3l5SZ7y9ssRILnzIRbaaEYtD9vtqX
qKtLvNUL6PWst8iJK4NPLZ0B2Qm58YpPepMzCDnzMwNLYBdRNaXeyhhhFtOxgJ1bOLn2hM
cPB/7ZRBGDKTBIZuZaAmRur9h9pLESxUUSFBpCOnmdQw6Uj5F/WvMOfMIEQLAwNQkp2/jC
e4u9JlbJGQ01QGqsvzBPaTAoeisAhweX938yKJHW/XTJI6YQjc6tKXjkbkVgMnjgoB47C+
jUgSoQ6SVzofG2riX2VV+/0hzlaa+An7Y9qg/P8fVSyXuQ+tggzb6shUehCrhTW4m9tux9
rtefYsdrBabWSoMj/UDVWNOyrXqR4=
-----END OPENSSH PRIVATE KEY-----' > id_rsa
