# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# do-While loop
i = 0
while True:
    i += 1
    if i > 5:
        break
    print(i)
    continue

# For In loop with Strings
for i in "Hello World":
    print(i)
# iterate list
l = ["Jim", "Asad", "Kamira"]
for i in l:
    print(i)

# For Loop with Range()
for i in range(len(l)):
    print(l[i])

# for i in range(start, end, increment)

# list Comprehension for loop
l = ["apple", "banana", "cherry"]
# print
[print(x) for x in l]

# The pass Statement
# for loops cannot be empty
for x in [0, 1, 2]:
  pass