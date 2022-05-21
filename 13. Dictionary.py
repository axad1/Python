# key value pairs
# key should be unique

month = {
    'jan': "January",
    'feb': "February",
    'mar': "March",
    'apr': "April",
    'may': "May",
    'jun': "June",
    'jul': "July",
    'aug': "August",
    'sep': "September",
    'oct': "October",
    'nov': "November",
    'dec': "December"
}

# get
print(month["jan"])
print(month.get("dec"))

# print default if key not found
print(month.get("luv", "Not a valid key"))

# get all keys
for i in month:
    print(i)

# get all values
for i in month:
    print(month[i])

# search
name = "mar"
if name in month:
    print(f"found = {month[name]}")
