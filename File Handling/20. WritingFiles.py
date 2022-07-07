# append file
file = open("asad.txt", "w")

# check if writable
print(file.writable())

file.write("\nToby - Human Resources")
file.write("\nKelly - Customer Services")

# close file
file.close()