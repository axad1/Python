try:
    value = 10/0
    n = int(input("Enter a number: "))

# zero division error
except ZeroDivisionError:
    print("Divided by zero")

# except value error
except ValueError:
    print("value error")

# excepts all
except:
    print("exception error")