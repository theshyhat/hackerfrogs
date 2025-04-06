> We download the file and inspect the metadata
```
exiftool red.png
```
> There's a poem in the metadata, and if we take the first letter of each sentence, we get "checklsb". This is a reference to a steganography technique. We can use zsteg to get the LSB value
```
sudo gem install zsteg
zsteg red.png
```
> In the resulting output, there's a base64 encoded string
```
echo -n 'cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==' | base64 -d
```
Finis
