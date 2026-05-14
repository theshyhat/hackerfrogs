# URL
https://hackropole.fr/en/challenges/misc/fcsc2025-misc-touillette/
# Concept
* we need to reverse a lot of string slicing operations in Python
# Method of solve
```Python
# This is the how the program reads the encrypted flag
output = open("output.txt").read()

# This ensures that the length of the flag file contents
# is exactly 64 characters in length
# assert len(output) == 64
#
# The length of the output.txt file is actually 65 characters
# (due to the newline character at the end of the file),
# which means that all our code won't work, since it relies on
# the length of the string being exactly 64 characters, so
# we rebuild the string to exclude the newline
output = output[:-1]

# The first thing we need to do is undo this code:
#
# print(x[1::2] + x[0::2])
#
# This means that the last operation on the flag string was
# splitting the string into two parts: all the even-numbered characters
# (x[1::2]), concatenated to all the odd-numbered characters (x[0::2])
#
# To reverse this, first we need to split the string into two parts
# with the same number of characters
even_half = output[0:32]
odd_half = output[32:]

# Then we need to recreate the string by taking the first character of
# the odd half and pairing it with the first character of the even half
# repeating the process with the second pairs, the third pairs, etc, etc,
# until all 32 pairs have been accounted for
restored_str = "".join(a + b for a, b in zip(odd_half, even_half))

# The next part of the original script we need to reverse is this:
#
# x = "".join([
#    flag[-8::-8],
#    flag[-7::-8],
#    flag[-6::-8],
#    flag[-5::-8],
#    flag[-4::-8],
#    flag[-3::-8],
#    flag[-2::-8],
#    flag[-1::-8],
# ])
#
# This code takes the character that is 8th from the last position
# in the string, then adds the next character 8 characters back from
# that character until we reach the beginning of the string (flag[-8::-8])
# Then we do the same thing, but starting with the character that is 7th
# from the end, skipping back 8 characters and adding the character in
# that position until we get to beginning of the string.
# This process is repeated with the character 6th from the end, 5th from
# the end, etc, etc, until we have eight sets of characters.
#
# So to reverse this process, we have to separate the string into eight
# evenly-sized chunks
chunk1 = restored_str[0:8]
chunk2 = restored_str[8:16]
chunk3 = restored_str[16:24]
chunk4 = restored_str[24:32]
chunk5 = restored_str[32:40]
chunk6 = restored_str[40:48]
chunk7 = restored_str[48:56]
chunk8 = restored_str[56:]

# But the characters in the chunks are in reverse order from where we
# want them, so the next step is to reverse all the chunk strings
rev_chunk1 = chunk1[::-1]
rev_chunk2 = chunk2[::-1]
rev_chunk3 = chunk3[::-1]
rev_chunk4 = chunk4[::-1]
rev_chunk5 = chunk5[::-1]
rev_chunk6 = chunk6[::-1]
rev_chunk7 = chunk7[::-1]
rev_chunk8 = chunk8[::-1]

# Then restore the order of the original flag string by using
# the same code we used to construct the string by adding the first
# sets of characters from each chunk, then the second sets of
# characters, etc, etc, until all the sets are accounted for
flag = "".join(a + b + c + d + e + f + g + h for a, b, c, d, e, f, g, h in zip(rev_chunk1, rev_chunk2, rev_chunk3, rev_chunk4, rev_chunk5, rev_chunk6, rev_chunk7, rev_chunk8))
 
# Finally, we print the flag
print(flag)
```



