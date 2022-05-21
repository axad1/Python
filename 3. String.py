# strings are immutable in python

s = "HELLO WORLD"
# convert to lower
print(s.lower())
# convert to upper
print(s.upper())
# check if upper
print(s.isupper())
# length + typecast to s
print("length = " + str(len(s)))
# return index of searched letter
print(s.index("R"))
# replace
print(s.replace("WORLD", "PYTHON"))