import turtle


class MyTurtle(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.left(90)
        self.goto(0, -300)

    def up(self):
        self.forward(20)

    def down(self):
        self.forward(-20)

    def verify_end(self):
        if self.ycor() > 280:
            self.goto(0, -300)
            return True