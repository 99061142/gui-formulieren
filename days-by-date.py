import tkinter as tk
from tkinter import ttk

from calendar import calendar
from calendar import monthrange
from calendar import month_name
from datetime import datetime


# Makes the window
window = tk.Tk()
window.geometry('300x200') 
window.title('Date by days calculator') # Window title


title = tk.Label(text="Date:", font=('arial', 18, 'bold')).pack(fill='y', pady=2) # Title


selected_day = tk.IntVar()
selected_month = tk.StringVar()
selected_year = tk.IntVar()
total_days = tk.IntVar()


def make_day_input():
    # create the input for the days
    day_input = ttk.Combobox(window, textvariable=selected_day)
    day_input['values'] = [[day] for day in range(1, total_days.get())] # Add day numbers to the input (first 3 letters)
    day_input['state'] = 'readonly' # User must choose a value that is a valid option

    day_input.pack(fill=tk.X, padx=5, pady=5) # Add the input to the screen


def make_month_input():    
    # create the input for the months
    month_input = ttk.Combobox(window, textvariable=selected_month)
    month_input['values'] = [month_name[month][0:3] for month in range(1, 13)] # Add month names to the input (first 3 letters)
    month_input['state'] = 'readonly' # User must choose a value that is a valid option

    month_input.pack(fill=tk.X, padx=5, pady=5) # Add the input to the screen


def make_year_input():
    # create the input for the year
    year_input = ttk.Entry(window, textvariable=selected_year)

    year_input.pack(fill=tk.X, padx=5, pady=5) # Add the input to the screen


def add_local_time():
    current_local_time = datetime.now() # Current local time

    current_day = current_local_time.day # Current day

    # Current month
    current_month = current_local_time.strftime('%b')
    current_month_num = current_local_time.month

    current_year = current_local_time.year # Current year

    current_days = monthrange(current_year, current_month_num)[1] + 1 # Calculate how many days are in the current month

    # Add the current information inside the inputs
    selected_day.set(current_day)
    selected_month.set(current_month)
    selected_year.set(current_year)
    total_days.set(current_days)


# Make all the inputs
def main():
    add_local_time() # Get the local times
    make_day_input() # Make the input for the days
    make_month_input() # Make the input for the months
    make_year_input() # Make the input for the year




# If the code starts
if __name__ == "__main__":
    main()
    window.mainloop()