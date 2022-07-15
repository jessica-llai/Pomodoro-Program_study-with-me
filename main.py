from tkinter import *
from tkinter import Tk
from time import strftime
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    intro_Label.config(text="timer")
    Checker_Label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count = LONG_BREAK_MIN
        intro_Label.config(text="break", fg="#e7305b",
                            font=(FONT_NAME, 25, "normal"))
        intro_Label.grid(column=2, row=2)
    elif reps % 2 == 0:
        count = SHORT_BREAK_MIN
        intro_Label.config(text="break", fg="#e2979c",
                            font=(FONT_NAME, 25, "normal"))
        intro_Label.grid(column=2, row=2)


    else:
        count = WORK_MIN
        intro_Label.config(text="work", fg="#9bdeac",
                            font=(FONT_NAME, 25, "normal"))
        intro_Label.grid(column=2, row=2)


    count_down(60 * count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # ensure the double digit in sec
    canvas.itemconfig(time_text, text=f"{count_min}: {count_sec}")  # assign the count to the text on canvas
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # after 1000ms(1s), count reduced by 1
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)  # add the star every (work+break) loop
        for _ in range(work_sessions):
            mark += "🌟"
            Checker_Label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Study Timer")
window.config(padx=100, pady=50, bg="#E8E8CC")  # add padding


"""text and button"""

intro_Label = Label(text="Welcome to the Pomodoro Timer", fg="#66806A", bg="#E8E8CC",font=(FONT_NAME, 25, "normal"))
intro_Label.grid(column=2, row=1)

Checker_Label = Label(bg="#E8E8CC")
Checker_Label.grid(column=2, row=4)

start_button = Button(text="Start", bg="#e2979c", fg="#446A46", command=start_timer)
start_button.grid(column=1, row=4)
reset_button = Button(text="Restart", bg="#e2979c", fg="#446A46", command=reset_timer)
reset_button.grid(column=3, row=4)

"""tomato"""

tomato = PhotoImage(file="tomato.png")
canvas = Canvas(window,width = 220,height = 250, bg="#E8E8CC", highlightthickness=0)
canvas.create_image(103, 112, image=tomato)
time_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=3)





window.mainloop()