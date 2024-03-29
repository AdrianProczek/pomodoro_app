from tkinter import *
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
REPS = 0
TIMER = NONE


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    label_title.config(text="Timer", fg=GREEN)
    label_checkmark.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 2 == 1:
        count_down(work_sec)
        label_title.config(text="Work", fg=GREEN)
    elif REPS % 8 == 0:
        count_down(long_break_sec)
        label_title.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        label_title.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_mic = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_mic}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            marks += "✔"
        label_checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label_title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
label_title.grid(column=1, row=0)

label_checkmark = Label(fg=GREEN, bg=YELLOW)
label_checkmark.grid(column=1, row=3)

button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

window.mainloop()
