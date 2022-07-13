import turtle
import random

y_cord = [x*20-200 for x in range(1,22)]
colors = ["black", "red", "blue", "green", "magenta", "indigo", "yellow", "purple"]

class Car(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len = 2, stretch_wid = 1)
        self.color(random.choice(colors))
        self.penup()
        self.goto(300, random.choice(y_cord))

    def move(self):
        self.forward(-10)

    def verify_colision(self, turtle):
        if self.ycor() == turtle.ycor():
            if self.distance(turtle) < 20:
                return True
        
    