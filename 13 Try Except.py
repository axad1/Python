# Try block
try:
    value = 10/0
    n = int(input("Enter a number: "))

# ------------
# Many Except blocks

except NameError:
  print("Variable x is not defined")

except ZeroDivisionError:
    print("Divided by zero")

except ValueError:
    print("Value Error")

# excepts all
except:
    print("Something else")

# -------------
# Else block
# if no errors were raised
else:
    print("All went good")
    
# ----------------

# Raise an exception
# you can  throw an exception if a condition occurs.
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

# ----------------

# Finally block
# executes whether error raises or not
finally:
  print("The 'try except' is finished")