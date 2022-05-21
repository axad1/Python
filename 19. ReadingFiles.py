# modes
'''
r - read only
w - write only
a - append only no read
r+ - read + write
'''
# open file
file = open("asad.txt", "r")

# check if readable return True/False
print(file.readable())
# check if writeable
print(file.writable())

# read individual line
print(file.readline())

# read all lines and put them in list
li = file.readlines()

# read complete the file
print(file.read())

# close file
file.close()