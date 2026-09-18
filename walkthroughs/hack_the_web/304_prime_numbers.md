# URL
https://hack.arrrg.de/challenge/304
# Category
Programming
# Concept
* parsing large datasets
* managing heavy computation
# Method of solve
## Part 1: Calculating the Primes
```Python
import os
import sympy

def find_and_save_primes(end_num):
    filename = "primes_output.txt"
    start_num = 2

    # 1. Automatically detect if a file exists to resume progress
    if os.path.exists(filename):
        try:
            with open(filename, "rb") as f:
                # Seek to the end of the file to efficiently read the last line
                f.seek(0, os.SEEK_END)
                pos = f.tell()
                
                # Move backward to find the start of the last line
                while pos > 0:
                    pos -= 1
                    f.seek(pos, os.SEEK_SET)
                    if f.read(1) == b'\n' and pos != f.tell() - 1:
                        break
                
                last_line = f.readline().decode().strip()
                if last_line.isdigit():
                    # Resume from the next integer after the last found prime
                    start_num = int(last_line) + 1
                    print(f"Resuming from last saved checkpoint: {start_num:,}")
        except Exception:
            print("Could not read last line. Defaulting to manual input.")

    # 2. Allow manual user input override
    user_input = input(f"Enter starting number (Press Enter to keep default {start_num:,}): ").strip()
    if user_input.isdigit():
        start_num = max(2, int(user_input))

    print(f"Calculating primes from {start_num:,} to {end_num:,}...")
    print(f"Saving results to '{filename}'...")

    # 3. Stream primes incrementally using an iterator to save memory
    prime_stream = sympy.primerange(start_num, end_num + 1)

    # Open file in append mode ('a') so we never overwrite past work
    with open(filename, "a", encoding="utf-8") as file:
        for prime in prime_stream:
            file.write(f"{prime}\n")
            # Optional: flush buffer periodically so data writes immediately
            file.flush() 

if __name__ == "__main__":
    # Your target: 2^32
    MAX_LIMIT = 4294967296 
    find_and_save_primes(MAX_LIMIT)
```
## Part 2: Add All The Numbers in the Numbers File
```Python
import os

def sum_numbers_in_file(filename):
    # Check if the file exists before starting
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        return

    total_sum = 0
    line_count = 0

    print(f"Reading '{filename}' and calculating total sum...")

    # Opening the file using a context manager
    with open(filename, 'r', encoding='utf-8') as file:
        # Loop directly over the file object to read it line-by-line (lazy loading)
        for line in file:
            cleaned_line = line.strip()
            if cleaned_line.isdigit():  # Ensure the line actually contains a valid number
                total_sum += int(cleaned_line)
                line_count += 1
                
                # Optional visual anchor: Print status updates for massive files
                if line_count % 10_000_000 == 0:
                    print(f"Processed {line_count:,} numbers...")

    print("\n--- Calculation Complete ---")
    print(f"Total numbers found: {line_count:,}")
    print(f"Total sum:           {total_sum:,}")
    return total_sum

if __name__ == "__main__":
    # Change this to match your file name
    TARGET_FILE = "primes_output.txt" 
    sum_numbers_in_file(TARGET_FILE)
```
