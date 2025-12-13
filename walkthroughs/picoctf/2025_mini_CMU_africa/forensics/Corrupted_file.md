# URL
https://play.picoctf.org/practice/challenge/519
# Concept
* fixing file headers
* magic bytes
# Method of solve
* when we examine the file in a hex editor, we see that the file should be a JPEG file from this output:
```
\x....JFIF
```
* this means this that we should be able to restore the file if we edit the magic bytes / file header
* we need to replace the first few bytes with these `FF D8 FF E0 00 10 4A 46
49 46 00 01`
* we can do that in any hex editor, in our example we used the `hexedit` program
* the last step is to rename the file to have a `jpg` file extension, then view the file with any image viewing program
