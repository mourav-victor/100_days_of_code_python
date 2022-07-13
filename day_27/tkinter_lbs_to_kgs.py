## TK-Inter GUI
from tkinter import *

# Create window
window = Tk()


# Configurate window
window.title("My GUI")
window.minsize(width=100, height=100)
window.config(padx=10, pady=5)


# Create labels
label = Label(text="Convertion GUI")
label.grid(column=1, row=0, pady=10)

label = Label(text="Lbs")
label.grid(column=2, row=1)

label = Label(text="Kgs")
label.grid(column=2, row=2)

label = Label(text="is equal to")
label.grid(column=0, row=2)

label_result = Label(text="")
label_result.grid(column=1, row=2)


# Create input
entry = Entry(width=10)
entry.grid(column=1, row=1)


# Create button
def button_func():
    lbl = float(entry.get())
    kg = str(round(lbl * 0.453592, 2))
    label_result.config(text=kg)
button = Button(text="Converter", command=button_func)
button.grid(column=1, row=3)


# At the very end
window.mainloop()