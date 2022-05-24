'''
Coleman-Liau index is computed as 0.0588 * L - 0.296 * S - 15.8,
where L is the average number of letters per 100 words in the text,
and S is the average number of sentences per 100 words in the text.
'''
# todo
import cs50
text = cs50.get_string("Text: ")

letters = 0
words = 1
sentences = 0

for i in text:
    if i.isalpha():
        letters += 1
    if i == ' ':
        words += 1
    if i == '.' or i == '?' or i == '!':
        sentences += 1

S = (sentences / words) * 100
L = (letters / words) * 100
index = 0.0588 * L - 0.296 * S - 15.8

if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print("Grade " + str(round(index)))
