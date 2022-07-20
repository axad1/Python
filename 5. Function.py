# lowercase or underscore_

def func():
    print("Hi!")

# Default Parameter Value
def func4(country = "Norway"):
    pass

# You can also send arguments with the key = value
# This way the order of the arguments does not matter
def func2(child3, child2, child1):
    pass
func2(child3 = "Linus", child1 = "Emil", child2 = "Tobias")

# ------------------

# Arbitrary Arguments, *args
# function will receive a tuple of arguments
def func1(one, *kids):
    pass
func1("Emil", "Tobias", "Linus")

# Arbitrary Keyword Arguments, **kwargs
# function will receive a dictionary of arguments
def func3(**kid):
    pass
func3(fname = "Tobias", lname = "Refsnes")

# A lambda function is a small anonymous function.
# can take any number of arguments, but can only have one expression.
x = lambda a : a + 10
print(x(5))

string ='GeeksforGeeks'
# lambda returns a function object
print(lambda string : string)

x ="GeeksforGeeks"
# lambda gets pass to print
(lambda n : print(n))(x)