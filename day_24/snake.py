## Turtle GUI
import turtle

UP = 90
DOWN = -90
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        self.snake_body = self.create_snake()
        self.head = self.snake_body[0]
        self.direction = "right"
        self.turtle_score = self.head.clone()
        self.turtle_score.goto(0 , 240)
        self.turtle_score.hideturtle()
        self.score = 0

        with open("./day_24/max_score.txt", mode="r") as file:
            max_score = file.read()
        self.higher_score = int(max_score)
        
        self.turtle_score.write(f"Current Score: {self.score}\nHigher Score: {self.higher_score}", align="center", font=("Arial", 18, "normal"))

    def create_snake(self):
        square1 = turtle.Turtle(shape="square")
        square1.color("white")
        square1.penup()
        square2 = square1.clone()
        square2.forward(-20)
        square3 = square1.clone()
        square3.forward(-40)

        return([square1, square2, square3])

    def move(self):
        for square_id in range(len(self.snake_body)-1, 0, -1):
            self.snake_body[square_id].goto(self.snake_body[square_id-1].xcor(), self.snake_body[square_id-1].ycor())
        self.head.forward(20)

    def eat_a_food(self):
        self.score += 1
        new_square = self.snake_body[-1].clone()
        self.snake_body.append(new_square)
        self.update_score()

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
        
        if self.score > self.higher_score:
            self.higher_score = self.score
        self.score = 0
        self.update_score()

        with open("./day_24/max_score.txt", mode="w") as file:
            file.write(str(self.higher_score))

        # Game over
        #self.turtle_score.write(f"Game Over\npress Enter to restart", align="center", font=("Arial", 18, "normal"))
        #input()
        self.reset_snake()

    def reset_snake(self):
        for squares in self.snake_body:
            squares.goto(1000,1000)
        self.snake_body.clear()
        self.snake_body = self.create_snake()
        self.head = self.snake_body[0]

    def update_score(self):
        self.turtle_score.clear()
        self.turtle_score.write(f"Current Score: {self.score}\nHigher Score: {self.higher_score}", align="center", font=("Arial", 18, "normal"))

    def get_snake_position(self):
        pos = []
        for square in self.snake_body[1:]:
            pos.append(square.pos())

        return pos




