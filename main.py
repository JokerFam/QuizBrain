import question_model
import data

questions = []

for question in data.question_data:
    questions.append(question_model.Questions(
        question['text'], question['answer']))

print(questions)
