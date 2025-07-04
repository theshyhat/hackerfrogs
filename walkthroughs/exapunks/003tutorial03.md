# level goal
* create the specified file in the outbox
* delete file 199
* leave no trace
# key concepts
* this level introduces 2 more commands
  * the `make` command creates an empty file held by the Exa that creates it
  * the `wipe` command deletes the file held by an Exa
  * the `muli` command multiples A and B together and writes the resulting value to C, e.g., `muli A B A`
  * the `subi` command subtracts B from A and writes the resulting value to C, e.g., `subi A B A`
# method of solve
`XA`
```
LINK 800
LINK 799
GRAB 199
COPY F M
COPY F M
WIPE
```
`XB`
```
LINK 800
LINK 800
MAKE
COPY M X
COPY M F
COPY X F
```
