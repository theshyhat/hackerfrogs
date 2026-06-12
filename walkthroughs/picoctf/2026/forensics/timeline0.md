# URL
https://learn.cylabacademy.org/library/720
# Method of solve
We can use SleuthKit to investigate 
```
tsk_gettimes partition4.img > body.txt
mactime -b body.txt -d > timeline.csv
cat timeline.csv | head
```
This points us to the bin/bcab file
```
fls -p -r partition4.img | grep bcab
icat partition4.img 4945
echo -n "NzFtMzExbjNfMHU3MTEzcl9oM3JfNDNhMmU3YWYK" | base64 -d
```
