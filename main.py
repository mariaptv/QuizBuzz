from QuizBuzz.quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []

for i in question_data:
    qa = Question(i.get("text"), i.get("answer"))
    question_bank.append(qa)

quiz = QuizBrain(question_bank)