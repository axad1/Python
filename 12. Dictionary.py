# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# store data values in key:value pairs
#  curly brackets

# Accessing Items
dic = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# by referring to key name, inside square brackets
x = dic["model"]
# get()
x = dic.get("model")

# Get Keys
x = dic.keys()
# or
for key in dic:
    print(key)
for x in dic.keys():
    print(x)

# Get Values
x = dic.values()
for i in dic:
    print(dic[i])
for x in dic.values():
    print(x)

# Get Items, as a list of tuples
x = dic.items()
for x, y in dic.items():
  print(x, y)

# Check if Key Exists
if "model" in dic:
    print("Yes")

# Get default if key not found
dic.get("luv", "Not a valid key")

# -----------------

# Add New index key and value
dic["color"] = 'red'

# Change Values update
# If the item does not exist, the item will be added
dic.update({"year": 2020})

# -----------------

# Removes the last inserted item
dic.popitem()
# Removing Items
dic.pop("model")
del dic["year"]

# Empties the dictionary
dic.clear()
del dic

# ----------------

# Make copy
mydict = dic.copy()
mydict2 = dict(dic)

# Dictionary Length
len(dict)
