import turtle
import pandas as pd
image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
# screen.setup(width=725, height=491)
# screen.bgpic(image)

screen.addshape(image)
turtle.shape(image)
# This is a way to get the x and y coordinates of the screen
coor_function = '''
def get_mouse_click_coor(x, y):
    print(x, y)

 turtle.onscreenclick(get_mouse_click_coor)
 turtle.mainloop()
'''





states_data = pd.read_csv("50_states.csv")
# all_the_states =  pd.DataFrame(states_data)
all_the_states_list = states_data.state.to_list()
guess_states = []
still_guessing = len(guess_states) < len(all_the_states_list)


# while still_guessing:

while still_guessing:
    user_state = screen.textinput(title={len(guess_states)/len(states_data)}, prompt="What's another state's name?").title()
    # print(f"user State: {user_state}")

    if user_state in all_the_states_list:
        # To get the current row of the state
        current_state = states_data[states_data.state == user_state]
        print(f"Current State Data: {current_state}")
        location = turtle.Turtle()
        location.hideturtle()
        location.penup()
        location.color("black")
        location.goto(int(current_state.x), int(current_state.y))
        location.write(user_state)
        guess_states.append(user_state)

        # OR use this below
        # location.write(states_data.state.item())

    if user_state == "Exit":
        #this APPROACH of code will get all the states that are not in the guess_state
        # missing_states = [state for state in all_the_states_list if state not in guess_states]
        # OR THIS APPROACH BELOW
        missing_states = []
        for state in all_the_states_list:
            if state not in guess_states:
                # Extract row as Series
                unknown_state = states_data[states_data.state == state].iloc[0]  
                 # ✅ Appending a Series instead of a DataFrame slice
                missing_states.append(unknown_state) 

        # Convert the list of Series into a new DataFrame
        new_data = pd.DataFrame(missing_states)
        # Save to CSV
        new_data.to_csv("states_to_learn.csv", index=False)
        break






screen.exitonclick()