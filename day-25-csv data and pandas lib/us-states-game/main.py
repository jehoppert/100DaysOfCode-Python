import turtle
import pandas

#setting up screen and background turtle image
screen = turtle.Screen()
screen.title("US States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#check to get corrdinates for states for 50_states.csv
#def get_mouse_click_coor(x, y):
#  print(x,y)
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()

state_data = pandas.read_csv("./50_states.csv")

states_guessed = []

while True:
  guess_state = screen.textinput(title=f"Guess the States {len(states_guessed)}/{len(state_data)}", prompt="Guess a State's Name").title()

  guess_state_data = state_data[state_data["state"] == guess_state]

  if guess_state == "Exit":
    break

  if not guess_state_data.empty and guess_state not in states_guessed:
    state = turtle.Turtle()
    state.color("black")
    state.penup()
    state.hideturtle()
    x = int(guess_state_data["x"])
    y = int(guess_state_data["y"])
    state.goto(x, y)
    state.write(f"{guess_state}", align="center", font=("Courier", 12, "normal"))
    states_guessed.append(guess_state)

#generate states missed csv file
states_missed_list = list(set(state_data["state"].to_list()) - set(states_guessed))

states_missed_df = pandas.DataFrame(states_missed_list)
states_missed_df.to_csv("./states_missed.csv")