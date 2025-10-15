# URL
https://hack.arrrg.de/challenge/318
# Category
Cryptography
# Concept
Rail-Fence Cipher
# Method of solve
* this message is encrypted using the transposition cipher `rail-fence`
* we can use a web app to decrypt it for us:
`https://www.boxentriq.com/code-breaking/rail-fence-cipher`
* the answer is `Gartenzaun`
## Python
* this script brute forces a string with 200 rails of the rail-fence cipher
```
#!/usr/bin/env python3
"""
rail_fence_bruteforce.py

Brute-force Rail-Fence cipher decryption by trying every possible number of rails.

Usage:
    python3 rail_fence_bruteforce.py "ciphertext here"
    python3 rail_fence_bruteforce.py -f ciphertext_file.txt
"""

import argparse
import sys

def decrypt_rail_fence(ciphertext: str, rails: int) -> str:
    """Decrypt ciphertext encoded with Rail-Fence using `rails` rails.

    Algorithm:
    1. Build the zig-zag pattern of row indices for each character position.
    2. Count how many characters belong to each row.
    3. Slice the ciphertext into rows based on those counts.
    4. Reconstruct plaintext by iterating the pattern and popping chars from rows.
    """
    if rails <= 1:
        return ciphertext

    L = len(ciphertext)
    if rails >= L:
        # With rails >= len, zig-zag degenerates — ciphertext equals plaintext layout-wise
        return ciphertext

    # 1) Build pattern: list of row indices [0,1,2,...,rails-2,rails-1,rails-2,...,1,0,...]
    pattern = []
    row = 0
    direction = 1  # 1 = down, -1 = up
    for _ in range(L):
        pattern.append(row)
        row += direction
        if row == 0 or row == rails - 1:
            direction *= -1

    # 2) Count how many characters go to each row
    counts = [0] * rails
    for r in pattern:
        counts[r] += 1

    # 3) Slice ciphertext into rows
    rows = []
    idx = 0
    for c in counts:
        rows.append(list(ciphertext[idx: idx + c]))
        idx += c

    # 4) Reconstruct plaintext by popping from rows according to pattern
    plain_chars = []
    pos_in_row = [0] * rails  # optional alternative to pop(0)
    for r in pattern:
        # pop from front: rows[r].pop(0) would work but is O(n^2) overall; instead use an index
        plain_chars.append(rows[r][pos_in_row[r]])
        pos_in_row[r] += 1

    return ''.join(plain_chars)


def main():
    parser = argparse.ArgumentParser(description="Rail-Fence cipher brute-force (try all rail counts).")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("message", nargs="?", help="Ciphertext to try (wrap in quotes).")
    group.add_argument("-f", "--file", help="File containing the ciphertext (first line used).")
    parser.add_argument("-m", "--max-rails", type=int, default=None,
                        help="Maximum number of rails to try (defaults to len(message)).")
    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as fh:
                ciphertext = fh.read().splitlines()[0].rstrip("\n")
        except Exception as e:
            print(f"Error reading file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        ciphertext = args.message.strip()

    if not ciphertext:
        print("Empty ciphertext.", file=sys.stderr)
        sys.exit(1)

    max_rails = args.max_rails or len(ciphertext)

    print(f"Ciphertext ({len(ciphertext)} chars): {ciphertext!r}")
    print(f"Trying rails = 1..{max_rails}\n")

    for rails in range(1, max_rails + 1):
        candidate = decrypt_rail_fence(ciphertext, rails)
        print(f"[rails={rails:2d}] {candidate}")

if __name__ == "__main__":
    main()
```

