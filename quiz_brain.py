class QuizBrain(object):
    def __init__(self, q_list):
        self.question_number = 1
        self.question_list = q_list

    def quiz(self):
        input(
            f'Q.{self.question_number}: {self.question_list[self.question_number-1].question} (True/False)? ')

    def still_has_a_question(self):
        if len(self.question_list) == (self.question_number-1):
            return False
        else:
            self.quiz()
            self.question_number += 1
            return True
