from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_bank = []
for q in question_data:
    question_bank.append(Question(q["question"], q["answer"]))

quiz = Quiz(question_bank)

while quiz.has_next_question():
    quiz.next_question()
print(f"Your Final Score {quiz.score}")
