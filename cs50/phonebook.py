import csv
from cs50 import get_string

file = open("asad.csv", "w")

name = get_string("name: ")
number = get_string("number: ")

writer = csv.writer(file)
writer.writerow([name,number])
writer.writerow([name,number])

file.close()