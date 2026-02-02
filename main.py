from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps == 8:
        countdown(long_break_sec)
        my_label.config(text="Long break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        my_label.config(text="Short Break", fg=PINK)
    else:
        countdown(work_sec)
        my_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10 :
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)


my_label = Label(text = "TIMER", font= (FONT_NAME, 40, "bold") , fg=GREEN, bg=YELLOW)
my_label.grid(column=1, row=0)

tomato_img = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 128, text="00:00", font=(FONT_NAME,35,"bold"), fill="white")
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightthickness=0, command= start_timer)
start_btn.grid(column=0, row=3)
reset_btn = Button(text="Reset", highlightthickness=0,command= reset_timer)
reset_btn.grid(column=3, row=3)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=4)

window.mainloop()