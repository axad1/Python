l = ["Jim", "Mike", "Toby", "Toby", "Kevin", "Karen"]

# append list on the end side
l.append("Creed")

# insert at an index
l.insert(1, "Kelly")

# get the index
l.index("Mike")

# count a specific element
l.count("Toby")

# ----------

# pop the last element or index
l.pop()
l.pop(3)

# remove
l.remove("Karen")

# del keyword removes the specified index
del l[1]
# The del keyword can also delete the list completely
# del l

# clear the list
l.clear()

# -----------

# Sort case sensitive
l.sort()
# Sort Descending
l.sort(reverse = True)
# case insensitive
l.sort(key = str.lower)

# reverse the order
l.reverse()

# -------------

# make copy
l.copy()

# make copy via list()
newlist = list(l)

# -------------

# Join list
list3 = list1 + list2

# extend list with Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)

# length
len(l)