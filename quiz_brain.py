class QuizBrain(object):
    def __init__(self, q_list):
        self.question_number = 1
        self.question_list = q_list
        self.score = 0

    def quiz(self):
        user_answer = input(
            f'Q.{self.question_number}: {self.question_list[self.question_number-1].question} (True/False)? ')
        if self.check_answer(
                user_answer, self.question_list[self.question_number-1].answer) == True:
            print('You got it right!')
            self.score += 1
        else:
            print('That is wrong.')

    def still_has_a_question(self):
        if len(self.question_list) == (self.question_number-1):
            return False
        else:
            self.quiz()
            self.question_number += 1
            return True

    def check_answer(self, user_answer, correct_answer):
        return user_answer.lower() == correct_answer.lower()

    def report(self):
        print(f'Your score is {self.score}.')
