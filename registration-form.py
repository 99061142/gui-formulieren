import tkinter as tk

# Makes the window
window = tk.Tk()
window.title("Form")


# ALl the questions the user must answer
questions = {
    "important": {
        "question1": '0',
        "question2": '0',
        "question3": '0',
        "question4": '0',
        "question5": '0',
    }
}


important_questions_answer = [] # All the important answers the user gave


# Clear the whole window
def clear_window():
    # Clear the window
    for items in window.winfo_children():
        items.destroy()


# Make the label / inputs for the questions
def question_inputs(path):
    # For every question the user must answer
    for question in questions[path]:
        question_answer = tk.StringVar()

        important_questions_answer.append(question_answer) 

        question_input = tk.Entry(window, textvariable=question_answer, width=25) # Input to answer the question
        
        question_input.pack() # Add the input to the window


# Validate the normal question answers
def validate_normal_questions():
    pass


# Validate the important question answers
def validate_important_questions():
    validation = True

    correct_answers = list( questions['important'].values() ) # Answers the user must give to the questions

    # Check every answer the user gave to the questions
    for answer, correct_answer in zip(important_questions_answer, correct_answers):
        # If the user did not choose the correct anwer
        if answer.get() != correct_answer:
            validation = False 


    return validation # Return if the user correctly answered the important questions


# Validate the answer the user gave, and go to the next questions or show the end screen
def head_question_passing(path):
    # If the user must answer the important questions
    if path == "important":
        validation = validate_important_questions() # Validate the important questions
    
    # If the user must answer the normal questions
    else:
        validation = validate_normal_questions() # Validate the normal questions

    # If the user did not answered the important questions correctly, or the user answered all the questions correctly
    if not validation or validation and path != "important":
        end_screen(validation) # Show the information about the answers / if the user answered the questions correctly

    # If the user correctly answered all the important answers
    else: 
        normal_question_screen() # Go to the normal questions


# End screen
def end_screen(validation):
    if validation:
        print("You have correctly answered all the questions")
    else:
        print("Sadly you don't have a chance to get a ticket")


# Screen with the normal questions (that can have any value)
def normal_question_screen():
    clear_window() # Clear the window


# Screen with the important questions (that must be true)
def head_question_screen():
    clear_window() # Clear the window

    question_inputs('important') # Make the important questions

    tk.Button(text="Start", font=('arial', 20), command=lambda: head_question_passing('important')).pack() # Button to submit the answer


# Homescreen when the user starts the program
def homescreen():
    tk.Label(text="Registrate yourself for the e-sport conference day", font=('arial', 18, 'bold')).pack(fill='x', pady=10) # Title for homescreen

    # Note before the user starts
    tk.Label(text=f"* NOTE", font=('arial', 15)).pack(fill='x', pady=5)
    tk.Label(text=("If you completed the form you can get the ticket, else you can't come to the conference"), font=('arial', 12)).pack(fill='x')

    tk.Button(text="Start", font=('arial', 20), command=head_question_screen).pack(ipadx=20, pady=50) # Starting button




# When the program starts
if __name__ == "__main__":
    homescreen() # Show the homescreen
    window.mainloop() # Starts the window