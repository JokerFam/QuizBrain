class QuizBrain(object):
    def __init__(self, q_list):
        self.question_number = 1
        self.question_list = q_list

    def quiz(self):
        ans = input(
            f'Q{self.question_number}. {self.question_list[self.question_number-1]} (True/False)')
