# I want you to write a function that accepts two strings and returns True if the two strings are anagrams of each other.
from collections import Counter
import unicodedata

def is_anagram(string1, string2):

    # string1 = Counter([i.lower() for i in string1.strip() if i != " "]).items()
    # string2 =  Counter([i.lower() for i in string2.strip() if i != " "]).items()
    if Counter([i.lower() for i in ''.join(filter(str.isalpha, string1))]).items() == Counter([i.lower() for i in ''.join(filter(str.isalpha, string2))]).items():
        return True
    return False


print(is_anagram("tea", "eat"))
print(is_anagram("tea", "treat"))
print(is_anagram("Listen", "silent"))
print(is_anagram("coins kept", "in pockets"))
# print(is_anagram("cardiografía", "radiográfica"))
s = unicodedata.normalize('NFD', 'radiográfica')
print(s)