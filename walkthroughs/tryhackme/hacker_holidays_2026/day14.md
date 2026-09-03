# URL
https://tryhackme.com/room/hh-managementwantsaword-6bf3cc41
# Concepts
* Windows file forensics
* extracting secrets from web browsers (Google Chrome)
* identifying VeraCrypt containers
# Method of solve
* when we down the task files, it is a dump of a Windows filesystem C drive
  * the tool that was used to create the dump was `KAPE`
* we are given hints that the Google Chrome browser on the system can be compromised
## Extracting the Required Files from The AppData Directory
* in order to extract the passwords from the Google Chrome browser, we need the following files:
  * the `Login Data` database file that Google Chrome uses
    * located at `/management-wants-a-word-forensics-hh-day-14/KAPE/C/Users/vera/AppData/Local/Google/Chrome For Testing/User Data/Default/Login Data`
  * the `Local State` JSON file that stores local browser settings, as well as encryption keys
    * located at `/management-wants-a-word-forensics-hh-day-14/KAPE/C/Users/vera/AppData/Local/Google/Chrome For Testing/User Data/Local State`
## Extract the Encryption Key From the Local State file
* since this is a JSON file, we can use `jq` and grep for the `encryption_key`
```
cat './management-wants-a-word-forensics-hh-day-14/KAPE/C/Users/vera/AppData/Local/Google/Chrome For Testing/User Data/Local State' | jq | grep -i "encrypted_key"
```
* take the `encrypted_key` value and write it a file called `encrypted_key`
## Turn the Encrypted Key into a Blob That Can Be Read Using Impacket Tools
* base64 decode the key, and output that into a binary file:
```
cat encrypted_key | base64 -d > browser_blob.bin
```
* we need to snip off the first five bytes of the file, which contain the string `DPAPI`
```
tail -c +6 browser_blob.bin > file.tmp && mv file.tmp browser_blob.bin
```
## Get The NTLM Hash For the Associated User Using Impacket Tools
* we need to extract the following two files:
  * the `SAM` file
    * located here: `./management-wants-a-word-forensics-hh-day-14/KAPE/C/Windows/System32/config/SAM`
  * the `SYSTEM` file
    * located here: `./management-wants-a-word-forensics-hh-day-14/KAPE/C/Windows/System32/config/SYSTEM` 
