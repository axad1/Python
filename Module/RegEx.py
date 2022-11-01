# re, work with Regular Expressions
import re

# Expressions
# ^ starts with
# $ ends with
# *	Zero or more occurrences
# +	One or more occurrences
# ?	Zero or one occurrences
# .	Any character (except newline character)


# Search the string, starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

# ---------------
# RegEx Functions

# print("The findall() Function")
# Returns a list containing all matches
x = re.findall("ai", txt)

# ---------------

# print("The search() Function")
# Returns a Match object
x = re.search("\s", txt)
# print("The first white-space character is located in position:", x.start())

# ---------------

# print("The split() Function")
# Returns a list where the string has been split at each match
x = re.split("in", txt)
# control the number of occurrences by specifying the maxsplit parameter
x = re.split("\s", txt, 1)

# ---------------

# print("The sub() Function")
# Replaces one or many matches with a string
x = re.sub("\s", "9", txt)
# control the number of replacements by count parameter:
x = re.sub("\s", "9", txt, 2)

# ---------------

# Match Object
# An object containing information about the search and the result.
# If there is no match, the value will be None

# Properties and methods of match object
# .string returns the string passed into the function.
# .span() returns a tuple containing the start-, and end positions of the match.
# .group() returns the part of the string where there was a match.
# .start(), .end()
