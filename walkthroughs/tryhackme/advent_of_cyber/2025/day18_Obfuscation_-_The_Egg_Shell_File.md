# URL
https://tryhackme.com/room/obfuscation-aoc2025-e5r8t2y6u9
# Concept
* obfuscation
* deobfuscation
# Method of solve
## Q1 - What is the first flag you get after deobfuscating the C2 URL and running the script?
* double click the SantaStealer icon on the Desktop of the task machine
* near the top of the script, copy the value of the `$C2B64` value: `aHR0cHM6Ly9jMi5ub3J0aHBvbGUudGhtL2V4Zmls`
* go to `https://cyberchef.io/` and paste the value into the `Input` window
* apply the `From Base64` operation, and note the value in the `Output` window
* type that value into the task machine `StantaStealer` editor window in the place of the `$C2` variable value
* save the script
* open a Powershell terminal, then run the following commands:
```
cd Desktop
.\SantaStealer.ps1
```
## Q2 - What is the second flag you get after obfuscating the API key and running the script again?
* in the script, copy the `$ApiKey` value: `CANDY-CANE-API-KEY`
* in CyberChef, paste the value into the `Input` window
* apply the `XOR` operation with the `Key` parameter set to `37`
* next, apply the `To Hex` operation underneath the `XOR` operation to apply both operations, one after another
* copy the value in the `Output` window
* in the script, replace the `$ObfAPIKEY` `hex` parameter with the value you copied
* save the script
* run it again in the Powershell terminal





