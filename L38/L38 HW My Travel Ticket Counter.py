import tkinter as tk
from tkinter import messagebox

# Main window
window = tk.Tk()
window.title("Travel Click Counter")
window.geometry("400x350")
window.configure(bg="#eaf4ff")
window.resizable(False, False)

# Counter variable
count = 0

# Update the counter on screen
def update_counter():
    counter_label.config(text=str(count))

# Increase the counter
def add_click():
    global count
    count += 1
    update_counter()

# Decrease the counter
def remove_click():
    global count
    if count > 0:
        count -= 1
    update_counter()

# Reset the counter
def reset_counter():
    global count
    count = 0
    update_counter()

# Heading
title_label = tk.Label(
    window,
    text="✈ Travel Click Counter",
    font=("Arial", 20, "bold"),
    bg="#eaf4ff",
    fg="#174a7e"
)
title_label.pack(pady=20)

# Description
description = tk.Label(
    window,
    text="Keep track of your travel count!",
    font=("Arial", 11),
    bg="#eaf4ff"
)
description.pack()

# Counter display
counter_label = tk.Label(
    window,
    text="0",
    font=("Arial", 42, "bold"),
    bg="white",
    fg="#174a7e",
    width=8
)
counter_label.pack(pady=15)

# Add button
add_button = tk.Button(
    window,
    text="+ Add Click",
    command=add_click,
    font=("Arial", 12, "bold"),
    bg="#2196f3",
    fg="white",
    width=15
)
add_button.pack(pady=5)

# Decrease button
remove_button = tk.Button(
    window,
    text="- Remove Click",
    command=remove_click,
    font=("Arial", 11),
    width=15
)
remove_button.pack(pady=5)

# Reset button
reset_button = tk.Button(
    window,
    text="Reset Counter",
    command=reset_counter,
    font=("Arial", 11),
    bg="#ffccbc",
    width=15
)
reset_button.pack(pady=5)

# Run the application
window.mainloop()
