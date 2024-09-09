from turtle import Turtle, Screen
import random


colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title = "Make Your Bet", prompt = f"Which turtle will win the race? Enter a color: {colors} ")

is_race_on = False
all_turtles = []


curr_x = 200
curr_y = -125

for i in range(6):
    t1 = Turtle("turtle")
    t1.color(colors[i])
    t1.penup()

    t1.goto(x=-curr_x, y=curr_y)

    all_turtles.append(t1)

    curr_y += 50


# Starting the race
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:

        if turtle.xcor() > 230: # Winning Condition
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        distance = random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()