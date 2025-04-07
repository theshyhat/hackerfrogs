# username
bandit12
# password
7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
# method of solve
Reverse the hex dump file with the XXD program
```
mkdir /tmp/...bandit12theshyhat
cp data.txt /tmp/...bandit12theshyhat/data.txt
cd /tmp/...bandit12theshyhat
file data
mv data data.gz
gunzip data.gz
file data
mv data data.bz2
bzip2 -d data.bz2
file data
mv data data.gz
gunzip data.gz
file data
mv data data.tar
tar -xf data.tar
file data5.bin
mv data5.bin data5.tar
tar -xf data5.tar
file data6.bin
mv data6.bin data6.tar
tar -xf data6.tar
mv data6.bin data6.bz2
bzip2 -d data6.bz2
file data6
mv data6 data6.tar
tar -xf data6.tar
file data8.bin
mv data8.bin data8.gz
gunzip data8.gz
file data8
cat data8
```
