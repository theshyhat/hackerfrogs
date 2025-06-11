# key points
* this level introduces the `belt` object and the `shift` verb
* the `belt` object is often used with the `shift` verb, which moves any object on top of it one tile in the direction that it is pointing
* a `shift` object can be used to move other objects out of the way
# method of solve
1) set `belt is push`
2) `push` a couple of belt onjects on top of the `wall` tiles
3) set `belt is shift`
4) wait a couple of turns, and the walls will be moved
5) set `belt is push`
6) push the `belt` objects two tiles to the right
7) set `belt is shift`
8) after the walls have moved to the right, break `belt is shift`
9) touch the `flag` to `win`
