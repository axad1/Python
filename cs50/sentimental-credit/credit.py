# TODO
import sys
import cs50

# get card
card = cs50.get_int("Number: ")
# calculate length
length = len(str(card))
# check for length
if length != 13 and length != 15 and length != 16:
    print("INVALID")
    sys.exit(0)
# copy card
x = card
sum1 = sum2 = 0
# in every loop 2 digits will be ommited
# loop x till length/2
for i in range(int(length/2+1)):
    # get last digit
    m1 = x % 10
    # add into sum1
    sum1 = sum1 + m1

    # ommit that last digit
    x = int(x / 10)

    # get get last digit
    m2 = x % 10
    # multiply this digit
    m2 = m2 * 2

    # ommit that last digit
    x = int(x / 10)
    
    # after multiply if we get two digit number then separate them
    d1 = int(m2 / 10)
    d2 = m2 % 10

    # add the sum of these digits to sum2
    sum2 = sum2 + d1 + d2

# make total of both sums
total = sum1 + sum2

# checksum according to luhn's law that last digit should be zero
if total % 10 != 0:
    print("INVALID")
    sys.exit(0)

# copy card into string
x = str(card)
# take first two digits
first = int(x[0])
second = int(x[1])

# check for conditions
if first == 5 and (second >= 1 and second <= 5):
    print("MASTERCARD")
    sys.exit(0)

if first == 3 and (second == 4 or second == 7):
    print("AMEX")
    sys.exit()

if first == 4:
    print("VISA")
    sys.exit()

print("INVALID")