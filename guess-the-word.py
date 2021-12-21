import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import string
from random import choice


# Makes the window
window = tk.Tk()
window.geometry('350x200') # Window size
window.title('Date by days calculator') # Window title


chosen_word = tk.StringVar() # Word the user has chosen
chosen_word_length = tk.IntVar() # Length for the chosen word 

random_letters = [] # List for the letters inside the input


# Clear the whole window
def clean_window():
    # Clear the window
    for widgets in window.winfo_children():
        widgets.destroy()


# Check if the word is guessed correctly, and return the message
def word_validation():
    guessed_letters = [letter.get().lower() for letter in random_letters] # Get all the guessed letters in lowercase
    guessed_word = ''.join(guessed_letters).lower() # String with the word the user guessed

    word = chosen_word.get() # Word the user must guess
    chosen_word_letters = list(word) # All the letters the user must guess


    # If the user guessed the word correctly
    if guessed_word == word:
        message = f"Gefeliciteerd, uw score is {0}. Wilt u nog een keer spelen?"
    
    # If the user did not guess the word correctly
    else:
        good_position = chosen_word_length.get() # Get the total amount of points the user can have

        # Check how many mistakes the user made
        for x in range(chosen_word_length.get()):
            if guessed_letters[x] != chosen_word_letters[x]:
                good_position -= 1
        else:
            message = f"Helaas er is/zijn {good_position} letter(s) goed."

        messagebox.showinfo(None, message) # Show the message box with the information


# Makes the game screen
def game_screen():
    title = tk.Label(text="Raad het woord", font=('arial', 18, 'bold')).grid(columnspan=chosen_word_length.get()) # Title for homescreen

    letters = list(string.ascii_uppercase) # All the uppercase letters the user can choose from

    global random_letters # List with all the random letters

    # Add letters to the letter list
    for x in range(1, chosen_word_length.get()):
        letter = tk.StringVar(value=choice(letters)) # Get an random letter and add it to an variable
        random_letters.append(letter) # Add the random letter to the list
    else:
        user_letter = choice(chosen_word.get()).upper() # Get an random letter out of the word the user must guess
        letter = tk.StringVar(value=user_letter) # Add the letter to an variable
        random_letters.append(letter) # Add the random letter to the list


    # Makes the inputs
    for button in range(chosen_word_length.get()):
        letter_input = ttk.Combobox(window, textvariable=random_letters[button], width=8)
        letter_input['values'] = [letter for letter in letters] # Add all the letters
        letter_input['state'] = 'readonly' # User must choose a value that is a valid option

        letter_input.grid(row=1, column=button, sticky=tk.W, padx=5, pady=5) # Add the input to the screen



    submit_button = tk.Button(text="Doe een gok", font=('arial', 10), command=word_validation).grid(columnspan=chosen_word_length.get()) # Button to submit the word


# Check if the user chose a valid word
def submit():   
    word_length = len(chosen_word.get()) # Get the length of the word the user must guess
    
    if word_length >= 4 and word_length <= 7:
        letters = string.ascii_lowercase + string.ascii_uppercase # Valid characters

        valid_word = True

        # Check every letter
        for letter in range(word_length):
            # Check if the letter is a valid option out of all the letters
            if chosen_word.get()[letter] not in letters:
                valid_word = False
                break
        else:
            chosen_word_length.set(word_length) # Set the word the user chose as the word the user must guess

            clean_window() # Delete everythting on the window
            game_screen() # Make the window to play the game


# Make the homescreen
def homescreen():
    title = tk.Label(text="Vul een woord in", font=('arial', 18, 'bold')).pack(fill='x') # Title for homescreen

    # Create the input for the word
    word_input = ttk.Entry(window, textvariable=chosen_word, width=35)

    word_input.pack(pady=10) # Add the input to the screen

    word_input_rules = tk.Label(text="(4 tot 7 letters)", font=('arial', 8)).pack(fill='x') # Add the rules to the screen

    submit_button = tk.Button(text="Stel woord in", font=('arial', 10), command=submit).pack(ipadx=20, pady=15) # Button to submit the word


# If the code starts
if __name__ == "__main__":
    homescreen() # Make the homescreen window
    window.mainloop()