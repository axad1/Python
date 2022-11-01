import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# Parse JSON - to Python Dictionary
y = json.loads(x)

# ------------------

# Python to JSON
x = json.dumps(y)

# Use the indent parameter to define the numbers of indents
x = json.dumps(y, indent=4)

# Use the separators, default value is (", ", ": ")
# item separator, key separator
x = json.dumps(y, separators=(". "," = "))

# Order the Result
x = json.dumps(y, sort_keys=True)



# -----------------
json.dumps({"name": "John", "age": 30})  # dict
json.dumps(["apple", "bananas"])         # list
json.dumps(("apple", "bananas"))         # tuple
json.dumps("hello")      # str
json.dumps(42)           # int
json.dumps(31.76)        # float
json.dumps(True)     # True
json.dumps(False)    # False
json.dumps(None)     # None
