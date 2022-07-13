import turtle

class Level(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-300 , 260)
        self.level = 1
        self.speed = 0.1

        self.write(f"Level: {self.level}", align="center", font=("Arial", 20, "normal"))

    def update_level(self):
        self.level += 1
        self.speed *= 0.8
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0 , 0)
        self.write(f"GAME OVER\nfinal score:  {self.level}", align="center", font=("Arial", 20, "normal"))
        
    