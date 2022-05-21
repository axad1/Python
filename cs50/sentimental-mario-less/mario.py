# TODO
import cs50

# input height with do-while loop
while True:
    n = cs50.get_int("Height: ")
    if n < 1 or n > 8:
        print("Invalid")
        continue
    break

# rows
for i in range(n):
    # spaces
    for j in range(n-1, i, -1):
        print("*", end="")
    # symbol
    for j in range(i+1):
        print("#", end="")
    # new-line
    print()