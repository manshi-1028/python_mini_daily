import json
import random
import string
from tkinter import *
from tkinter import messagebox

# ---------------- PASSWORD GENERATOR ---------------- #

def generate_password():
    password_entry.delete(0, END)

    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*()_+-="

    password_chars = []

    password_chars += random.choices(letters, k=random.randint(8, 10))
    password_chars += random.choices(symbols, k=random.randint(2, 4))
    password_chars += random.choices(numbers, k=random.randint(2, 4))

    random.shuffle(password_chars)

    password = "".join(password_chars)
    password_entry.insert(0, password)

# ---------------- SAVE PASSWORD ---------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Missing Data",
            message="Please fill all fields."
        )
        return

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        with open("data.json", "w") as file:
            json.dump(new_data, file, indent=4)

    else:
        data.update(new_data)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------- SEARCH ---------------- #

def search():
    website = website_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(
            title="Error",
            message="No data file found."
        )

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]

            messagebox.showinfo(
                title=website,
                message=f"Email: {email}\nPassword: {password}"
            )
        else:
            messagebox.showinfo(
                title="Not Found",
                message=f"No details for {website}."
            )

# ---------------- UI ---------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Labels

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons

search_button = Button(
    text="Search",
    width=14,
    command=search
)
search_button.grid(row=1, column=2)

generate_button = Button(
    text="Generate Password",
    command=generate_password
)
generate_button.grid(row=3, column=2)

add_button = Button(
    text="Add",
    width=36,
    command=save_password
)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