* then run `impacket-secretsdump`
```
impacket-secretsdump -sam SAM -system SYSTEM local > ntlm_hashes
```
## Crack the Hash For the Vera User
* copy the line of the file with the vera user and write to a file:
```
echo '1241186a4aac4f34f4bf7ace71b396a8' > vera_nthash
```
* we can now feed this into Hashcat to get the password for the vera user:
```
hashcat -m 1000 -a 0 vera_nthash /usr/share/wordlists/rockyou.txt
```
* we discover the password is `minivera`
## Extract the DPAPI Master Key File
* the file can be found in the following directory:
```
./management-wants-a-word-forensics-hh-day-14/KAPE/C/Users/vera/AppData/Roaming/Microsoft/Protect/S-1-5-21-2529683458-431225740-1723070931-1000/c90719ef-5b98-474e-b934-136d606a702a
```
* once found, we can extract the master key from it using Impacket:
```
impacket-dpapi masterkey -file ./management-wants-a-word-forensics-hh-day-14/KAPE/C/Users/vera/AppData/Roaming/Microsoft/Protect/S-1-5-21-2529683458-431225740-1723070931-1000/c90719ef-5b98-474e-b934-136d606a702a -sid S-1-5-21-2529683458-431225740-1723070931-1000 -hashes 1241186a4aac4f34f4bf7ace71b396a8
```
* we need to supply the password for the vera user to complete this step
* the output of the command will have the decrypted key: `0x5e5715ec9b6df5a86e97902692a66d28e691f05d5bc1e04d0159cfe960e94c978c07e5004a0179d3a96df2468885a28175b0b02cc064445f116a752d2b3e9d40`
## Get the AES Key From the Browser Blob File Using Impacket Tools
* with the decrypted key and the Browser Blob, we can get the AES key for the Chrome browser database file using this command:
```
impacket-dpapi unprotect -file browser_blob.bin -key 0x5e5715ec9b6df5a86e97902692a66d28e691f05d5bc1e04d0159cfe960e94c978c07e5004a0179d3a96df2468885a28175b0b02cc064445f116a752d2b3e9d40
```
* the output is a 32-byte hexadecimal key we can use to decrypt and read the secrets in the Chrome database file
## Get the Secrets Using A Python Script
* this Python script will extract the secrets (shoutout to my friend Gemini)
```Python
# pip install pycryptodome
import os
import sqlite3
from Crypto.Cipher import AES

# 1. INPUT CONFIGURATION
# Paste your 32-byte (64 character) hex key here
HEX_KEY = "206A39A0971327EA9487E4AEA9844F5D3670162456982276939A712646DA0B02" # IMPORTANT
# Path to your extracted Login Data file
LOGIN_DATA_PATH = "login_data.db"  # IMPORTANT

def decrypt_password(ciphertext, aes_key):
    try:
        # Check for modern Chromium payload signatures (v10 or v20)
        if ciphertext.startswith(b'v10') or ciphertext.startswith(b'v20'):
            # The Initialization Vector (IV) is 12 bytes long, starting at byte index 3
            iv = ciphertext[3:15]
            # The actual encrypted password payload starts after the IV
            encrypted_password = ciphertext[15:]
            
            # Initialize the AES-GCM cipher
            cipher = AES.new(aes_key, AES.MODE_GCM, iv)
            # Decrypt and verify (truncating the 16-byte GCM authentication tag at the end)
            decrypted = cipher.decrypt(encrypted_password[:-16])
            return decrypted.decode('utf-8', errors='ignore')
    except Exception as e:
        return f"[Decryption Error: {e}]"
    return ""

def main():
    # Convert hex key string to raw bytes
    aes_key = bytes.fromhex(HEX_KEY)
    
    if not os.path.exists(LOGIN_DATA_PATH):
        print(f"[-] Error: Could not find Login Data file at {LOGIN_DATA_PATH}")
        return

    # Connect to the SQLite database
    conn = sqlite3.connect(LOGIN_DATA_PATH)
    cursor = conn.cursor()
    
    try:
        # Query target credential columns
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        rows = cursor.fetchall()
        
        print(f"[+] Found {len(rows)} credential entries.\n")
        print(f"{'URL / Service':<50} | {'Username':<30} | {'Password'}")
        print("-" * 100)
        
        for url, username, ciphertext in rows:
            if username or ciphertext:
                plaintext_pass = decrypt_password(ciphertext, aes_key)
                print(f"{str(url):<50} | {str(username):<30} | {plaintext_pass}")
                
    except sqlite3.OperationalError as e:
        print(f"[-] Database error: {e}. (Ensure Chrome isn't locking the file)")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
```
* we should have a password after running the script: `Wh4t1sV3raD0inG0nTh1sH0st`
## Figuring Out The Backup File
* there is a suspicious file in this location: `./management-wants-a-word-forensics-hh-day-14/KAPE/C/Users/vera/Documents/backup`
* this file is a VeraCrypt container
  * the only clue that it is this type of file is the fact that its file size is evenly divisible by 512
  ```
  python -c 'print(104857600 % 512)'
  ```
* if this is a VeraCrypt container, we need to mount it
## Mounting the VeraCrypt Container
* we use this command to mount the container:
```
sudo cryptsetup tcryptOpen backup backup
```
* it will ask for a password, which we provide
* then we find the backup container with this command:
```
find /dev -name backup
```
* it's in `/dev/mapper/backup`
* mount the container
```
sudo mount /dev/mapper/backup /mnt/backup
```
## Enter the Container and Get The Flag
* once we've entered the container directory, there's a suspicious directory name
* inside, there is a PDF with the flag
* finished!

