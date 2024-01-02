""" Importing necessary modules from tkinter library """
import tkinter as tk
from tkinter import filedialog, messagebox


# Function to open a file and display its content in the text editor
def open_file():
    # Opens a file dialog window to select a file
    file_path = filedialog.askopenfilename()
    # If a file is chosen
    if file_path:
        # Open the file in read mode and read its content
        with open(file_path, 'r', encoding="utf-8") as file:
            # Delete existing content in the text widget
            text.delete(1.0, tk.END)
            # Insert the content of the file into the text widget
            text.insert(tk.END, file.read())


# Function to save the content of the text editor to a file
def save_file():
    # Opens a file dialog window to choose a location to save the file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )
    # If a location is chosen
    if file_path:
        # Open the file in write mode and write the content from the text widget to the file
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(text.get(1.0, tk.END))


# Function to clear the content of the text editor (create a new file)
def new_file():
    # Delete existing content in the text widget
    text.delete(1.0, tk.END)


# Function to display information about the text editor in a message box
def about():
    # Show an information message box with details about the text editor
    messagebox.showinfo("About", "Simple Text Editor\nCreated with Tkinter by Mohamed Khedr")


# Function to apply a bold font style to the selected text in the text editor
def bold_text():
    # Apply a "bold" tag to the selected text range in the text widget
    text.tag_add("bold", "sel.first", "sel.last")
    # Configure the "bold" tag to use a bold Arial font with a font size of 12
    text.tag_config("bold", font=("Arial", 12, "bold"))


# Create the main Tkinter window
root = tk.Tk()
# Set the title of the window
root.title("Simple Text Editor")

# Create a text widget to display/edit text
text = tk.Text(root, wrap="word")
# Use the pack geometry manager to place the text widget within the window, allowing it to expand in both directions
text.pack(expand=True, fill="both")

# Create a menu bar to hold different menus
menu_bar = tk.Menu(root)

# Create a "File" submenu with options for New, Open, Save As, and Exit
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save As", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create an "Edit" submenu with an option to apply bold formatting to selected text
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Bold", command=bold_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Create a "Help" submenu with an option to display information about the text editor
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Configure the root window to use the menu bar
root.config(menu=menu_bar)

# Start the main event loop to display the GUI and handle user interactions
root.mainloop()
