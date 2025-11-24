# URL
https://ringzer0ctf.com/challenges/51
# Concept
* Windows `Groups.xml` file
* how to decrypt GPP encrypted passwords
# Method of solve
* download the zip file
* unzip the zip file
* see that there is a `Groups.xml` file included in the unzipped files
* it's possible for encrypted passwords to be found in the `Groups.xml` file
* we can decrypt those encrypted passwords using a common tool, `gpp-decrypt`
```
gpp-decrypt "PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw"
```
