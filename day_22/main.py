## Turtle GUI
import turtle
import random
import time
import paddle
import ball
import score

def faster():
    global speed
    speed *= 0.9

def slower():
    global speed
    speed *= 1.1

# Create and configurate screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()
#screen.setup(width=800, height=600)
print(f"{screen.canvwidth} x {screen.canvheight}")

## Create snake and food
paddle_p1 = paddle.Paddle("p1")
paddle_p2 = paddle.Paddle("p2")
ball = ball.Ball()
score = score.Score()
#food = food.Food()

screen.onkeypress(key="Up", fun=paddle_p2.up)
screen.onkeypress(key="Down", fun=paddle_p2.down)
screen.onkeypress(key="w", fun=paddle_p1.up)
screen.onkeypress(key="s", fun=paddle_p1.down)

screen.onkeypress(key="p", fun=paddle_p1.print_position)
screen.onkeypress(key="m", fun=faster)
screen.onkeypress(key="n", fun=slower)

speed = 0.01


## Play the game
while(True):
    screen.update()

    ball.paddle_collision(paddle_p1, paddle_p2)
    ball.side_collision(score)
    ball.move()
    time.sleep(speed)

screen.exitonclick()
