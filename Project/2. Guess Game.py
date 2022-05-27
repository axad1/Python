import random
import sys

n = random.randint(1, 10)
for i in range(5):
    x = int
    try:
        x = int(input("Guess a number (1 to 10)\t" + str(i+1) + "): "))
    except ValueError:
        print("Input number only")
        sys.exit()
    if x<1 or x>10:
        print("Not in range")
        sys.exit(0)
    if x == n:
        print("You got it!")
        sys.exit()
    elif x > n:
        print("\tToo higher")
    else:
        print("\tToo lower")
    
print("Better luck next time")
print("Answer = " + str(n))