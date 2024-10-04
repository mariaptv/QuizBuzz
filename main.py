

from QuizBuzz.quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []

for i in question_data:
    question_text = Question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

end_game = False

while end_game == False:
    if quiz.still_has_questions() == False:
        end_game == True
    else:
        answer = quiz.next_question()
        if answer :
            quiz.question_number += 1
        else:
            end_game = True