import tkinter


# Makes window
window = tkinter.Tk() # Makes the window
window.title("Clicker") # Window title
window.configure(bg="gray") # Window background color


background = tkinter.StringVar(value="gray") # Background color
previous_background = tkinter.StringVar(value="gray") # Previous background color
button_value = tkinter.IntVar(value=0) # Value of the button with the number
previous_num = tkinter.IntVar() # Previous value of the button with the number
previous_bind = tkinter.StringVar() # Previous bind the user used

global button_with_num # All the information about the button with the number


# Change background color
def change_background():
    window.configure(bg=background.get())


# Change the number inside the second button
def change_num(text):
    # If it is an event the user has triggered (keyboard)
    if text != "up" and text != "down":
        text = text.keysym.lower() # Get the text what the user has done]
        previous_bind.set(text) # Set the bind to the last bind the user has used


    # Increase / decrease the number
    if text == "up" or text == "plus":
        new_number = button_value.get() + 1
    else:
        new_number = button_value.get() - 1

    button_value.set(new_number) 
    
    # If number is lower than 0
    if new_number < 0 and previous_num.get() == 0:
        background.set('red')

    # If number is equal to 0
    if new_number == 0 and previous_num.get() < 0 or new_number == 0 and previous_num.get() > 0:  
        background.set('gray')
    
    # If number is higher than 0
    if new_number > 0 and previous_num.get() == 0:
        background.set('green')

    # Change the background
    if background.get() != previous_background.get():
        previous_background.set(background.get())

        change_background() # Change the background color

    change_button_value() # Change the value of the second button

    previous_num.set(new_number) # Set the previous number to the number that is made


# Change the button value
def change_button_value():
    button_with_num['text'] = button_value.get() # Change the button value


# Make the 3 buttons
def make_buttons():
    for button_num in range(1, 4):
        # Make a button
        button = tkinter.Button(
            window, 
            font=("arial", 10, 'bold'), 
            width=20
        )

        button.pack(
            fill='both',
            expand=True,
            pady=20,
            padx=20
        )

        # First button
        if button_num == 1:
            text = "up"
            
            button['text'] = text
            button['command'] = lambda text=text: change_num(text)

        # Second button
        elif button_num == 2:   
            global button_with_num

            button_with_num = button

            change_button_value()

        # Third button
        else:
            text = "down"
            button['text'] = text
            button['command'] = lambda text=text: change_num(text)

        button.pack() # Add the button to the window


# Change the background color when the mouse enters / leaves the window
def change_background_binds(event):
    # When the mouse enters the window the background color gets yellow
    if event == "mouse_enter":
        background.set("yellow")

    # When the mouse leaves the window the background color gets to its original color
    else:   
        background.set(previous_background.get())

    change_background() # Change the background color


def multiplied_divided_bind(event):
    if previous_bind.get() == "up" or previous_bind.get() == "+":        
        new_number = button_value.get() * 3  # Change the value

    elif previous_bind.get() == "down" or previous_bind.get() == "-":
        new_number = button_value.get() // 3 # Change the value


    if previous_bind.get() == "up" or previous_bind.get() == "down" or orprevious_bind.get() == "+" or previous_bind.get() == "-":
        button_value.set(new_number) # Set the new value 
        change_button_value() # Update the value to the new value


# Bindings for the game
def bindings():
    global button_with_num

    window.bind('<Enter>', lambda event:change_background_binds("mouse_enter"))
    window.bind('<Leave>', lambda event:change_background_binds("mouse_leave"))

    window.bind("+", change_num)
    window.bind("<Up>", change_num)
    window.bind("-", change_num)
    window.bind("<Down>", change_num)

    window.bind("<space>", multiplied_divided_bind)
    button_with_num.bind('<Double-Button-1>', multiplied_divided_bind)


# If the code starts
if __name__ == "__main__":
    make_buttons() # Makes the 3 buttons
    bindings() # Add the bindings

    window.mainloop() # Open the window