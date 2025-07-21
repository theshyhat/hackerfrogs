# username
aura
# password
TiqpedAFjwmVyBlYpzRh
# mission contents
User aegle has a good memory for numbers.
# method of solve
* This challenge requires you to input a string of numbers into the `numbers binary`
* `1 2 3 1 2 3 9 1 1 1 1 2 6`
* We're workshopping a Python script to automate the process..
```
import subprocess

def run_numbers_binary():
    # Path to the binary
    binary_path = "/pwned/aura/numbers"
    
    # Run the binary, send input, and capture output
    try:
        process = subprocess.Popen(
            binary_path,              # Binary to execute
            stdin=subprocess.PIPE,     # Pipe for input
            stdout=subprocess.PIPE,    # Pipe for output
            stderr=subprocess.PIPE,    # Pipe for errors (optional)
            text=True                  # Use text mode (for Python 3.7+)
        )
        
        # Send "1" followed by a newline
        output, errors = process.communicate(input="1\n2\n3\n1\n2\n3\n9\n1\n1\n1\n1\n2\n6\n")
        
        # Print the result
        print("Output:", output)
        if errors:
            print("Errors:", errors)
    
    except PermissionError:
        print("Error: You don't have execute permissions on the binary.")
    except FileNotFoundError:
        print("Error: Binary not found at", binary_path)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    run_numbers_binary()
```
