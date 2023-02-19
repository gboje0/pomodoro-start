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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    screen.after_cancel(timer)
    screen_background.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    pass_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 1
    short_break = SHORT_BREAK_MIN * 1
    long_break = LONG_BREAK_MIN * 1

    if reps % 8 == 0:
        countdown(long_break)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break)
        title_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text="work", fg=GREEN)
    # countdown(1 * 20)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
# allows the timer to show 00
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    screen_background.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = screen.after(1000, countdown, count -1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for n in range(work_session):
            marks += "✔"
        pass_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("pamadora")
screen.config(pady=50, padx=100, bg=YELLOW)
# screen.grid(column=1, row=1)

title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

screen_background = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
screen_background.create_image(100, 112, image=tomato_img)
timer_text = screen_background.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
screen_background.grid(column=1, row=1)


reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2,)

pass_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
pass_mark.grid(column=1, row=2)


screen.mainloop()