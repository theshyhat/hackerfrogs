# key points
* when an object is both `push` and `tele`, the `push` rule takes precedence, and the play can't use the object for teleporting
# method of solve
1) move the `love` object to a position below the `love is push` rule
2) move the `push` text into the `love` object, teleporting it
3) when the `push` text is not on the left-hand side of the map, move into the `love` object, teleporting `baba` to the right side of the map
4) move down, and when `push` is on the right-hand side of the map, move `baba` up, teleporting the `push` text up and forming the rule `love is push`
5) move the `love` object down into the water, destroying it
6) touch the `flag` to win
