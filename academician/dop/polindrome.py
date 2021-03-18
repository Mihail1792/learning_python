#A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. This includes capital letters, punctuation, and word dividers.
#Implement a function that checks if something is a palindrome.
import typing

def polindr(s: str) -> typing.Optional[bool]:
    s1 = s[::-1]
    return s == s1

print(polindr("annanna"))