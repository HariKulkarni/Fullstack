import csv
from tkinter import Tk, Label, Frame, Scrollbar, Listbox, Button

def load_csv_data():
    file_path = "data.csv"  # Replace with your CSV file path

    try:
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            data = list(csv_reader)

            for row in data:
                listbox.insert("end", ", ".join(row))
    except FileNotFoundError:
        print("CSV file not found.")

# Create the main window
window = Tk()
window.title("CSV Data Viewer")

# Create a frame to hold the listbox and scrollbar
frame = Frame(window)
frame.pack(pady=10)

# Create a scrollbar
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# Create a listbox to display the CSV data
listbox = Listbox(frame, yscrollcommand=scrollbar.set)
listbox.pack(side="left", fill="both")

# Configure the scrollbar to work with the listbox
scrollbar.config(command=listbox.yview)

# Create a button to load the CSV data
load_button = Button(window, text="Load CSV", command=load_csv_data)
load_button.pack(pady=10)

# Run the main window's event loop
window.mainloop()
