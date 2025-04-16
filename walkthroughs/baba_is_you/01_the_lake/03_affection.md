# key points
* this level introduces the love object (a heart)
* it also introduces the `move` verb, which makes the object move one tile in a set direction each time we move
# method of solve
1) Setup the rules `keke is push`, then move keke into place to collide with the love object after a few steps
2) Setup the `love is push` and `keke is move` rules, so keke moves the love object out of the algae box, and we have access to it
3) Unset the rule `love is push` so we can actually move into the object
