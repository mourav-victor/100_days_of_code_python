## A true/false quiz game
import data

class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def print_question(self):
        print(f"{self.text}. (True or False): ")

    def ask_question(self):
        ans = input(f"{self.text}. (True or False): ")
        if(ans == self.answer or ans == (self.answer).lower() or ans == (self.answer[0]).lower()):
            print("Yeah, you are right!\n")
            return True
        return False
## -------------------------------

class Quiz:

    def __init__(self, questions):
        self.questions = questions
        self.nb_of_questions = len(questions)
        self.score = 0


    def print_all_questions(self):
        for item in self.questions:
            print(item.text)

    def print_score(self):
        print(f"Your current score is: {self.score}\n")

    def play(self):
        while(self.score < self.nb_of_questions):
            ans = input(f"Q.{self.score+1}: {self.questions[self.score].text}. (True/False): ")
            right_ans = self.questions[self.score].answer
            if(ans == right_ans or ans == right_ans.lower() or ans == right_ans[0].lower()):
                self.score += 1
                print("You got it")
                self.print_score()
            else:
                print("You lost.")
                break
        
        print("Congrats, you beat us!")

#question_1 = Question("Jeff Bezzos is the richiest man alive", True)
#question_1.print_question()

question_list = [Question(x["text"], x["answer"]) for x in data.question_data]

# in_game = True
# question_nb = 0

# while(in_game):
#     in_game = question_list[question_nb].ask_question()
#     question_nb += 1

#     if(question_nb == len(question_list)):
#         print("You won! Congrats")
#         break

# print("You lost...")

my_quiz = Quiz(question_list)
my_quiz.play()