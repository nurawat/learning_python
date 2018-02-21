#
# Create a program that takes some text and return alist of all the character in the text that are not vowels,
# sorted in alphabetical OrderedDictionary  you can either enter the text from the keyboard
# or initialise a stirng variable with the string
#


# Ussing sets

__author__ = 'nurawat'

text = "this is arun"

vowels = frozenset("aeiou")

nonVowelList = set(text).difference(vowels)
print(sorted(nonVowelList))
