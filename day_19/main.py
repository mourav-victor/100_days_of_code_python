## Turtle GUI
import turtle
import random

# Configs
my_screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("DarkGreen")
my_screen.bgcolor("grey")
my_turtle.speed("slow")


print(my_turtle) 
print(f"{my_screen.canvwidth} x {my_screen.canvheight}")


def etch_a_sketch():
    def move_forwards():
        my_turtle.forward(10)
    def move_backwards():
        my_turtle.backward(10)
    def turn_left():
        my_turtle.left(15)
    def turn_right():
        my_turtle.right(15)

    my_screen.listen()
    my_screen.onkeypress(key="w", fun=move_forwards)
    my_screen.onkeypress(key="s", fun=move_backwards)
    my_screen.onkeypress(key="a", fun=turn_left)
    my_screen.onkeypress(key="d", fun=turn_right)
    my_screen.exitonclick()

def two_players_turtle_race():
    def p1_move_forwards():
        my_turtle.forward(10)
    def p2_move_forwards():
        his_turtle.forward(10)
    def set_trutles():
        my_turtle.penup()
        his_turtle.penup()
        my_turtle.setpos(-300,-20)
        his_turtle.setpos(-300,20)
        my_turtle.pendown()
        his_turtle.pendown()

    his_turtle = my_turtle.clone()
    his_turtle.color("Indigo")
    set_trutles()
    my_screen.listen()
    my_screen.onkeypress(key="w", fun=p1_move_forwards)
    my_screen.onkeypress(key="o", fun=p2_move_forwards)
    my_screen.exitonclick()

def random_turtle_race():
    my_screen.setup(width = 1000, height = 600)
    #user_bet = my_screen.textinput(title="TURTLE RACE", prompt="Who's gonna win?")

    my_turtle.penup()
    my_turtle2 = my_turtle.clone()
    my_turtle2.color("red")
    my_turtle3 = my_turtle.clone()
    my_turtle3.color("yellow")
    my_turtle4 = my_turtle.clone()
    my_turtle4.color("blue")
    my_turtle5 = my_turtle.clone()
    my_turtle5.color("indigo")
    my_turtle6 = my_turtle.clone()
    my_turtle6.color("purple")
    my_turtle.goto((-400,-100))
    my_turtle2.goto((-400,-60))
    my_turtle3.goto((-400,-20))
    my_turtle4.goto((-400, 20))
    my_turtle5.goto((-400, 60))
    my_turtle6.goto((-400,100))
    turtles = [my_turtle, my_turtle2, my_turtle3, my_turtle4, my_turtle5, my_turtle6]

    on_race = True
    while(on_race):
        my_turtle.forward(random.randint(1,10))
        my_turtle2.forward(random.randint(1,10))
        my_turtle3.forward(random.randint(1,10))
        my_turtle4.forward(random.randint(1,10))
        my_turtle5.forward(random.randint(1,10))
        my_turtle6.forward(random.randint(1,10))

        for turtle in turtles:
            if turtle.xcor() > 480:
                on_race = False
    
    my_screen.exitonclick()

#etch_a_sketch()
#two_players_turtle_race()
random_turtle_race()