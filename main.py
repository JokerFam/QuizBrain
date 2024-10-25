import question_model
import data
import quiz_brain

questions = []

for question in data.question_data:
    questions.append(question_model.Questions(
        question['text'], question['answer']))

quiz = quiz_brain.QuizBrain(questions)
run = True

while run:
    quiz.quiz()
