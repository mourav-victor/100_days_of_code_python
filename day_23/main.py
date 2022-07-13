## Turtle GUI
import random
import time
import turtle
import my_turtle_class
import level
import car

# Create and configurate screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Crossing Street")
screen.tracer(0)
screen.listen()
#screen.setup(width=800, height=600)
print(f"{screen.canvwidth} x {screen.canvheight}")

## Create objects
turtle = my_turtle_class.MyTurtle()
level = level.Level()

screen.onkeypress(key="Up", fun=turtle.up)
screen.onkey(key="Down", fun=turtle.down)

#car = car.Car()
cars = []

## Play the game
lost = False
while(not lost):
    screen.update()

    if(random.randint(1,100) <= 25):
        cars.append(car.Car())

    for any_car in cars:
        if(any_car.verify_colision(turtle)):
            level.game_over()
            lost = True
        any_car.move()

    if(turtle.verify_end()):
        level.update_level()
        for any_car in cars:
            any_car.goto(-200,-200)
            any_car.reset()
            any_car.color("white")
        cars = []
        

    time.sleep(level.speed)

screen.exitonclick()
