from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

turtle.pensize(10)

def move_forwards():
    turtle.forward(20)

def move_backwards():
    turtle.backward(20)

def turn_clockwise():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)

def turn_anticlockwise():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)

def return_to_center():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()

screen.onkey(move_forwards, key="w")
screen.onkey(move_backwards, key="s")

screen.onkey(turn_clockwise, key="d")
screen.onkey(turn_anticlockwise, key="a")

screen.onkey(return_to_center, key="c")


screen.exitonclick()
 