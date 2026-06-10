# Scenario
* One of the puzzles in this level involves us spelling out a word with a combination lock where there are letters on the turn wheels
* The riddle that points us towards the answer indicates a word meaning:
  * something in-between
  * something that is left behind, or the presence of something
* we wrote a Python script that brute-forces all the words in the dictionary with the possible letters in the lock:
```Python
from itertools import product

letters_1 = ['a', 'w', 't', 'r', 'o', 'l', 'k', 'i', 'e', 'c']
letters_2 = ['o', 'l', 'k', 'i', 'e', 'c', 'a', 'w', 't', 'r']
letters_3 = ['t', 'r', 'o', 'l', 'k', 'i', 'e', 'c', 'a', 'w']
letters_4 = ['k', 'i', 'e', 'c', 'a', 'w', 't', 'r', 'o', 'l']

dictionary_path = "/usr/share/dict/words"

with open(dictionary_path, "r", encoding="utf-8", errors="ignore") as f:
    dictionary_words = {line.strip().lower() for line in f if line.strip()}

found_words = []

for combo in product(letters_1, letters_2, letters_3, letters_4):
    word = "".join(combo)
    if word in dictionary_words:
        found_words.append(word)

print(found_words)
```
* and these are the results:
`['alta', 'alto', 'aloe', 'alit', 'alec', 'alar', 'acre', 'acct', 'awol', 'aria', 'area', 'aral', 'work', 'wore', 'wool', 'woke', 'witt', 'wire', 'wile', 'wilt', 'will', 'wiki', 'wick', 'were', 'welt', 'well', 'weir', 'week', 'weer', 'weak', 'wear', 'weal', 'watt', 'ware', 'wart', 'walk', 'wale', 'walt', 'wall', 'wake', 'wait', 'wail', 'wack', 'waco', 'wwii', 'writ', 'tote', 'toto', 'tore', 'tort', 'took', 'toot', 'tool', 'toll', 'toke', 'toil', 'tito', 'tire', 'tiro', 'tile', 'tilt', 'till', 'tike', 'tier', 'tick', 'teri', 'terr', 'tell', 'teak', 'teat', 'tear', 'teal', 'tate', 'tare', 'tara', 'tart', 'taro', 'talk', 'tale', 'talc', 'tall', 'take', 'tail', 'tack', 'tact', 'taco', 'twit', 'twee', 'trot', 'trio', 'trek', 'tree', 'rote', 'rotc', 'rook', 'root', 'role', 'roll', 'roil', 'rock', 'roar', 'rowe', 'rite', 'rita', 'riot', 'rile', 'rill', 'riel', 'rick', 'rice', 'rico', 'reek', 'reel', 'rear', 'real', 'rate', 'rare', 'rake', 'rail', 'rack', 'race', 'oort', 'oleo', 'okra', 'okla', 'otto', 'oreo', 'oral', 'lott', 'lori', 'lore', 'lora', 'look', 'loot', 'lola', 'loll', 'loki', 'lock', 'loci', 'loco', 'lowe', 'lite', 'lire', 'lira', 'lila', 'lilt', 'like', 'lick', 'lice', 'liar', 'leta', 'lela', 'leek', 'leer', 'leak', 'lear', 'late', 'lark', 'lara', 'lake', 'lair', 'lack', 'lace', 'kook', 'klee', 'kite', 'kirk', 'kilt', 'kilo', 'kill', 'kiel', 'kick', 'kiwi', 'keto', 'keri', 'kerr', 'keel', 'keck', 'kate', 'kari', 'kara', 'karo', 'karl', 'kali', 'kale', 'kroc', 'iota', 'iowa', 'ikea', 'ieee', 'ella', 'eire', 'earl', 'ewer', 'etta', 'erik', 'erie', 'eric', 'cote', 'cork', 'core', 'cora', 'cook', 'coot', 'cool', 'cole', 'cola', 'colt', 'colo', 'coke', 'coil', 'cock', 'coat', 'coal', 'cowl', 'clot', 'clii', 'clit', 'clio', 'clew', 'cleo', 'claw', 'cite', 'celt', 'cell', 'catt', 'cato', 'care', 'cara', 'cart', 'carr', 'carl', 'calk', 'cali', 'call', 'cake', 'crow', 'cree', 'crew', 'craw']`



