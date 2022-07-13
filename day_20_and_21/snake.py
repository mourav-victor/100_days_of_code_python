## Turtle GUI
import turtle

UP = 90
DOWN = -90
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        square1 = turtle.Turtle(shape="square")
        square1.color("white")
        square1.penup()
        square2 = square1.clone()
        square2.forward(-20)
        square3 = square1.clone()
        square3.forward(-40)
        self.snake_body = [square1, square2, square3]
        self.head = square1
        self.direction = "right"
        self.turtle_score = self.head.clone()
        self.turtle_score.goto(0 , 270)
        self.turtle_score.hideturtle()
        self.score = 0
        
        self.turtle_score.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def move(self):
        for square_id in range(len(self.snake_body)-1, 0, -1):
            self.snake_body[square_id].goto(self.snake_body[square_id-1].xcor(), self.snake_body[square_id-1].ycor())
        self.head.forward(20)

    def eat_a_food(self):
        self.score += 1
        new_square = self.snake_body[-1].clone()
        self.snake_body.append(new_square)
        self.turtle_score.clear()
        self.turtle_score.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def up(self):
        if self.direction != "down":
            self.head.setheading(UP)
            self.direction = "up"

    def down(self):
        if self.direction != "up":
            self.head.setheading(DOWN)
            self.direction = "down"

    def left(self):
        if self.direction != "right":
            self.head.setheading(LEFT)
            self.direction = "left"

    def right(self):
        if self.direction != "left":
            self.head.setheading(RIGHT)
            self.direction = "right"

    def snake_is_dead(self):
        self.turtle_score.goto(0,0)
        self.turtle_score.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def get_snake_position(self):
        pos = []
        for square in self.snake_body[1:]:
            pos.append(square.pos())

        return pos




