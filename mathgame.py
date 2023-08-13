import tkinter as tk
from random import randint

def generate_numbers():
    num1.set(randint(0, 100))
    num2.set(randint(0, 100))
def onenter(event):
    check_guess()
def check_guess():
    global ptCount
    try:
        user_guess = int(guess_entry.get())
        
        if user_guess == num1.get() + num2.get():
            result_label.config(text="Correct!")
            ptCount.set(ptCount.get()+1)
            pt_label.config(textvariable=ptCount)
            generate_numbers()
        else:
            result_label.config(text="Incorrect! Try again.")
            ptCount.set(ptCount.get()-1)
            pt_label.config(textvariable=ptCount)
            generate_numbers()
        guess_entry.delete(0,tk.END)
    except ValueError:
        result_label.config(text="Invalid input. Enter a number.")
    pass

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")
width=500
height=500
root.geometry(f"{width}x{height}")

# Initialize random numbers
num1 = tk.IntVar()
num2 = tk.IntVar()
ptCount=tk.IntVar()

ptCount.set(0)
# Generate initial random numbers
generate_numbers()

# Create and place widgets
num_label1 = tk.Label(root, textvariable=num1)
num_label1.pack()

plus_label = tk.Label(root, text="+")
plus_label.pack()

num_label2 = tk.Label(root, textvariable=num2)
num_label2.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()

check_button = tk.Button(root, text="Check Guess", command=check_guess)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

pt_label = tk.Label(root, textvariable=ptCount)
pt_label.pack()

root.bind("<Return>",onenter)

# Start the GUI event loop
root.mainloop()