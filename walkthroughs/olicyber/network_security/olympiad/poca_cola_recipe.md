# URL
https://training.olicyber.it/challenges#challenge-25
# Concept
* extracting files from packets
* searching for packets with keywords
# Method of solve
* the first thing we look for is packets containing interesting keywords, like `frame contains "password"`
* we find two packets, which reference a password (`qhcdpoktbjdsujbsrpjwr`), and a reference to a recipe (`ricetta` in italian)
* `frame contains "ricetta"` results in `18626`, which references a file named `ricetta.txt.zip`
* we can use the Wirshark `Export Objects` -> `HTTP`, then find the file associated with packet `18626`, then save the file as `p18626.bin`
* when we inspect the file using `xxd`, we see that the zip file magic bytes `50 4b 03 04` start at `0xc0 + 12 bytes`, which is `0xcb`:
```
000000c0: 7874 2e7a 6970 220d 0a0d 0a50 4b03 0433  xt.zip"....PK..3
```
* and the end of the zip file, bytes `50 4b 05 06` end at `0x1a0 + 13 bytes`, which is `0x1bf`
* we'll use the `dd` tool to crop the HTTP headers off the file and restore it to the filename `ricetta.txt.zip`:
```
dd if=p18626.bin of=ricetta.txt.zip bs=1 skip=$((0xCB)) count=$((0x1BF - 0xCB))
```
* now we have to unzip the file, but this zip file requires a password, so we'll use 7z to unzip it:
```
7z x ricetta.txt.zip
```
* read the file and we're finished
