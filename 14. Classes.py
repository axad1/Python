# (self parameter is a reference to the current instance of the class,
# It is used to access variables that belongs to the class
# It does not have to be named self , but should be first)

class MyClass:
    # The __init__() Function like Constructor
    def __init__(self):
        pass
    x = "Hi!"
    y = lambda self: "This is me"

# Create Object
obj = MyClass()

# Delete Class Properties
del MyClass.x

# -----------------

# Python Inheritance

# Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# Create a Child Class
class Student(Person):
    # When you add the __init__(),
    # the child class will no longer inherit the parent's __init__()
    # To keep the inheritance of the parent's __init__(),
    # add a call to the parent's __init__()
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

# Or Use the super() Function

class Student2(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)