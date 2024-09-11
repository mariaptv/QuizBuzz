from QuizBuzz.quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []

for i in question_data:
    qa = Question(i.get("text"), i.get("answer"))
    question_bank.append(qa)

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