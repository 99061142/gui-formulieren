import tkinter as tk

# Makes the window
window = tk.Tk()
window.geometry("380x410")
window.title('Login')
window.resizable(0, 0)


# Makes the board
for row in range(10):
    for col in range(10):
        # Change background color
        if row % 2 == 0 and col % 2 == 0 or row % 2 != 0 and col % 2 != 0:
            background = "black"
        else:
            background = "white"

        # Add button to the row
        block = tk.Button(window, bg=background, width=4, height=2).grid(column=col, row=row)


# When the code starts
if __name__ == "__main__":
    window.mainloop()   