import pandas as pd
import turtle

scn = turtle.Screen()
data = pd.read_csv(
    "https://raw.githubusercontent.com/svrohith9/100-days-python/main/Day25/us-states-game-start/50_states.csv")
image = ".\\Day25\\us-states-game-start\\blank_states_img.gif"

scn.addshape(image)
turtle.shape(image)
game_running = True
states_found = []

states_data = data["state"].to_list()

while len(states_found) <= 50:
    answer = scn.textinput(title=f"{len(states_found)}/50 states",
                           prompt="what's another state ?").title()
    if answer == "Exit":
        missed_states = []
        for state in states_data:
            if state not in states_found:
                missed_states.append(state)
        print(missed_states)
        break
    if answer in states_data:
        state_data = data[data.state == answer]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer, align='center', font=('Arial', 10, 'normal'))
        states_found.append(answer)
