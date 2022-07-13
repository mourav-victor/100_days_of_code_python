import turtle
import random

class Paddle(turtle.Turtle):

    def __init__(self, player):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len = 5, stretch_wid = 1)
        self.color("white")
        self.speed("fastest")
        self.left(90)
        

        if player == "p1":
            self.goto(-300, 0)

        if player == "p2":
            self.goto(300, 0)

    
    def up(self):
        if self.verify_limits("up"):
            self.forward(20)

    def down(self):
        if self.verify_limits("down"):
            self.backward(20)

    def verify_limits(self, side):
        if(side == "up"):
            if (self.ycor() < 300):
                return True

        if(side == "down"):
            if (self.ycor() > -300):
                return True

        return False
    
    def print_position(self):
        print(self.pos())