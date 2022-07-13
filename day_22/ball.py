import turtle
import random

#VERTICAL_PACE = 5
HORIZONTAL_PACE = 5
RESET_IN_CENTER = True

class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 1, stretch_wid = 1)
        self.color("white")
        self.up_pace = 5
        self.right_pace = HORIZONTAL_PACE

    def move(self):
        self.wall_collision()
        #self.side_collision()
        self.goto(self.xcor() + self.right_pace, self.ycor() + self.up_pace)

    def wall_collision(self):
        if (self.ycor() > 300):
            self.up_pace = -abs(self.up_pace)
    
        if (self.ycor() < -300):
            self.up_pace = abs(self.up_pace)

    def side_collision(self, score):
        if (self.xcor() > 350):
            self.right_pace = -HORIZONTAL_PACE
            score.update_score("p2")
            self.reset_position()
    
        if (self.xcor() < -350):
            self.right_pace = HORIZONTAL_PACE
            score.update_score("p1")
            self.reset_position()
    
    def paddle_collision(self, paddle_1, paddle_2):
        if (self.xcor() >= 280 and self.xcor() <= 300 and self.distance(paddle_2) < 60):
            self.right_pace = -HORIZONTAL_PACE
            self.update_angle()

        if (self.xcor() <= -280 and self.xcor() >= -300 and self.distance(paddle_1) < 60):
            self.right_pace = HORIZONTAL_PACE
            self.update_angle()

    def update_angle(self):
        self.up_pace = random.randint(1,10)
        if(random.choice([True, False])):
            self.up_pace *= -1

    def reset_position(self):
        if(RESET_IN_CENTER):
            self.goto(0, 0)


    def print_position(self):
        print(self.pos())