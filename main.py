from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

FONT_NAME = "Courier"
FILE_NAME = "data.json"
# ---------------------------- SEARCH FUNCTION  ------------------------------- #
def find_password():
    try:
        #Open file
        with open(FILE_NAME, "r") as data_file:
            #Rear old data into a dictionary
            data = json.load(data_file)
    except FileNotFoundError:
        #Message
        messagebox.showerror(title="Error",
                             message="No data file found!")
    else:
        website = website_entry.get()
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,
                                message=f"Email/Username: {email}\nPassword: {password}")
        else:
            messagebox.showwarning(title="Oops",
                                   message=f"No details for the website {website} exist")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2,4))]

    shuffle(password_list)
    #Convert from list to string
    password = "".join(password_list)
    #Enter the password in the entry field, deleting it first (just in case)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    #Copy password into clipboard
    window.clipboard_clear()
    window.clipboard_append(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    #Get data
    website = website_entry.get()
    usermail = usermail_entry.get()
    password = password_entry.get()
    new_data = {
            website: {
                "email": usermail,
                "password": password,
                }
            }

    if len(website) == 0 or len(usermail) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops",
                             message="Please don't leave any field empty!")

    else:
        try:
            with open(FILE_NAME, "r") as data_file:
                #Read old data into a dictionary
                data = json.load(data_file)
        except FileNotFoundError:
            with open(FILE_NAME, "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Update data dictionary
            data.update(new_data)
            with open(FILE_NAME, "w") as data_file:
                #Save updated data
                json.dump(data, data_file, indent=4)
        finally:
            #Delete entries
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

#Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)

#Labels x3
website_label = Label(text="Website:", font=(FONT_NAME, 10), bg="white")
usermail_label = Label(text="Email/Username:", font=(FONT_NAME, 10), bg="white")
password_label = Label(text="Password:", font=(FONT_NAME, 10), bg="white")

#Entries x3
website_entry = Entry(width=21)
website_entry.focus()
usermail_entry = Entry(width=35)
usermail_entry.insert(0, "myusermail@domain.com")
password_entry = Entry(width=21)

#Buttons x3
add_button = Button(text="Add", highlightthickness=0, width=36, bg="white", command=save)
search_button = Button(text="Search", highlightthickness=0, bg="white",
                       command=find_password, width=15)
generate_pass_button = Button(text="Generate Password", highlightthickness=0,
                              bg="white", command=generate_password)

#Layout
canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1, sticky="EW")
search_button.grid(row=1, column=2, sticky="EW")
usermail_label.grid(row=2, column=0)
usermail_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_label.grid(row=3, column=0, sticky="EW")
password_entry.grid(row=3, column=1, sticky="EW")
generate_pass_button.grid(row=3, column=2, sticky="EW")
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
