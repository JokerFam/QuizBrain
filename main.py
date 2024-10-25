import question_model
import data
import quiz_brain

questions = []

for question in data.question_data:
    questions.append(question_model.Questions(
        question['text'], question['answer']))

quizz = quiz_brain.QuizBrain(questions)
run = True

while run:
    try:
        run = quizz.still_has_a_question()
    except IndexError as e:
        run = False

quizz.report()
