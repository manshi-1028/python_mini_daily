from question_model import Question
from data import question_data
from quiz_brain import Quizbrain
question_bank=[]
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))
quiz = Quizbrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print(f"your final score is {quiz.score}/{quiz.question_number}")