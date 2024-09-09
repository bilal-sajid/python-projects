from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    current_text = item["question"]
    current_answer = item["correct_answer"]
    question_bank.append(Question(current_text, current_answer))

# print(question_bank)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    print()
    quiz.next_question()

print()
print("You've completed the Quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")