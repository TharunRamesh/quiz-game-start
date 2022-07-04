from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_Bank = []
for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    new_q = Question(text, answer)
    question_Bank.append(new_q)
print(question_Bank)

new_quizbrain = QuizBrain(question_Bank)
while new_quizbrain.still_has_questions():
    new_quizbrain.next_question()
print("you have completed the quiz")
print(f"your final score is: {new_quizbrain.score}/{new_quizbrain.question_number}")
