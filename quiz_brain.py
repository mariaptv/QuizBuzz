class QuizBrain:

    def __init__(self, question_list):
        self.question_number =0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/false)")
        correct_answer = current_question.answer
        if answer == correct_answer:
            print("You have it correct")
            return True
        else:
            print("You are wrong")
            return False

