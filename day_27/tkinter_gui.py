## TK-Inter GUI
import tkinter

# Create window
window = tkinter.Tk()

# Configurate window
window.title("My GUI")
window.minsize(width=400, height=300)

# Create label
label = tkinter.Label(text="Hello World", font=("Arial", 18, "italic"))
label.pack(side="top")
#label.pack(expand=True)

label_count = tkinter.Label(text="count: 0")
label_count.pack(side="bottom")

# Create button
count = 0
def button_func():
    global count
    count += 1
    label_count.config(text=f"count: {count}")
    print(f"Oh, you clicked me {count} times!")

button = tkinter.Button(text="click here", padx=10, command=button_func)
button.pack(side="bottom")

# create input
entry = tkinter.Entry(width=30)
entry.focus()
entry.pack()

# create radiobutton
def radio_clicked():
    entry.insert(1000, "@gmail.com")
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="gmail.com", value=1, variable=radio_state, command=radio_clicked)
radiobutton2 = tkinter.Radiobutton(text="hotmail.com", value=2, variable=radio_state, command=radio_clicked)
radiobutton3 = tkinter.Radiobutton(text="yahoo.com", value=3, variable=radio_state, command=radio_clicked)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()

# create checkbutton
checkbuton = tkinter.Checkbutton(text="I accept the terms")
checkbuton.pack()


# At the very end
window.mainloop()
