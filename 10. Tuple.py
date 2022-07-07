# A tuple is a collection which is ordered and unchangeable.
# tuples are immutable or not changeable
# round brackets
# Allow Duplicates

# tuple() Constructor
t = tuple(("apple", "banana", "cherry")) # note the double round-brackets

# To create a tuple with only one item
# you have to add a comma after the item
t2 = ("apple",)

# Access Range
t[0]
t[0:]
t[:3]
t[-1]

# Count the item
t.count('apple')

# Check if Item Exists
if "apple" in t:
    print("yes")

# length
len(t)

# index() method finds the first occurrence of the specified value.
t.index('apple')

# --------------

# You can't change tuple
# convert into list and convert the list back into a tuple.

# change
# append
# remove
l = list(t)
t = tuple(l)


# Join tuple
t = t1 + t2
# Multiply Tuples
t = t * 2

# delete the tuple
del t

# ------------

# Unpacking a Tuple
fruits = ("apple", "banana", "cherry", 'grapes')
(one, two) = fruits
# use * asterisk to collect the remaining values as a list
(*three) = fruits
# Python will assign values to the *variable until
# the number of values left matches the number of variables left
(a, *b, c) = fruits
