import turtle
import random

class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.8, stretch_wid = 0.8)
        self.color("blue")
        self.speed("fastest")
        self.change_location()
        

    def change_location(self):
        self.goto((random.randint(-180, 180), random.randint(-140, 140)))