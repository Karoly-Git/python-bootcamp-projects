from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("\n🎉 You've completed the quiz!")
print(f"Your final score is: {quiz.score} out of {quiz.question_number}.")
print("Thanks for playing! 🚀")
