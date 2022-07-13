import pandas as pd
import turtle as tt

states_table = pd.read_csv("./day_25/50_states.csv")
print(states_table)

screen = tt.Screen()
screen.title("U.S. States Game")
img = "./day_25/blank_states_img.gif"
screen.addshape(img)
tt.shape(img)

count = 0
total = len(states_table["state"])

while(count < total):
    
    ans = screen.textinput(title=f"Guess the State [{count}/{total}]", prompt="What is the name?").title()
    if ans in states_table["state"].to_list():
        count += 1
        t = tt.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_table[states_table["state"] == ans]
        print(state_data)
        t.goto(float(state_data.x), float(state_data.y))
        t.write(ans)

    if ans == "Exit":
        break

screen.exitonclick()