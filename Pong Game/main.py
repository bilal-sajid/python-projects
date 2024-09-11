# Imports
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)

# Setting Up Screen
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")

# Creating Paddles
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# Creating Ball
ball = Ball()

# Creating Scoreboard
scoreboard = Scoreboard()

# Event Listeners
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")



# Game Logic
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)

    screen.update()
    ball.move()

    # Detect Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect Collision with Paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    
    # Detect Right Paddle Misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()
    
    # Detect Left Paddle Misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()
        

# Exit on Click
screen.exitonclick()