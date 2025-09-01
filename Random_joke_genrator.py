import tkinter as tk
import pyjokes

# Function to get a new joke
def get_joke():
    joke = pyjokes.get_joke()
    joke_label.config(text=joke)

# Create the main window
root = tk.Tk()
root.title("😂 Joke Generator")
root.geometry("500x250")
root.config(bg="#1e1e2e")  # background of the main window (dark mode)

# Add a title label
title_label = tk.Label(
    root,
    text="Welcome to Joke Generator!",
    font=("Arial", 16, "bold"),
    fg="white",           # text color
    bg="#1e1e2e"          # same as window bg (blends in)
)
title_label.pack(pady=10)

# Label to display jokes
joke_label = tk.Label(
    root,
    text="Click the button to get a joke!",
    wraplength=400,
    justify="center",
    font=("Arial", 12),
    fg="yellow",          # joke text color
    bg="#1e1e2e"          # same background as window
)
joke_label.pack(pady=20)

# Button to fetch jokes
joke_button = tk.Button(
    root,
    text="Tell me a Joke 😂",
    command=get_joke,
    font=("Arial", 12, "bold"),
    fg="white",           # button text color
    bg="#4CAF50",         # button background color (green)
    activebackground="lime",  # button color when pressed
    activeforeground="black"  # text color when pressed
)
joke_button.pack(pady=10)
# Run the Tkinter event loop
root.mainloop()
