import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
number = "0123456789"
symbols = "!@#$%^&*()"

string = lower + upper + number + symbols

password = "".join(random.sample(string, 8))

print(password)
