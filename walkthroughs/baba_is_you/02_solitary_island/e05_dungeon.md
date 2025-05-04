# key points
* this level features a weird interaction, where text can overlap with a playable object if the playable object is unable to move due to a `stop` object or the edge of the map
* we should note that text cannot overlap with other text tiles
# method of solve
1) form the rules `baba is you` and `keke is you` simultaneously
2) position `baba` and `keke` to the top and bottom of the `wall is stop` rule
3) move `keke` up, causing the `wall text` to overlap with `baba`
4) move down, breaking the `wall is stop` rule
5) form the rule `wall is win`
6) move into the `wall` to win
