## Turtle in OOP
import turtle

# Configs
my_screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("DarkGreen")
my_screen.bgcolor("grey")
my_turtle.speed("slow")

print(my_turtle) 
print(f"{my_screen.canvwidth} x {my_screen.canvheight}")

# Heart 
def heart():
  
    # Set the fill color to red
    my_turtle.fillcolor('red')
  
    # Start filling the color
    my_turtle.begin_fill()
  
    # Draw the left line
    my_turtle.left(140)
    my_turtle.forward(113)
  
    # Draw the left curve
    for i in range(200):
  
        # Defining step by step curve motion
        my_turtle.right(1)
        my_turtle.forward(1)
    my_turtle.left(120)
  
    # Draw the right curve
    for i in range(200):
  
        # Defining step by step curve motion
        my_turtle.right(1)
        my_turtle.forward(1)
  
    # Draw the right line
    my_turtle.forward(112)
  
    # Ending the filling of the color
    my_turtle.end_fill()

# Actions
while(True):
    my_turtle.forward(100)
    my_turtle.left(55)

my_screen.exitonclick()