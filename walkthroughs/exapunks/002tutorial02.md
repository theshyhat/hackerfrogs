# level goal
* append the correct value to the end of file 200
* move file 200 to the outbox
* leave no trace
# key concepts
* this level introduces 4 more commands
  * the `copy` command copies the value of A to B, e.g., `copy F X`
  * the `addi` command adds A and B together and writes the resulting value to C, e.g., `addi A B A`
  * the `muli` command multiples A and B together and writes the resulting value to C, e.g., `muli A B A`
  * the `subi` command subtracts B from A and writes the resulting value to C, e.g., `subi A B A`
# method of solve
```
link 800
grab 200
copy f x
addi x f x
muli x f x
subi x f x
copy x f
link 800
drop
halt
```
