from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Verdana"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""
circles = ""
checkmarks = ""


# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps, circles, checkmarks
    window.after_cancel(timer)
    reps = 0
    circles = ""
    checkmarks = ""
    b_start.config(state="normal", bg=GREEN)
    canvas.itemconfig(c_counter, text="25:00")
    l_title.config(text="Timer")
    l_checkmark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():
    global reps
    reps += 1
    b_start.config(state="disabled", bg=YELLOW)
    if reps % 2 != 0:
        count_down(WORK_MIN * 60)
        l_title.config(text=f"Work", fg=GREEN)
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        l_title.config(text="Break", fg=PINK)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        l_title.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(counter):
    global checkmarks, circles, timer
    c_min = floor(counter / 60)
    c_sec = counter % 60
    canvas.itemconfig(c_counter, text=f"{c_min:02d}:{c_sec:02d}")
    if counter > 0:
        timer = window.after(1000, count_down, counter - 1)
    else:
        if reps % 2 == 0 and reps % 8 != 0:
            checkmarks += "✔"
            l_checkmark.config(text=f"{circles}\n{checkmarks}")
        elif reps % 8 == 0:
            checkmarks = ""
            circles += "🟢"
            l_checkmark.config(text=f"{circles}\n{checkmarks}")
        timer_start()


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Jörg - The Pomodoro Technique")
window.minsize(width=200, height=465)
window.config(padx=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
c_counter = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 18, "bold"))
canvas.grid(column=1, row=1)

# Label
l_title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"), pady=20)
l_title.grid(column=1, row=0)

l_checkmark = Label(font=(FONT_NAME, 20, "bold"), pady=20, bg=YELLOW, fg=GREEN)
l_checkmark.grid(column=1, row=3)

# Buttons
b_start = Button(text="Start", command=timer_start, width=8, font=(FONT_NAME, 8, "normal"), bg=GREEN)
b_start.grid(column=0, row=2)
b_reset = Button(text="Reset", command=timer_reset, width=8, font=(FONT_NAME, 8, "normal"), bg=GREEN)
b_reset.grid(column=2, row=2)

window.mainloop()
