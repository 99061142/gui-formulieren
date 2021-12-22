import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno
from tkinter.messagebox import showinfo

from string import ascii_lowercase
from string import ascii_uppercase

from random import choice
from random import shuffle


# Makes the window
window = tk.Tk()
window.title('Date by days calculator')


chosen_word = tk.StringVar() # Word the user did choose
max_score = tk.IntVar() # End score

chosen_letters = [] # list of the letters the user has chosen


# Make the starting values / reset the starting values
def starting_values():
    global chosen_letters

    chosen_word.set(value='') # Word the user must guess
    chosen_letters = [] # list of the letters the user has chosen


# Clear the whole window
def clean_window():
    # Clear the window
    for items in window.winfo_children():
        items.destroy()


# Change the screen with the answer if the user wants to play again
def change_screen(question):
    play_again = askyesno(None, question) # Question if the user wants to play again

    if play_again:
        clean_window() # Clears the window
        homescreen() # Show the homescreen
    else:
        exit() # Stop the program


# Check if the word is guessed correctly, and return the message
def word_validation():
    guessed_letters = [letter.get().lower() for letter in chosen_letters] # list of all the guessed letters
    guessed_word = ''.join(guessed_letters).lower() # String with the letters the user guessed

    word = chosen_word.get() # Word the user must guess

    # If the user guessed the word correctly
    if guessed_word == word:
        question = f"Gefeliciteerd, uw score is {max_score.get()}. Wilt u nog een keer spelen?"
        change_screen(question) # Ask if the user wants to play again
    
    # If the user did not guess the word correctly
    else:
        wrong_position = 0 # Keeps track of the wrongly guessed letters

        # Check how many mistakes the user made
        for guessed_letter, word_letter in zip(guessed_word, word):
            # If the user did not guess the letter correctly
            if guessed_letter != word_letter:
                wrong_position += 1 # Increase the wrongly guessed letters score
        else:
            # Change the total score with the wrongly guessed letters amount
            new_score = max_score.get() - wrong_position
            max_score.set(new_score)

            # Show how many letters the user guessed correctly
            message = f"Helaas er is/zijn {len(word) - wrong_position} letter(s) goed."
            showinfo(None, message)


            if new_score <= 0:
                # Ask if the user wants to play again
                question = "Uw score is lager of gelijk aan 0, wilt u opnieuw beginnnen?"
                change_screen(question) # Ask if the user wants to play again


# Make the random letters for the button
def get_letters(letter):
    letters = list(ascii_uppercase) # All the letters of the alphabet

    letter_list = [] # Letters for 1 button

    # Add the letter of the word the user must guess to the letter list
    letter = tk.StringVar(value=letter.upper())
    letter_list.append(letter)
    
    # Add 4 random letters to the letter list
    for _ in range(4):
        letter = tk.StringVar(value=choice(letters))
        letter_list.append(letter)
    else:
        shuffle(letter_list)  # Shuffle the values of the letters for the button


    return letter_list


# Makes the game screen
def game_screen():
    word_length = len(chosen_word.get()) # Amount of letters the user must guess

    tk.Label(text="Raad het woord", font=('arial', 18, 'bold')).grid(columnspan=word_length, pady=(0, 10)) # Title for game screen

    # Make the buttons to guess the letter
    for col, letter in enumerate(chosen_word.get()):
        letter_list = get_letters(letter) # Get the random letters

        start_letter = choice(letter_list) # Letter the user chose
        chosen_letters.append(start_letter) # List with the letters the user chose


        # Make the input
        letter_input = ttk.Combobox(window, textvariable=start_letter, width=8)
        letter_input['values'] = [letter.get() for letter in letter_list] # Add all the letters
        letter_input['state'] = 'readonly' # User must choose a value that is a valid option

        letter_input.grid(row=1, column=col, sticky=tk.W, padx=5, pady=5) # Add the input to the screen

    tk.Button(text="Doe een gok", font=('arial', 10), command=word_validation).grid(columnspan=word_length, pady=(20, 50)) # Button to submit the word


# Check if the user chose a valid word
def submit():   
    word_length = len(chosen_word.get()) # Get the length of the word the user must guess
    
    if word_length >= 4 and word_length <= 7:
        letters = ascii_lowercase + ascii_uppercase # Valid characters

        # Check every letter
        for letter in chosen_word.get():            
            # Check if the letter is a valid option out of all the letters
            if letter not in letters:
                break

        # If every letter is valid
        else:
            max_score.set(word_length * word_length) # Set the max score the user can have

            clean_window() # Delete everythting on the window
            game_screen() # Make the window to play the game


# Make the homescreen
def homescreen():
    starting_values()

    tk.Label(text="Vul een woord in", font=('arial', 18, 'bold')).pack(fill='x', pady=10) # Title for homescreen

    tk.Entry(window, textvariable=chosen_word, width=35).pack(pady=10, padx=50) # Input for the word

    tk.Label(text="(4 tot 7 letters)", font=('arial', 8)).pack(fill='x') # Rules for the word

    tk.Button(text="Stel woord in", font=('arial', 10), command=submit).pack(ipadx=20, pady=50) # Button to submit the word




# If the code starts
if __name__ == "__main__":
    homescreen() # Make the homescreen window
    window.mainloop() # Show the window