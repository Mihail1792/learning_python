#An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).
#Note: anagrams are case insensitive
#Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

import typing
def anagram(s: str,s1: str) ->typing.Optional[bool]:
    s = set(s)
    s1 = set(s1)
    return s ==s1


print(anagram("tanunay", "aanntyu"))