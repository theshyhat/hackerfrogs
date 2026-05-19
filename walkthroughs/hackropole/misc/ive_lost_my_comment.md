# URL
https://hackropole.fr/en/challenges/misc/fcsc2026-misc-i-ve-lost-my-comment/
# Concept
* SSH keys are base64-encoded
# Method of solve
* copy the content of the private key, then base64 decode it
```
echo 'b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZWQyNTUxOQAAACBIZ5WpczSqpCbIR6wKsJmqYVLeBYOudgXouim+4SafxgAAAKApQxqsKUMarAAAAAtzc2gtZWQyNTUxOQAAACBIZ5WpczSqpCbIR6wKsJmqYVLeBYOudgXouim+4SafxgAAAEAxP+EgAYW4M3WHuwkOiBp4Qo0tXMHctFQal2w+3CUgyUhnlalzNKqkJshHrAqwmaphUt4Fg652Bei6Kb7hJp/GAAAAGmh0dHBzOi8vZmNzYy5mci9Qc0lnMFZCdTduAQID' | base64 -d
```


