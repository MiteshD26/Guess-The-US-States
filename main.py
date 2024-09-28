import pandas as pd
import turtle

chances = 65
guessed_state = []
data = pd.read_csv("50_states.csv")

tim = turtle.Turtle()
tim.hideturtle()
tim.penup()

SRC = turtle.Screen()
SRC.title("Guess the State Game")
image = "blank_states_img.gif"
SRC.addshape(image)
turtle.shape(image)

game_status = True
guess_count = 0
while game_status:

    answer_state = (SRC.textinput(title=f"{guess_count}/50 || Chances left {chances}", prompt="GUESS")).title()
    chances -= 1
    if answer_state in guessed_state:
        chances += 1
    for state_name in data["state"]:
        if state_name == answer_state:
            if answer_state in guessed_state:
                pass
            else:
                guessed_state.append(answer_state)
                state_data = data[data.state == answer_state]
                x = (state_data.x.item())    #if dont want to write item(), typecast it to INT
                y = (state_data.y.item())
                tim.goto(x,y)
                tim.write(answer_state, align="center", font=("Times New Roman", 10, "bold"))


        guess_count = len(guessed_state)

        if guess_count >= 50:
            game_status = False

print(guessed_state)
SRC.exitonclick()