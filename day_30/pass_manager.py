## Password Generator GUI
import random
from tkinter import *
from tkinter import messagebox as mb
import json

from cv2 import FlannBasedMatcher

PASSWORD_LENGTH = 10
LETTERS = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "0123456789"
SPECIAL = "!@#$%&"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate(length):
    passw = random.choice(LETTERS.upper()) + random.choice(NUMBERS) + random.choice(SPECIAL)
    for i in range(length-len(passw)):
        passw += random.choice(LETTERS+NUMBERS+SPECIAL)
    entry_password.delete(0, END)
    entry_password.insert(0, passw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add(): 

    web = entry_website.get()
    user = entry_email.get()
    passw = entry_password.get()

    #mb.showerror("Answer", "Sorry, no answer available")
    #mb.showinfo(title="Confirm", message="Do you want to sabe this data?", options=Button(text="No"))
    confirm = mb.askokcancel(title="Confirm", message=f"Do you want to sabe this data?\n - user: {user}\n - password: {passw}")
    new_data = {
        web: {
            "email": user,
            "password": passw,
        }
    }

    if(confirm and len(web) and len(passw)):
        with open("./day_30/data.json", 'r') as file:
            data = json.load(file)
            data.update(new_data)

        with open("./day_30/data.json", 'w') as file:
            json.dump(data, file, indent = 4)
            entry_website.delete(0,END)
            entry_password.delete(0,END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():

    web = entry_website.get()
    user = entry_email.get()
    passw = entry_password.get()

    with open("./day_30/data.json", 'r') as file:

        data = json.load(file)

        try:
            passw = data[web]["password"]
        except:
            print("Website not found")
        else:
            print(data)
            print(data[web]["password"])
            print(data.keys())
            entry_password.delete(0,END)
            entry_password.insert(0,passw)


# ---------------------------- UI SETUP ------------------------------- #

# Create window
window = Tk()
window.title("PasswordManager App")
window.config(padx=100, pady=50, bg="white")

# Create canvas IMG logo
canvas = Canvas(width=200, height=224, bg="white", highlightthickness=0)
canvas_pic = PhotoImage(file="./day_29/logo.png")
canvas.create_image(100, 100, image=canvas_pic)
canvas.grid(column=1, row=0)

# Create label for fields name
label_website = Label(text="Website: ", bg="white")
label_website.grid(column=0, row=1)
label_email = Label(text="Username: ", bg="white")
label_email.grid(column=0, row=2)
label_password = Label(text="Password: ", bg="white")
label_password.grid(column=0, row=3)

# Create entry fields
large_width = 40
small_width = 30
entry_website = Entry(width=small_width)
entry_website.grid(column=1, row=1)
entry_email = Entry(width=large_width)
entry_email.insert(0,"moura.victor@udemy.com")
entry_email.grid(column=1, row=2, columnspan=2)
entry_password = Entry(width=small_width)
entry_password.grid(column=1, row=3)

# Create buttons
button_width = 7
button_genpass = Button(text="Generate", width = button_width, command= lambda: generate(PASSWORD_LENGTH))
button_genpass.grid(column=2, row=3)
button_search = Button(text="Search", width = button_width, command= search)
button_search.grid(column=2, row=1)
button_add = Button(text="Add", width=35, command=add)
button_add.grid(column=1, row=4, columnspan=2, pady=10)

# Create verification labels
label_maj = Label(text="", fg="red", bg="white")
label_maj.grid(column=1, row=5)
label_num = Label(text="", fg="red", bg="white")
label_num.grid(column=1, row=6)
label_spe = Label(text="", fg="red", bg="white")
label_spe.grid(column=1, row=7)



window.mainloop()
