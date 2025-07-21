# username
acantha
# password
mYYLhLBSkrzZqFydxGkn
# objective
The user alala has left us a program, if we insert the 6 correct numbers, she gives us her password!
# method of solve
```
scp -P 6666 acantha@hades.hackmyvm.eu:/pwned/acantha/guess /tmp/
chmod +x guess
```
Python Script...
```
import subprocess

# Path to the binary
binary_path = "./guess"

# Loop through all 6-digit PINs
for pin in range(1000000):
    # Format the PIN to be 6 digits, with leading zeros if necessary
    pin_str = str(pin).zfill(6)
    print(f"Trying PIN: {pin_str}")

    # Use subprocess to run the binary and provide input
    process = subprocess.Popen([binary_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Send the PIN as input to the binary
    output, error = process.communicate(input=(pin_str + '\n').encode())

    # Decode the output to make it human-readable
    output_decoded = output.decode()

    # Check if the binary's output contains the failure message
    if "NO" not in output_decoded:
        print(f"Correct PIN found: {pin_str}")
        break
```
