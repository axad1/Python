class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

questions = [
    "What color are apples?\n(a) Red\n(b) Purple\n(c) Orange\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n"
]

quiz = [
    Question(questions[0], 'a'),
    Question(questions[1], 'c'),
    Question(questions[2], 'b')
]

def test():
    score = 0
    for q in quiz:
        answer = input(q.question)
        if answer == q.answer: score+=1
    print("You got " + str(score) + "/" + str(len(quiz)) + " scores")


test()