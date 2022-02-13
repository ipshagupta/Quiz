from question_model import Question
from data_film import question_data_film
from quiz_brain import QuizBrain
from data_music import question_data_music

question_bank = []

choice = input("Choose the type of trivia from below\n1. Music\n2. Film\n-> Your choice:    ").lower()
if choice == "music":
    for question in question_data_music:
        new_q = Question(question['question'], question['correct_answer'])
        question_bank.append(new_q)

elif choice == "film":
    for question in question_data_film:
        new_q = Question(question['question'], question['correct_answer'])
        question_bank.append(new_q)

print("\nQuiz starts now!\n")

q = QuizBrain(question_bank)

while q.still_has_questions():
    q.next_question()

print(f"\nThe quiz has ended. Your final score is: {q.score} out of {len(question_bank)}!!")
