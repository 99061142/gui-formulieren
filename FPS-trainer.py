import tkinter as tk
from tkinter.messagebox import showinfo
import random

# Make the window
window = tk.Tk() # Start the window
window.title('Simple FPS trainer') # Window title
window.geometry("500x300") # Window size
window.configure(bg="lightgray") # Window background


user_time_input = tk.StringVar() # Value what the user chose to check if it is a number

time = tk.IntVar(value=20) # Time the user has chosen
points = tk.IntVar(value=0) # Points on the scoreboard

global scoreboard
global start_button
global button


# Keybinds for the keyboard / button
keybinds = {
    'keyboard': ['w', 'a', 's', 'd', 'space'],
    'button': [
        {'text': 'single-click', 'bind': 'Button-1'}, 
        {'text': 'double-click', 'bind': 'Double-Button-1'}, 
        {'text': 'triple-click', 'bind': 'Triple-Button-1'}
    ]
}


def game_over_screen():
    text = button['text'] # Button text

    # If keybind was with the keyboard
    if text in keybinds['keyboard']:
        window.unbind(f"<{text}>")
    
    # If keybind was clicking the button
    else:
        button.unbind(f"<{text}>")


    button.destroy() # Destroy the last random button

    play_again = tk.messagebox.askyesno("Game over", f"Congratulations you have {points.get()} points, wanna play again?") # Messagebox

    if play_again:
        home_screen() # Go to the start screen
    else:
        window.destroy() # Destroy the window


def countdown():
    # If the user has time left
    if time.get() > 0:
        new_time = time.get() - 1

        time.set(new_time)  # Decrease the time

        scoreboard_text() # Change the time on the scoreboard

        window.after(1000, countdown) # After every second this function is called again
    
    # If the time is over
    else:
        game_over_screen() # Game over screen


# Add the points when the user completed the bind
def add_points(event):
    bind = event.keysym.lower() # Bind what the user must do

    # Check how many points must be added, and unbind the bind
    if bind in keybinds['keyboard']:
        new_points = points.get() + 1

        window.unbind(f"<{bind}>")

    else:
        new_points = points.get() + 2

        button.unbind(f"<{bind}>")


    button.destroy() # Destroy the button

    points.set(new_points) # Update the points
    scoreboard_text() # Update the points on the scoreboard

    random_keybind() # Add a new random button


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

    width = random.randint(scoreboard_height, window.winfo_width() // 2) # Random width position
    height = random.randint(scoreboard_height * 2, window.winfo_height() // 4 * 3) # Random height position

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


def game():
    start_button.destroy() # Destroy the starting button
    
    countdown() # Countdown for the game
    random_keybind() # Add a random button


# Add / change the text of the scoreboard
def scoreboard_text():
    scoreboard_str = f"Time remaining: {time.get()}               {points.get()} points" # Text 
    scoreboard.configure(text=scoreboard_str) # Edit the scoreboard


# Makes the scoreboard
def scoreboard():
    global scoreboard

    # Make the scoreboard
    scoreboard = tk.Label(
        window,
        bg="black",
        fg="white",
        font=('arial',15)
    )

    scoreboard_text()

    scoreboard.pack(fill='x')


# Show the starting screen and add the scoreboard
def starting_screen():
    global start_button

    scoreboard() # Add the scoreboard to the screen

    # Button to start the game
    start_button = tk.Button(
        window, 
        font=("arial", 15), 
        width=20,
        text='Press here to start',
        command=lambda: game()
    )

    start_button.pack(expand=True)



def login_clicked(start_screen):
    user_input = user_time_input.get() # Users input

    # If the user chose an number, the value gets changed
    if user_input.isdigit():
        time.set(user_input) # Time value is the users input


    # Show an error, or what the user has chosen
    msg = f"The time you chose is '{time.get()}'" if user_input.isdigit() else f"You did not choose a number, it is automatically '{time.get()}"  

    showinfo(
        title='Information',
        message=msg
    )

    start_screen.destroy() # Destroy the home screen
    starting_screen() # Go to the starting screen


# Home screen where the user can choose a number
def home_screen():
    # Start screen
    start_screen = tk.Frame(window)
    start_screen.pack(padx=10, pady=10, fill='x', expand=True)


    # Time label / input
    time_label = tk.Label(start_screen, text="Time:")
    time_label.pack(fill='x', expand=True)

    time_entry = tk.Entry(start_screen, textvariable=user_time_input)
    time_entry.pack(fill='x', expand=True)
    time_entry.focus()

    # Submit button
    login_button = tk.Button(start_screen, text="Submit", command=lambda: login_clicked(start_screen))
    login_button.pack(fill='x', expand=True, pady=10)




# If the code starts
if __name__ == "__main__":  
    home_screen()
    window.mainloop()