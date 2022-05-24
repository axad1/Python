import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        return

    # Read database file into a variable
    db = open(sys.argv[1], "r")
    reader = csv.DictReader(db)

    # store every person's data into list
    people = []
    for row in reader:
        people.append(row)

    # copy STR names from 1st row except 1st item "name"
    fields = reader.fieldnames[1:]
    # close db
    db.close()

    # create dictionary for STR's and assign value 0 to every key
    STRs = {
        i : 0 for i in fields
    }

    # Read DNA sequence file into a variable
    dna_file = open(sys.argv[2], "r")
    dna = dna_file.read()

    # close dna_file
    dna_file.close()

    # Find longest match of each STR in DNA sequence
    for key in STRs:
        STRs[key] = longest_match(dna, key)

    # Check database for matching profiles
    for p in people:
        match = 0
        # check if key matches
        for key in STRs:
            if int(p[key]) == STRs[key]:
                match += 1

        # if all STR's are matching
        if match == len(STRs):
            print(p['name'])
            return

    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()