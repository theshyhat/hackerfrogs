# level goal
* move file 200 to the outbox
* leave no trace
# key concepts
* we're introduced to 4 commands in this level
  * the `link` command moves the Exa from one node to another, e.g., `link 800`, the link argument is relative to the node the Exa is currently in
  * the `grab` command picks up files in the current node, and must be used with the file name, e.g., `grab 200`
  * the `drop` command drops the file held by the Exa into the current node
  * the `halt` command removes the Exa from the level
# method of solve
```
link 800
grab 200
link 800
drop
halt
```
