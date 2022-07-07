# Looping Using List Comprehension
# A short hand for loop that will print all items in a list:

# newlist = [expression for item in iterable if condition == True]

l = ["apple", "banana", "cherry"]
[print(x.upper()) for x in l]

newlist = [x for x in range(10) if x < 5]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newfruits = [x if x != "banana" else "orange" for x in fruits]
print(newfruits)