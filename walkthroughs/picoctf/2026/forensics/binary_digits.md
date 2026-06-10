# URL
https://learn.cylabacademy.org/library/698
# Concept
* binary digit to binary data conversion
* magic byte / file header identification
# Method of solve
## CyberChef Method
1) In the CyberChef UI, click on the `Open File as Input` in the `Input` window, then select the `digits.bin` file
2) In the `Operations` window, search `from binary`, then drag the `From Binary` operation button into the `Recipe` window
3) In the `Output` windows, click on the `Save output to file` button and save the file as `digits.jpg`
4) Open the file to obtain the flag
## Python method
```Python
with open("digits.bin", "r") as f:
    data = f.read().strip()
    print("Reading input from file: digits.bin")
    print(f"File contents:\n{data}")

data = "".join(data.split())

output = bytes(int(data[i:i+8], 2) for i in range(0, len(data), 8))
print(f"Converted binary digits to bytes:\n{output}")

with open("digits.jpg", "wb") as f:
    f.write(output)

print("Wrote output to file: digits.jpg")
```
