from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters)for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = []

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data={
        website:{
            "email":email,
            "password":password,
        }
    }

    if len(website) == 0 or len(password)==0 or len(email) ==0:
        messagebox.showinfo(title="Empty Field", message="Please don't leave any field empty")
    else:
        try:
            with open ("data.json", "r") as data_file:
                data = json.load(data_file)               
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            password_entry.delete(0, END)
            email_entry.insert(0,"olutomiwa.oyegbola@gmail.com")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open ("data.json", "r") as data_file:
        data = json.load(data_file)
    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"email: {email}\n password: {password}")
    else:
        messagebox.showinfo(title="Error", message="Sorry, the website is not in memory")

# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image= lock_img)
canvas.grid(row=0, column=1)

website_label = Label (text="Website:")
website_label.grid(row=1, column=0, sticky="w")

website_entry = Entry(width=22)
website_entry.grid(row=1,column=1, sticky="w")
website_entry.focus()

search = Button(text="Search",highlightthickness=0, command=find_password, width=15)
search.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0,sticky="w")

email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w" )
email_entry.insert(0,"olutomiwa.oyegbola@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="w")

password_entry = Entry(width=22, highlightthickness=0,bd=1 )
password_entry.grid(row=3, column=1, sticky="w")

create_pass = Button(text="Generate Password", highlightthickness=0, command=generate_password)
create_pass.grid(row=3,column=2, sticky="w")

add_button = Button(width=36, text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()