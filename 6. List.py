# list() Constructor
l2 = list(("apple", "banana", "cherry")) # note the double round-brackets

# List
l = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

# Negative Indexing
l[-1]

# change value
l[1] = "Mike"

# Range of Indexes
l[1:3]
l[:3]
l[2:]
l[-4:-1]

# length
len(l)

# Check if Item Exists
if "Mike" in l:
    print("yes")

# Change a Range or Insert New Items
l[1:3] = ["blackcurrant", "watermelon"]
