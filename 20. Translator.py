# Giraffe Language
# vowels -> g

def translate(phrase):
    str = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                str += "G"
            else:
                str += "g"
        else:
            str += letter
    return str

print(translate(input("Enter phrase: ")))