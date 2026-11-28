# URL
https://github.com/cyberstudentsfoundation/csd-ctf/blob/main/rounds/1/Pokemon%20PW%20Crack/challenge.md
# Concept
* creation of custom wordlists
* hash identification
* NTLM hash cracking
# Method of solve
* we're a format for the correct cleartext password in this exercise
  * the name of a Pokemon concatenated with
  * a two-digit number
  * e.g., `pikachu67`
* the first thing we need to do is create a list of all the Pokemon
  * we can do this with a handy web app: `https://pokemondb.net/tools/text-list`
* the next thing we need to do is create the list concatenated with the two-digit numbers:
```Bash
while IFS= read -r pokemon; do for ((i = 0; i < 100; i++)); do printf '%s%02d\n' "$pokemon" "$i"; done; done < all_pokemon_lowercase.txt > all_combined_pokemon_lowercase.txt
```
* the next thing we need to do is identify what kind of hash this hash is
* this tool correctly identifies the hash as `NTLM`: `https://hashes.com/en/tools/hash_identifier`
* the last thing we need to do is crack the hash using a cracking program:
```
hashcat -m 1000 -a 0 hash all_combined_pokemon_lowercase.txt
```
