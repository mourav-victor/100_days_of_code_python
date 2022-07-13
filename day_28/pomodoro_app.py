import time
from tkinter import *

## ---------------------------- CONSTANTS ------------------------------- ##
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 #* 60
SHORT_BREAK_MIN = 5 #* 60
LONG_BREAK_MIN = 20 #* 60
reps = 0
rest = FALSE

## ---------------------------- CONFIG TIMES ------------------------------ ## 
def new_window():

    def update_configs():
        global WORK_MIN
        global SHORT_BREAK_MIN
        global LONG_BREAK_MIN
        WORK_MIN = int(work_entry.get())
        SHORT_BREAK_MIN = int(break_entry.get())
        LONG_BREAK_MIN = int(rest_entry.get())

    newWindow = Toplevel(window)
    newWindow.title("Configuration")
    newWindow.config(padx=20,pady=15)

    Label(newWindow, text ="Work period: ").grid(column=0, row=0)
    Label(newWindow, text ="Break period: ").grid(column=0, row=1)
    Label(newWindow, text ="Rest period: ").grid(column=0, row=2)

    work_entry = Entry(newWindow, width=10)
    work_entry.insert(0, WORK_MIN)
    work_entry.grid(column=1, row=0)

    break_entry = Entry(newWindow, width=10)
    break_entry.insert(0, SHORT_BREAK_MIN)
    break_entry.grid(column=1, row=1)

    rest_entry = Entry(newWindow, width=10)
    rest_entry.insert(0, LONG_BREAK_MIN)
    rest_entry.grid(column=1, row=2)

    Label(newWindow, text ="", pady = 30).grid(column=0, row=3)

    Button(newWindow, text="Ok", padx=10, command=update_configs).grid(column=1, row=4)
 

## ---------------------------- TIMER MECHANISM -------------------------- ## 
def start_timer():
    if canvas.itemcget(timer_text, 'text') == "00:00":
        global reps
        global rest
        rest = FALSE
        reps += 1
        title.config(text="Work", fg=GREEN)
        count_down(WORK_MIN)
    
    
## ---------------------------- COUNTDOWN MECHANISM ---------------------- ## 
def count_down(count):
    global reps
    global rest
    secs = count % 60
    secs = str(secs) if secs >= 10 else f"0{secs}"
    mins = count // 60
    mins = str(mins) if mins >= 10 else f"0{mins}"
    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")

    if count > 0:
        window.after(1000, count_down, count-1)

    if count == 0:
        if not rest:
            title.config(text="Break", fg=PINK)
            marks = check_marks.cget("text") + "✔"
            check_marks.config(text=marks)
            rest = True

            if reps % 4 == 0:
                count_down(LONG_BREAK_MIN)
            else:    
                count_down(SHORT_BREAK_MIN)

        else:
            title.config(text="Reset!", fg=RED)


## ---------------------------- UI SETUP --------------------------------- ##

# Create window
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# Create title
title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
title.grid(column=1, row=0)

# Create canvas image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas_pic = PhotoImage(file="./day_28/tomato.png")
canvas.create_image(100, 112, image=canvas_pic)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Create buttons
button_start = Button(text="Start", padx=10, command=start_timer)
button_start.grid(column=0, row=3)
button_reset = Button(text="Reset", padx=10, command=start_timer)
button_reset.grid(column=2, row=3)
button_menu = Button(window, text="☰", padx=10, bg=YELLOW, command=new_window)
button_menu.grid(column=2, row=0)

# Create label for checkmarks
check_marks = Label(text="", bg=YELLOW, fg=GREEN, font=(22))
check_marks.grid(column=1, row=3)

#count_down(10)
window.mainloop()
