import csv

with open("asad.csv", "r") as file:
    
    for i in csv.DictReader(file):
        print(i)


# no need to close file in this way