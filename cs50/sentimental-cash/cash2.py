import cs50

# get dollars
while True:
    dollar = cs50.get_float("How many dollars you owe? : ")
    if dollar > 0:
        break
    continue

cents = round(int(dollar * 100))
coins = 0

# for every coin sorted, the counter +1
while cents > 0:
    while cents >= 25:
        coins += 1
        cents -= 25
    while cents >= 10:
        coins += 1
        cents -= 10
    while cents >= 5:
        coins += 1
        cents -= 5
    while cents >= 1:
        cents -= 1
        coins += 1
print(coins)