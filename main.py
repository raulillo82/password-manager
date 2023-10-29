from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle

FONT_NAME = "Courier"
FILE_NAME = "data.txt"
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

    if len(website) == 0 or len(usermail) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops",
                             message="Please don't leave any field empty!")

    else:
        is_ok = messagebox.askokcancel(title=website,
                               message=f"These are the details:\nEmail/Website: "
                               f"{website}\nPassword: {password}\nOK to save?")
        #Add data to the file if agreed
        if is_ok == True:
            with open(FILE_NAME, "a") as data_file:
                data_file.write(f"{website} | {usermail} | {password}\n")
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
website_label = Label(text="Website:", font=(FONT_NAME, 12), bg="white")
usermail_label = Label(text="Email/Username:", font=(FONT_NAME, 12), bg="white")
password_label = Label(text="Password:", font=(FONT_NAME, 12), bg="white")

#Entries x3
website_entry = Entry(width=35)
website_entry.focus()
usermail_entry = Entry(width=35)
usermail_entry.insert(0, "myusermail@domain.com")
password_entry = Entry(width=21)

#Buttons x2
add_button = Button(text="Add", highlightthickness=0, width=36, bg="white", command=save)
generate_pass_button = Button(text="Generate Password", highlightthickness=0,
                              bg="white", command=generate_password)

#Layout
canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
usermail_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)
website_entry.grid(row=1, column=1, columnspan=2)
usermail_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)
generate_pass_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
