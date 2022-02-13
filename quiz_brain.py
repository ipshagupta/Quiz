class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f'Q.{self.question_number + 1}. {current_question.question} (True/False)?:    ')
        self.question_number += 1
        self.check_answer(user_answer, current_question)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, current_question):
        if user_answer == current_question.correct_answer:
            self.score += 1
            print(f"Correct! Your score:  {self.score} / {self.question_number}\n")
        elif user_answer != current_question.correct_answer:
            print(f"That was wrong! Your score:  {self.score} / {self.question_number}\n")
