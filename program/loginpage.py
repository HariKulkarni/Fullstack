from tkinter import Tk, Label, Entry, Button

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username == "admin" and entered_password == "password":
        login_status.config(text="Login successful!", fg="green")
        # Perform actions after successful login
    else:
        login_status.config(text="Invalid username or password.", fg="red")

# Create the main window
window = Tk()
window.title("Login Page")

# Create and position the username label and entry
username_label = Label(window, text="Username:")
username_label.pack()
username_entry = Entry(window)
username_entry.pack()

# Create and position the password label and entry
password_label = Label(window, text="Password:")
password_label.pack()
password_entry = Entry(window, show="*")
password_entry.pack()

# Create and position the login button
login_button = Button(window, text="Login", command=login)
login_button.pack()

# Create and position the login status label
login_status = Label(window, text="")
login_status.pack()

# Run the main window's event loop
window.mainloop()
