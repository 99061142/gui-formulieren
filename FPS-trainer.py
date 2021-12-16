import tkinter as tk
from tkinter import messagebox
import random


# Make the window
window = tk.Tk() # Start the window
window.title('Simple FPS trainer') # Window title
window.geometry("500x300") # Window size
window.configure(bg="lightgray") # Window background


# Keybinds for the keyboard / button
keybinds = {
    'keyboard': ['w', 'a', 's', 'd', 'space'],
    'button': [
        {'text': 'single-click', 'bind': 'Button-1'}, 
        {'text': 'double-click', 'bind': 'Double-Button-1'}, 
        {'text': 'triple-click', 'bind': 'Triple-Button-1'}
    ]
}


time = None # Starting value for the time
points = None # Starting value for the points
button = None # Random created button


# Add the points when the user completed the bind
def add_points(event):
    global points

    bind = event.keysym.lower() # Bind what the user must do

    # Check how many points must be added, and unbind the bind
    if bind in keybinds['keyboard']:
        points += 1 
        window.unbind(f"<{bind}>")

    else:
        points += 2
        button.unbind(f"<{bind}>")


    button.destroy() # Destroy the button

    scoreboard_text() # Update the points in the scoreboard
    random_keybind() # Add a new random button


# Scoreboard text
def scoreboard_text():
    global time
    global points


    scoreboard_str = f"Time remaining: {time}               {points} points" # Text 
    scoreboard.configure(text=scoreboard_str) # Edit the scoreboard


# Countdown to 0
def countdown():
    global time

    # If the user has time left
    if time > 0:
        time -= 1 # Decrease the time
        scoreboard_text() # Change the time on the lable

        window.after(1000, countdown) # After every second this function is called again
    
    # If the time is over
    else:
        game_over_screen() # Game over screen


# Make a button with a random bind and a random position
def random_keybind():
    global button # Random created button

    events = list(keybinds.keys()) # Make a list of the possible bind options
    event = random.choice(events) # Choose if its a keyboard or a button bind

    bind = random.choice(keybinds[event]) # Choose a random bind 


    # If the event is for the keyboard
    if event == "keyboard":
        text = f"press {bind}" # Text inside the button
        bind = f"<{bind}>" # Bind for the keyboard

    # If the event is for the button
    else:
        text = bind['text'] # Text inside the button
        bind = f"<{bind['bind']}>" # Bind for the button


    # Make a button with a random bind and a random position
    bind_button = tk.Button(
        window, 
        font=("arial", 15), 
        width=20
    )

    scoreboard_height = scoreboard.winfo_height() # Height of the scoreboard

    width = random.randrange(scoreboard_height, window.winfo_width() // 2) # Random width position
    height = random.randrange(scoreboard_height * 2, window.winfo_height() // 4 * 3) # Random height position

    bind_button.place(x=width, y=height) # Add the button to the window


    # If the keybind is for the keyboard
    if event == "keyboard": 
        bind_button['text'] = text # Text inside the button
        window.bind(bind, add_points) # Bind for the keyboard

    # If the keybind is for the button
    else:
        bind_button['text'] = text # Text inside the button
        bind_button.bind(bind, add_points) # Bind for the button

    button = bind_button # Add the created button to the global button 


# Game started
def game(start_button):
    start_button.destroy() # Destroy the starting button
    
    countdown() # Starts the countdown
    random_keybind() # Add a random button


# Starting screen
def start_screen():
    global time
    global points

    # Values when the player starts
    time = 20
    points = 0

    # Make the button to start the game
    start_button = tk.Button(
        window, 
        font=("arial", 15), 
        width=20,
        text='Press here to start'
    )

    start_button['command'] = lambda: game(start_button) # Function when the button gets pressed

    start_button.pack(expand=True) # Add the button to the window


# Game over screen
def game_over_screen():
    text = button['text'] # Button text

    # If keybind was with the keyboard
    if text in keybinds['keyboard']:
        window.unbind(f"<{text}>")
    
    # If keybind was clicking the button
    else:
        button.unbind(f"<{text}>")


    button.destroy() # Destroy the last random button

    play_again = tk.messagebox.askyesno("Game over", f"Congratulations you have {points} points, wanna play again?") # Messagebox

    if play_again:
        start_screen() # Go to the start screen
    else:
        window.destroy() # Destroy the window











# Make the scoreboard
scoreboard = tk.Label(
    window,
    bg="black",
    fg="white",
    font=('arial',15)
)

scoreboard.pack(fill='x')




# If the code starts
if __name__ == "__main__":
    start_screen() # Add the start screen
    scoreboard_text() # Add the scoreboard

    window.mainloop() # Show the window