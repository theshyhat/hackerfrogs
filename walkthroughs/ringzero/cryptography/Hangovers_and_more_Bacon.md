# URL
https://ringzer0ctf.com/challenges/114
# Concept
* Bacon cipher
* transformation of text (uppercase to A, lowercase to B)
# Method of solve
* we are given a ciphertext in the form of a French paragraph
* we need to convert all uppercase letters to the letter A to conform to the Bacon cipher, which is made up entirely of A and B characters
* we also need to convert the lowercase letters to the letter B
* we can do that with this command:
```
echo 'VoiCI unE SUpeRbe reCeTtE cONcontee pAR un GrouPe dArtistEs culinaiRe, dONT le BOn Gout et lE SeNs de LA cLasSe nest limIteE qUe par LE nombre DE cAlOries qUils PeUVEnt Ingurgiter. Ces virtuoses de la friteuse vous presente ce petit clip plein de gout savoureux !!' | tr '[:upper:]' "A" | tr '[:lower:]' "B" | tr -d " " | tr -d "," | tr -d '!' | tr -d "."
```
* then we can feed the transformed text into a web app that decodes Bacon Cipher
```
https://www.dcode.fr/bacon-cipher
```
