# An iterator is an object that can be iterated upon and
# implements the iterator protocol, which consist of the methods __iter__() and __next__().

# Strings, lists, tuples, dictionaries, and sets are all iterable objects,
# They have an iter() method which is used to get an iterator.

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))

# --------------------

# Iterate a class or object

class MyNumbers:
  # implement __iter__ method
  def __iter__(self):
    self.a = 1
    return self

  # implement __next__ method
  def __next__(self):
    if self.a <= 10:
      x = self.a
      self.a += 1
      return x
    else:
      # stop iteration statement
      raise StopIteration


myiter = iter(MyNumbers())
print(next(myiter))
print(next(myiter))

# We can also use a for in loop to iterate through an iterable object.
# The for in loop actually creates an iterator object,
# and executes the next() method for each loop.
for x in MyNumbers():
  print(x, end='\t')