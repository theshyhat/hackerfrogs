# URL
https://tryhackme.com/room/yara-aoc2025-q9w1e3y5u7
# Concept
YARA rules for defensive cybersecurity
# Method of solve
* the task wants us to write a YARA rule to run on a specific directory
* first navigate to the `/home/ubuntu/Downloads` directory
```
cd /home/ubuntu/Downloads
```
* from here we can write the YARA rules we'll use for the task into a file: we'll call the file `rule.yar`
```
rule TBFC_string_match
{
    strings:
        $s = /TBFC:[A-Za-z0-9]+/ ascii
    condition:
        $s
}
```
* now we can run the `yara` command with the `rule.yar` file on the `easter` directory
```
yara -s -r rule.yar easter
```
## Q1 - How many images contain the string TBFC?
Count the number of files that match after the previous command
## Q2 - What regex would you use to match a string that begins with TBFC: followed by one or more alphanumeric ASCII characters?
`/TBFC:[A-Za-z0-9]+/`
## Q3 - What is the message sent by McSkidy?
Look at the numbers on the matching files to determine the word order of the message
