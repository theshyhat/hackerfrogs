# HackerFrogs AfterSchool Cryptography Session 3
## Session Topic: Classical Cryptographic Ciphers Pt 2 /w PicoCTF
# Challenge 1: PicoCTF Vigenere
## PicoCTF Link
https://play.picoctf.org/practice/challenge/316
### YouTube Walkthrough Link
https://youtu.be/k0b6NBDcfTk?t=895
### Method of Solve
#### METHOD 1 (Python)
* Step 1: use the following command in the webshell terminal to start editing a file named `vigenere.py`:
```
nano vigenere.py
```
* Step 2: paste the following Python code into the text editor:
```
def vigenere_decrypt(ciphertext, key):
    """
    Decrypts a Vigenere cipher given the ciphertext and key.

    :param ciphertext: The encrypted string.
    :param key: The key used for decryption.
    :return: The decrypted plaintext.
    """
    plaintext = ""
    key_index = 0  # Track position in the key

    for char in ciphertext:
        if char.isalpha():  # Only decrypt alphabetic characters
            key_char = key[key_index % len(key)]  # Cycle through the key
            key_index += 1

            if char.islower():  # Lowercase letters
                c_index = ord(char) - ord('a')
                k_index = ord(key_char.lower()) - ord('a')
                p_index = (c_index - k_index) % 26
                plaintext += chr(p_index + ord('a'))
            elif char.isupper():  # Uppercase letters
                c_index = ord(char) - ord('A')
                k_index = ord(key_char.upper()) - ord('A')
                p_index = (c_index - k_index) % 26
                plaintext += chr(p_index + ord('A'))
        else:
            # Non-alphabetic characters remain unchanged
            plaintext += char

    return plaintext

# Example Usage
if __name__ == "__main__":
    encrypted_string = "rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}"  # Your encrypted text
    key_string = "CYLAB"  # Replace with your key

    decrypted_text = vigenere_decrypt(encrypted_string, key_string)
    print("Decrypted Text:", decrypted_text)
```
* Step 3: Save the file by typing in `ctrl + x`, then `y`, then hit the enter key to confirm the filename.
* Step 4: Use the following command to run the Python script:
```
python vigenere.py
```
* Step 5: Copy the flag, which starts with `picoCTF`, and ends with `}`
* Step 6: on the PicoCTF challenge page, submit the flag
#### METHOD 2 (Using Websites)
* Step 1: Copy the file link on the PicoCTF challenge page
* Step 2: in the webshell, use the following command to download the ciphertext file:
```
wget <file_address_here>
```
Replace `<file_address_here>` with the address you copied from the challenge page
* Step 3: Read the file with the following command:
```
cat cipher.txt
```
* Step 4: Copy the output
* Step 5: Access the following website `https://cryptii.com/pipes/vigenere-cipher`
* Step 6: On the `cryptii` website, paste the ciphertext string into the `Ciphertext` field
* Step 7: In the `KEY` field in the type in the key from the challenge page `cylab`
Observe that the decrypted flag appears in the `Plaintext` field on the webpage
* Step 8: Copy the flag from the `Plaintext` field. From `picoCTF` until `}`
* Step 9: On the PicoCTF challenge page, submit the flag
# Challenge 2: PicoCTF Rail Fence
## PicoCTF Link
https://play.picoctf.org/practice/challenge/289
## YouTube Walkthrough Link
https://youtu.be/k0b6NBDcfTk?t=3393
### Method of solve
#### METHOD 1 (Python)
* Step 1: use the following command in the webshell terminal to start editing a file named `rail-fence.py`:
```
nano rail-fence.py
```
* Step 2: Copy and paste the following code into the nano editor:
```
def rail_fence_decrypt(ciphertext, num_rails):
    """
    Decrypts a ciphertext encrypted using the Rail Fence cipher with the specified number of rails.

    :param ciphertext: The encrypted string.
    :param num_rails: The number of rows (rails) used for encryption.
    :return: The decrypted plaintext.
    """
    # Calculate the pattern of the rail fence
    rail_pattern = [[] for _ in range(num_rails)]
    
    # Create an empty structure to mark the pattern
    pattern = [0] * len(ciphertext)
    rail = 0
    direction = 1  # 1 for down, -1 for up

    for i in range(len(ciphertext)):
        pattern[i] = rail
        rail += direction
        if rail == 0 or rail == num_rails - 1:
            direction *= -1

    # Count the number of characters per rail
    rail_counts = [pattern.count(r) for r in range(num_rails)]

    # Extract characters for each rail
    pos = 0
    for rail in range(num_rails):
        rail_pattern[rail] = list(ciphertext[pos:pos + rail_counts[rail]])
        pos += rail_counts[rail]

    # Reconstruct the plaintext by following the pattern
    plaintext = []
    rail = 0
    direction = 1
    for i in range(len(ciphertext)):
        plaintext.append(rail_pattern[rail].pop(0))
        rail += direction
        if rail == 0 or rail == num_rails - 1:
            direction *= -1

    return ''.join(plaintext)

# Example Usage
if __name__ == "__main__":
    encrypted_string = "Ta _7N6D8Dhlg:W3D_H3C31N__387ef sHR053F38N43DFD i33___N6"
    num_rails = 4
    decrypted_text = rail_fence_decrypt(encrypted_string, num_rails)
    print("Decrypted Text:", decrypted_text)
```
* Step 3: Save the file by typing in `ctrl + x`, then `y`, then hit the enter key to confirm the filename.
* Step 4: Use the following command to run the Python script:
```
python rail-fence.py
```
* Step 5: Copy the flag, which starts with `picoCTF`, and ends with `}`
* Step 6: on the PicoCTF challenge page, submit the flag
# Challenge 3: PicoCTF Transposition Trial
## PicoCTF Link
https://play.picoctf.org/practice/challenge/312
## YouTube Walkthrough Link
https://youtu.be/k0b6NBDcfTk?t=2039
### Method of solve
* Step 1: use the following command in the webshell terminal to start editing a file named `tpt.py`:
```
nano tpt.py
```
* Step 2: Copy and paste the following code into the nano editor:
```
def rearrange_blocks(blocks):
    """
    Rearranges each block by moving the 3rd character to the 1st position.
    Leaves incomplete blocks (length < 3) unchanged.
    """
    rearranged = []
    for block in blocks:
        if len(block) == 3:
            # Move 3rd character to front: [2] + [0] + [1]
            new_block = block[2] + block[0] + block[1]
            rearranged.append(new_block)
        else:
            # Leave incomplete blocks unchanged
            rearranged.append(block)
    return rearranged

def process_file(filename, block_size=3):
    """
    Processes a file by:
    1. Splitting into blocks
    2. Rearranging blocks
    3. Concatenating the result
    """
    try:
        with open(filename, 'r') as file:
            content = file.read().replace('\n', '')  # Remove newlines
        
        # Split into blocks
        blocks = [content[i:i+block_size] for i in range(0, len(content), block_size)]
        
        # Rearrange blocks
        rearranged = rearrange_blocks(blocks)
        
        # Concatenate all blocks
        final_result = ''.join(rearranged)
        
        return blocks, rearranged, final_result
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return [], [], ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return [], [], ""

if __name__ == "__main__":
    filename = input("Enter the file path: ")
    original, rearranged, final = process_file(filename)
    
    print("\nOriginal Blocks:")
    for i, block in enumerate(original, 1):
        print(f"Block {i}: {block}")
    
    print("\nRearranged Blocks:")
    for i, block in enumerate(rearranged, 1):
        print(f"Block {i}: {block}")
    
    print("\nFinal Concatenated Result:")
    print(final)
```
* Step 3: Save the file by typing in `ctrl + x`, then `y`, then hit the enter key to confirm the filename.
* Step 4: Use the following command to run the Python script:
```
python tpt.py
```
* Step 5: Copy the flag, which starts with `picoCTF`, and ends with `}`
* Step 6: on the PicoCTF challenge page, submit the flag
