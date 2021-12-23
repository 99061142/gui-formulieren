import tkinter as tk
from random import choice

# Makes the window
window = tk.Tk()
window.title("Form")


# ALl the questions the user must answer
questions = {
    "important": {
        "important_question1": '',
        "important_question2": '',
        "important_question3": '',
        "important_question4": '',
        "important_question5": '',
    },

    "normal": [
        "normal_question1",
        "normal_question2",
        "normal_question3",
        "normal_question4",
        "normal_question5"
    ]
}


question_path = tk.StringVar(value='important') # Starting path for the questions
head_validation = tk.BooleanVar(value=True) # If the user got all the important questions correct


important_questions_answer = [] # All the important answers the user gave
normal_questions_answer = [] # All the normal answers the user gave


# Clear the whole window
def clear_window():
    # Clear the window
    for items in window.winfo_children():
        items.destroy()


# Make a registration code
def make_registration_code():
    characters = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" # Alowed characters

    registration_code = ''.join([choice(characters) for _ in range(16)]) # Make a random registration code with the alowed characters
    
    return registration_code # Return the registration code


# Make the label / inputs for the questions
def question_inputs():
    path = question_path.get()

    # For every question the user must answer
    for row, question in enumerate(questions[path]):
        question_answer = tk.StringVar()

        # Add the answer of the users to the specific list for the path
        if path == "important":
            important_questions_answer.append(question_answer) 
        else:
            normal_questions_answer.append(question_answer) 


        tk.Label(text=f"{question}: ", font=('arial', 12)).grid(row=row, column=0) # Label with the question before the input

        question_input = tk.Entry(window, textvariable=question_answer, width=25) # Input to answer the question
        question_input.grid(row=row, column=1) # Add the input to the window


# Validate the normal question answers
def validate_normal_questions(path):
    return True


# Validate the important question answers
def validate_important_questions(path):
    validation = True

    correct_answers = list( questions['important'].values() ) # Answers the user must give to the questions

    # Check every answer the user gave to the questions
    for answer, correct_answer in zip(important_questions_answer, correct_answers):
    
        # If the user did not choose the correct anwer
        if answer.get() != correct_answer:
            validation = False 


    return validation # Return if the user correctly answered the important questions


# Validate the answer the user gave, and go to the next questions or show the end screen
def question_passing():
    path = question_path.get()


    # If the user must answer the important questions
    if path == "important":
        validation = validate_important_questions(path) # Validate the important questions
    
    # If the user must answer the normal questions
    else:
        validation = validate_normal_questions(path) # Validate the normal questions

    if head_validation.get() and not validation:
        head_validation.set(False)

    # If it were the last questions
    if path == list(questions)[-1]:
        end_screen() # Show the information about the answers / if the user answered the questions correctly

    # If the user correctly answered all the important answers
    else: 
        question_keys = list(questions) # Get the question paths

        # Get the next path for the next questions
        new_path_index = question_keys.index(path) + 1
        new_path = question_keys[new_path_index]

        question_path.set(new_path) # Set the new path

        question_screen() # Go to question screen


# End screen
def end_screen():
    clear_window() # Clear the window

    if head_validation.get():
        all_answers = important_questions_answer + normal_questions_answer # All the answers the user gave

        # Add the questions to the list
        all_questions = [] 

        for path in questions:
            all_questions = all_questions + list(questions[path])


        # Show the question + the answer of the user
        for position, (answer, question) in enumerate(zip(all_answers, all_questions)):
            tk.Label(text=f"Voor de vraag '{question}', was jou antwoord: ", font=('arial', 15)).grid(column=0, row=position)
            tk.Label(textvariable=answer, font=('arial', 15)).grid(column=1, row=position)
        else:
            registration_code = make_registration_code() # Get the random generated registration code

            tk.Label(text=f"Jou registratie code is '{registration_code}'", font=('arial', 15)).grid(columnspan=2, pady=20)

    else:
        tk.Label(text="Sadly you don't have a chance to get a ticket", font=('arial', 15)).pack(fill='both')


def question_screen():
    path = question_path.get() # Path for the questions

    clear_window() # Clear the window

    question_inputs() # Make the normal questions

    tk.Button(text="Submit", font=('arial', 20), command=question_passing).grid(columnspan=2) # Button to submit the answers


# Homescreen when the user starts the program
def homescreen():
    tk.Label(text="Registrate yourself for the e-sport conference day", font=('arial', 18, 'bold')).pack(fill='x', pady=10) # Title for homescreen

    # Note before the user starts
    tk.Label(text="* NOTE", font=('arial', 15)).pack(fill='x', pady=5)
    tk.Label(text="If you completed the form you can get the ticket, else you can't come to the conference", font=('arial', 12)).pack(fill='x')

    tk.Button(text="Start", font=('arial', 20), command=question_screen).pack(ipadx=20, pady=50) # Starting button




# When the program starts
if __name__ == "__main__":
    homescreen() # Show the homescreen
    window.mainloop() # Starts the window