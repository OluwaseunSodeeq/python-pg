
class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        # print(f"current_question : {current_question}")
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.question} \n(True or False) ? ").capitalize()
        print(user_answer)
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print(f"{user_answer} is Correct! Your score is now {self.score} / {self.question_number} " )
        else:
            print(f"Sorry,{user_answer} is incorrect. \n The correct answer was {correct_answer}.")
        print("\n")

        
