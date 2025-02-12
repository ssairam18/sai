import os
import pyperclip
import tkinter as tk

# Folder where your .jpg files are located
folder_path = r'C:\Users\ssairam18\Downloads\data'  # Use raw string for Windows path
check_file = 'check.txt'  # The check.txt file name

# Read check.txt
def read_check_file():
    with open(check_file, 'r') as file:
        return file.readlines()

# Initialize Tkinter window
root = tk.Tk()
root.title('File Checker')

# Create a canvas and a scrollbar
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
frame = tk.Frame(canvas)

# Configure the scrollbar to interact with the canvas
canvas.configure(yscrollcommand=scrollbar.set)

# Place the canvas and scrollbar in the window
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Create a window inside the canvas
canvas.create_window((0, 0), window=frame, anchor="nw")

# Function to copy text to clipboard
def copy_to_clipboard(text):
    pyperclip.copy(text)

# Function to open the file when the label is green
def open_file(file_path):
    os.startfile(file_path)

# Function to create color-coded text
def create_color_coded_text():
    # Clear previous labels
    for widget in frame.winfo_children():
        widget.destroy()

    lines = read_check_file()
    for line in lines:
        line = line.strip()  # Remove any leading/trailing whitespace
        # Check if the jpg file exists
        jpg_file = f"{line}.jpg"
        file_path = os.path.join(folder_path, jpg_file)

        if os.path.isfile(file_path):
            color = "green"
        else:
            color = "red"

        # Create a label for each file name
        label = tk.Label(frame, text=line, fg=color, cursor="hand2")
        label.pack(pady=5, anchor="w")

        # If green, make it clickable to open the file
        if color == "green":
            label.bind("<Button-1>", lambda e, file_path=file_path: open_file(file_path))
        # If red, make it clickable to copy to clipboard
        if color == "red":
            label.bind("<Button-1>", lambda e, text=line: copy_to_clipboard(text))

    # Update the scroll region of the canvas after adding all labels
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# Function to reload the files
def reload_files():
    create_color_coded_text()

# Create the "Reload" button
reload_button = tk.Button(root, text="Reload", command=reload_files)
reload_button.pack(pady=10)

# Initial load of files
create_color_coded_text()

# Run the Tkinter event loop
root.mainloop()
