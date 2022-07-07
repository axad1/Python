# A set is a collection which is unordered, unchangeable*, and unindexed
# Duplicates Not Allowed
# curly brackets

# set() Constructor
set1 = set(("apple", "banana", "cherry")) # note the double round-brackets
# in constructor accepts only 1 argument

set2 = {"one", "two", "three"}

# Access
for x in set1:
    print(x)

# Check
print("banana" in set1)

# --------------

# Once a set is created, you cannot change its items, but you can add new items.

# Add item
set1.add('orange')
# Add Sets
set1.update(set2)
# The object in the update() can be Any Iterable

# --------------

# Remove Item

# remove
set1.remove('banana') # will raise an error
# discard
set1.discard('banana') # will NOT raise an error
set1.pop() # remove last

# Clear
set1.clear()

# Delete
del set2

# --------------

# Join sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

# union 
set3 = set1.union(set2)
# update
set1.update(set2)

# --------------

# Keep ONLY the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# intersection
z = x.intersection(y)
# intersection_update
x.intersection_update(y)

del x,y

# --------------

# Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# symmetric_difference
z = x.symmetric_difference(y)
# symmetric_difference_update
x.symmetric_difference_update(y)

# --------------

# Length
len(set1)

# copy
newset = x.copy()