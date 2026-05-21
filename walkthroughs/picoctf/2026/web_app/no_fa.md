# URL

# Concept

# Method of solve
```Python
import base64
import json
import zlib
import sys

def decode_flask_cookie(cookie):
  compressed = False
  payload = cookie

  if payload.startswith('.'):
    compressed = True
    payload = payload[1:]

  data = payload.split('.')[0]
  data += '=' * (-len(data) % 4)
  raw = base64.urlsafe_b64decode(data)

  if compressed:
    raw = zlib.decompress(raw)

  return raw.decode('utf-8')

cookie = sys.argv[1]
decoded = decode_flask_cookie(cookie)
print(json.dumps(json.loads(decoded), indent=2))
```




