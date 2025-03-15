import turtle
from turtle import Screen, Turtle
import pandas as pd

# Set up screen
screen = Screen()
screen.title("U.S States Game")
image = "Day25/day-25-us-states-game-start/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

# Load state data
data = pd.read_csv("Day25/day-25-us-states-game-start/50_states.csv")

correct_guesses = 0
list_of_states = data.state.to_list()
guessed_states = []
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(
        title=f"Guess the State {correct_guesses}/50",
        prompt="Enter a state name or type 'Exit' to quit:"
    )

    # If user closes the input box or types 'Exit', end the game
    if answer_state is None or answer_state.lower() == "exit":
        missing_states = [state for state in list_of_states if state not in guessed_states]
        df = pd.DataFrame(missing_states, columns=["Missed States"])
        df.to_csv("states_to_learn.csv", index=False)
        break

    # Convert input to Title Case
    answer_state = answer_state.title()

    # Check if the answer is correct and not already guessed
    if answer_state in data['state'].values and answer_state not in guessed_states:
        state_data = data[data.state == answer_state]
        x, y = int(state_data.iloc[0].x), int(state_data.iloc[0].y)

        # Display state name on the map
        display_state = Turtle()
        display_state.penup()
        display_state.hideturtle()
        display_state.goto(x, y)
        display_state.write(answer_state, align='center')

        correct_guesses += 1
        guessed_states.append(answer_state)

    # End game if all states are guessed
    if correct_guesses == 50:
        message_turtle = Turtle()
        message_turtle.hideturtle()
        message_turtle.penup()
        message_turtle.goto(0, 0)  # Position message at the center
        message_turtle.write("Congratulations! You guessed all 50 states!", align="center", font=("Arial", 16, "bold"))
        
        screen.update()
        screen.ontimer(screen.bye, 3000)  # Auto close after 3 seconds
        break
