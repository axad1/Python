n = [4, 8, 15]
l = ["Jim", "Mike", "Toby", "Toby", "Kevin", "Karen"]

# extend list with other list
n.extend(l)

# append list on the end side
l.append("Creed")

# insert at any index
l.insert(1, "Kelly")

# remove
l.remove("Jim")

# clear the list
n.clear()

# pop the last element
l.pop()

# get the index
i = l.index("Mike")

# count a specific element
c = l.count("Toby")

# sort
l.sort()

# make copy
l2 = l.copy()

# reverse the order
l.reverse()

print(n)
print(l2)
