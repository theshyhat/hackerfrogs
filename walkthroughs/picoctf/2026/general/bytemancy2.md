# URL
https://learn.cylabacademy.org/library/724
# Concept
* sending arbitrary bytes as input
# Method of solve
The `app.py` script follows:
```Python
import sys

while(True):
  try:
    print('⊹──────[ BYTEMANCY-2 ]──────⊹')
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print()
    print('Send me the HEX BYTE 0xFF 3 times, side-by-side, no space.')
    print()
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print('⊹─────────────⟡─────────────⊹')
    print('==> ', end='', flush=True)
    user_input = sys.stdin.buffer.readline().rstrip(b"\n")
    if user_input == b"\xff\xff\xff":
      print(open("./flag.txt", "r").read())
      break
    else:
      print("That wasn't it. I got: " + str(user_input))
      print()
      print()
      print()
  except Exception as e:
    print(e)
    break
```
The app is looking for byte `0xFF`, and we can do it in two different ways.

This command is for doing it with `Python`:
```
python -c 'import sys;sys.stdout.buffer.write(b"\xff"*3 + b"\x0a")' | nc lonely-island.picoctf.net 62675
```
And this one is for `Printf`:
```
printf "\xff\xff\xff\x0a" | nc lonely-island.picoctf.net 62675
```
The reason why we include the `x0a` byte is to send the command off (it's the newline byte)
