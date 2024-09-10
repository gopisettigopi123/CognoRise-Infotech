import tkinter as tk
from tkinter import messagebox
import time

# Function to update the countdown
def countdown(count):
    # Formatting the time in minutes and seconds
    minutes, seconds = divmod(count, 60)
    time_format = '{:02d}:{:02d}'.format(minutes, seconds)
    label['text'] = time_format
    if count > 0:
        # After 1000ms (1 second), call countdown function with count - 1
        root.after(1000, countdown, count - 1)
    else:
        messagebox.showinfo("Time's up!", "The countdown has finished!")

# Function to start the countdown
def start_countdown():
    try:
        # Get the time from the entry and convert it to seconds
        time_in_minutes = int(entry.get())
        countdown(time_in_minutes*60)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number!")

# Create the main window
root = tk.Tk()
root.title("Countdown Timer")

# Label for the timer display
label = tk.Label(root, font=('Helvetica', 48), text="00:00")
label.pack()

# Entry field for user to input time in minutes
entry = tk.Entry(root, font=('Helvetica', 24))
entry.pack()

# Button to start the countdown
start_button = tk.Button(root, text="Start", font=('Helvetica', 18), command=start_countdown)
start_button.pack()

# Run the tkinter event loop
root.mainloop()
