# key points
* even if parts of rules are negated, any valid portions still apply
# method of solve
1) Set the rule `cog is robot` to create two robots
2) setup the horizontal sequence `is cog stop` in the row between the `flag` and `rock` text tiles located on the right-hand part of the map
3) setup the rule `robot is push`
4) push one of the robots to the left of the `is cog stop` tiles
5) form the rule `robot is move`
6) break the rule `robot is move` when the robot crosses the water, back to the left-hand side of the map
7) push two `and` text tiles into positions beside the water in rows between the (`rock` and `ice`) and (`ice` and `win`) text tiles on the right-hand side of the map
8) form the rule `robot is push`, then push the robots into position directly to the left of the separate `and` text tiles
9) form the rule `robot is move` in a position very close to the `flag`
10) move over the flag and wait for the robots to move the `and` tiles to the right-hand side of the screen, forming the rule `flag is rock and ice and win`
