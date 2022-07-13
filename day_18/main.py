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
colors = ["orange", "lime", "yellow", "blue", "red", "magenta", "saddle brown", "indigo"]
random_angle = [0, 90, 180, 270]

def ch1_draw_square(turtle, size):
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)

def ch2_dashed_line(turtle, size):
    for i in range(10):
        turtle.pendown()
        turtle.forward(size/20)
        turtle.penup()
        turtle.forward(size/20)

def ch3_draw_form(turtle, size, sides):
    angle = 360 / sides
    for i in range(sides):
        turtle.forward(size)
        turtle.left(angle)

def ch1_draw_square_dash(turtle, size):
    ch2_dashed_line(turtle, size)
    turtle.left(90)
    ch2_dashed_line(turtle, size)
    turtle.left(90)
    ch2_dashed_line(turtle, size)
    turtle.left(90)
    ch2_dashed_line(turtle, size)

def ch4_random_walk(turtle, size, number_of_steps):
    turtle.pensize(15)
    for i in range(number_of_steps):
        #turtle.pencolor(random.choice(colors))
        turtle.forward(size)
        turtle.setheading(random.choice(random_angle))

def ch5_random_path(turtle, size, number_of_steps):
    turtle.pensize(15)
    for i in range(number_of_steps):
        turtle.forward(size)
        turtle.left(random.choice(random_angle))

def ch6_spirograph(turtle, size, number_of_circles):
    angle = 360 / number_of_circles
    turtle.speed("fastest")
    for i in range(number_of_circles):
        turtle.circle(size)
        turtle.left(angle)
    
def final_project_art(turtle, radius, width, length, offset):
    #angle = 360 / number_of_circles
    turtle.speed("fastest")
    turtle.penup()
    turtle.sety(offset)
    turtle.setx(offset)
    for j in range(length):
        for i in range(width):
            turtle.pendown()
            turtle.dot(radius, random.choice(colors))
            turtle.penup()
            if i == width - 1:
                break
            turtle.forward(radius*3)
        
        if j % 2 == 0:
            angle = 90
        else:
            angle = 270
        turtle.left(angle)
        turtle.forward(radius*3)
        turtle.left(angle)
    



# Actions
while(False):
    my_turtle.forward(100)
    my_turtle.left(55)

#ch1_draw_square(my_turtle, 200)
#ch1_draw_square_dash(my_turtle, 200)
#ch3_draw_form(my_turtle, 100, 7)
#ch6_spirograph(my_turtle, 100, 32)
final_project_art(my_turtle, 20, 10, 10, -275)
my_screen.exitonclick()