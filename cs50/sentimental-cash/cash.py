# TODO
import cs50

# get dollars
while True:
    dollar = cs50.get_float("How many dollars you owe? : ")
    if dollar > 0:
        break
    continue

cents = int(dollar * 100)

quarters = cents / 25
cents = cents - int(quarters) * 25

dimes = cents / 10
cents = cents - int(dimes) * 10

nickels = cents / 5
cents = cents - int(nickels) * 5

coins = int(quarters) + int(dimes) + int(nickels) + int(cents)

print(int(coins))