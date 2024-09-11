import turtle
import pandas

image = "US States Game/blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S States Game")

screen.addshape(image)

turtle.shape(image)


states_data = pandas.read_csv("US States Game/50_states.csv")
all_states = states_data["state"].tolist()

guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?: ")
    answer_state = answer_state.title()
    # print(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("US States Game/States To Learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        current_state_data = states_data[states_data["state"] == answer_state]
        t.goto(current_state_data.x.item(),current_state_data.y.item())
        t.write(answer_state)

