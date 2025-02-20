from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Angela's Approach
question_bank= []
for each_question in question_data:
    # print(each_question)
    new_question = Question(each_question["text"],each_question["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(" you've completed the quiz")
print(f"Your final score is {quiz.score} / {len(question_bank)}")


# My Approach
# question_bank= []
# score = 0
# for each_question in question_data:
#     # print(each_question)
#     new_question = Question(each_question["text"],each_question["answer"])
#     user_answer = input(f"{new_question.question} \n True or False ").capitalize()
#     question_bank.append(new_question)

#     if user_answer == new_question.answer:
#         print("Correct")
#         score += 1
#     else:
#         print(f"Sorry, that's incorrect. The correct answer is {new_question.answer}.")
#     print(f"You got {score}/{len(question_data)}")
    # print(f"{each_question["id"]} : {new_question.question} \n {new_question.answer}")
