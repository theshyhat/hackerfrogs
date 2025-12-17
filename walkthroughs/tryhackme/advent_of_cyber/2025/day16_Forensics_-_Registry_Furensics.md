# URL
https://tryhackme.com/room/registry-forensics-aoc2025-h6k9j2l5p8
# Concept
* Windows log forensics
# Method of solve

## Q1 - What application was installed on the dispatch-srv01 before the abnormal activity started?
* navigate to the `SOFTWARE` hive, then we can see a certain program was uninstalled on the system by navigating to the following path:
```
ROOT\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall
```
* sort the entries by `Timestamp`, then lookup the sole entry that was uninstalled on `October 21 2025`
* we find the name of the app in the `DisplayName` column
## Q2 - What is the full path where the user launched the application (found in question 1) from?
* we can find the name of executed applications by navigating to the `NTUSER.DAT` hive
* then we can find the executed applications at the following path:
```
ROOT\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Compatibility Assistant\Store
```
## Q3 - Which value was added by the application to maintain persistence on startup?
* if we navigate to `SOFTWARE` hive, we can see what programs startup after the user logs in in this path:
```
ROOT\Microsoft\Windows\CurrentVersion\Run
```
