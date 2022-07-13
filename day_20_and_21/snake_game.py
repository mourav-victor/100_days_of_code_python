## Turtle GUI
import turtle
import random
import time
import snake
import food

# Create and configurate screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
#screen.setup(width=800, height=600)
print(f"{screen.canvwidth} x {screen.canvheight}")

## Create snake and food
snake = snake.Snake()
food = food.Food()

## Play the game
while(True):
    
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)
    snake.move()

    if snake.head.distance(food) < 15:
        food.change_location()
        snake.eat_a_food()

    screen.update()

    if snake.head.xcor() > 370 or snake.head.xcor() < -370 or snake.head.ycor() < -300 or snake.head.ycor() > 300 :
        snake.snake_is_dead()
        break

    if snake.head.pos() in snake.get_snake_position():
        snake.snake_is_dead()
        break

    time.sleep(0.05)





#etch_a_sketch()
#two_players_turtle_race()
screen.exitonclick()
