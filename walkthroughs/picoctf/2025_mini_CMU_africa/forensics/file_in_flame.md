# URL
https://play.picoctf.org/practice/challenge/523
# Concept
* base64-encoded data
* OCR (image to text) translation
# Method of solve
* we download the file, then we look at the contents
* the contents look like a base64-encoded string:
```
base64 -d logs.txt > new_logs
```
* when we use the `file` command on the new_logs file, we see that is a PNG image
* when we look at the image in an image viewer, we see a string of letters and numbers
* we can crop that image in Gimp, then give the image to Google images to extract the text data
* from there, we can use `xxd` to translate the hex characters to ASCII:
```
echo "7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F37383265353563397D" | xxd -r -p
```

