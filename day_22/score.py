import turtle
import random

class Score(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0 , 240)
        
        self.score = [0, 0]
        self.write(f"Score:\n{self.score[0]} vs {self.score[1]}", align="center", font=("Arial", 24, "normal"))

    def update_score(self, player):
        if player == "p1":
            self.score[0] += 1
        if player == "p2":
            self.score[1] += 1
        self.clear()
        self.write(f"Score:\n{self.score[0]} vs {self.score[1]}", align="center", font=("Arial", 24, "normal"))
        
    