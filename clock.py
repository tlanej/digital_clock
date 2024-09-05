import tkinter as tk
from tkinter import font
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Configure the clock label
clock_font = font.Font(family='Helvetica', size=48, weight='bold')
clock_label = tk.Label(root, font=clock_font, bg='black', fg='white')
clock_label.pack(fill='both', expand=True)

# Start the clock
update_time()

# Run the application
root.mainloop()
