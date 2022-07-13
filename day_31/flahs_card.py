import random
import time
import pandas as pd
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("./day_31/data/french_words.csv")
words  = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card
    if(canvas.itemcget(card_lang, 'text') == "English"):
        current_card = random.choice(words)
        canvas.itemconfig(card_lang, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")
        canvas.itemconfig(card_bg, image = canvas_pic_front)
        window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_lang, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image = canvas_pic_back)

def got_right():
    if(canvas.itemcget(card_lang, 'text') == "English"):
        words.remove(current_card)
        next_card()

## Create window
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


## Create canvas IMG logo
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_pic_front = PhotoImage(file="./day_31/images/card_front.png")
canvas_pic_back = PhotoImage(file="./day_31/images/card_back.png")
card_bg = canvas.create_image(400, 263, image=canvas_pic_front)
canvas.grid(column=0, row=0, columnspan=2)


## Create Labels
card_lang = canvas.create_text(400, 150, text="English", font=("Ariel", 30, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "italic"))


## Create Buttons
wrong_image = PhotoImage(file="./day_31/images/wrong.png")
right_image = PhotoImage(file="./day_31/images/right.png")
button_wrong = Button(image=wrong_image, command=next_card)
button_right = Button(image=right_image, command=got_right)
button_wrong.grid(row=1, column=0)
button_right.grid(row=1, column=1)



# # Create label for fields name
# label_website = Label(text="Website: ", bg="white")
# label_website.grid(column=0, row=1)
# label_email = Label(text="Username: ", bg="white")
# label_email.grid(column=0, row=2)
# label_password = Label(text="Password: ", bg="white")
# label_password.grid(column=0, row=3)

# # Create entry fields
# large_width = 40
# small_width = 30
# entry_website = Entry(width=small_width)
# entry_website.grid(column=1, row=1)
# entry_email = Entry(width=large_width)
# entry_email.insert(0,"moura.victor@udemy.com")
# entry_email.grid(column=1, row=2, columnspan=2)
# entry_password = Entry(width=small_width)
# entry_password.grid(column=1, row=3)

# # Create buttons
# button_width = 7
# button_genpass = Button(text="Generate", width = button_width, command= lambda: generate(PASSWORD_LENGTH))
# button_genpass.grid(column=2, row=3)
# button_search = Button(text="Search", width = button_width, command= search)
# button_search.grid(column=2, row=1)
# button_add = Button(text="Add", width=35, command=add)
# button_add.grid(column=1, row=4, columnspan=2, pady=10)

# # Create verification labels
# label_maj = Label(text="", fg="red", bg="white")
# label_maj.grid(column=1, row=5)
# label_num = Label(text="", fg="red", bg="white")
# label_num.grid(column=1, row=6)
# label_spe = Label(text="", fg="red", bg="white")
# label_spe.grid(column=1, row=7)

next_card()

window.mainloop()
