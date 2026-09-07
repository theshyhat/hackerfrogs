# WORK IN PROGRESS
# URL
https://hackropole.fr/en/challenges/reverse/fcsc2024-reverse-strike/
# Concept
* input transformation
* 
# Method of solve
* when we look at the decompiled version of the program (Cutter), we see that there are two functions to pay attention to
  * the main function (of course)
  * and the lookup function
  * 
```Python
def generate_payload():
    # 1. Define the custom alphabet and the target string
    alphabet = "abcdefghijklmnopqrstuvwxyz!# $:-()."
    target_string = "# congratulations! this is a strike :-) you should now see the flag printed ... #"
    
    payload = ""
    
    # 2. Iterate through each character in the target string
    for j, char in enumerate(target_string):
        # Find the index of the character in the alphabet
        target_index = alphabet.index(char)
        
        # Calculate the loop variable 'i' for this character position
        i = j * 2
        
        # 3. Reverse the modulo math: (target_index - i) % 35
        var_21h = (target_index - i) % 35
        
        # 4. Convert the resulting byte value back into 2 hex characters (zero-padded)
        payload += f"{var_21h:02x}"
        
    return payload

# Generate and print the answer
result = generate_payload()
print(f"Payload (Length: {len(result)} characters):\n{result}")
```
