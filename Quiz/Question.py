from app import Question

question_prompt = [
    "What color of apples?\n(a) Red/Green\n(b) Blue\n(c) Orange\n\n",
    "What is capital of united state?\n(a) New York\n(b) Florida\n(c) San Francisco\n\n",
    "How many faces in the die?\n(a) 5\n(b) 7\n(c) 6\n\n",
]


questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "a"),
    Question(question_prompt[2], "c"),
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        
        if answer == question.answer:
            score += 1
    print("You got  " + str(score) + "/ " + str(len(questions)) + " correct")

run_quiz(questions)