# key points
* this level showcases the concept of using moving objects to pull other objects through dangerous tiles
# method of solve
1) form the rule `leaf is pull`
2) pull the `leaf` objects into a same row as the `win` tile, facing left
3) move the `push` text into position into the tile between the three `hedge`s
4) form the rule `leaf is move`, and break it when the first `leaf` enters the same column as the `fungus`
5) form the rule `leaf is pull`, then pull a `leaf` downwards into the tile between two `hedge`s
6) move the `push` text tile to the position directly below the `leaf` in the same column as the `fungus`
7) form the rule `leaf is pull and `leaf is move`, and wait until the `fungus` is moved into a non-`foliage` tile
8) form the rule `key is pull`, then move it out, then `key is push`, and push it into the `fungus`, revealing the `flag`
