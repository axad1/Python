# greater number

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a>b and a>c:
    print("a is greater")
elif a>b and not a>c:
    print("c is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greater")

x = 5
y = 10

# Short if
# Ternary Operators, or Conditional Expressions
if x > y: print("a is greater than b")

# Short if-else
print("X") if x > y else print("=") if x == b else print("Y")

# The pass Statement
# if statements cannot be empty,
# but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.
if y > x:
    pass