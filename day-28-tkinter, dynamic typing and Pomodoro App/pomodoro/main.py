from tkinter import *
import math

# --- CONSTANTS --- #
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

# --- TIMER RESET --- # 

def reset_timer():
  global reps
  window.after_cancel(timer)
  label_title.config(text="Timer", fg=GREEN)
  canvas.itemconfig(timer_text, text="00:00")
  label_check.config(text="")
  reps = 0
  

# --- TIMER MECHANISM --- # 
def start_timer():
  global reps
  reps += 1

  #work
  if reps % 2 == 1:
    label_title.config(text="Work", fg=GREEN)
    count_down(WORK_MIN * 60)
  #long break
  elif reps % 8 == 0:
    label_title.config(text="Break", fg=RED)
    count_down(LONG_BREAK_MIN * 60)
  #short break
  else:
    label_title.config(text="Break", fg=PINK)
    count_down(SHORT_BREAK_MIN * 60)

# --- COUNTDOWN MECHANISM --- # 
#looping simulation in tkinter
def count_down(count):
  global timer

  #format 00:00
  count_minutes = math.floor(count / 60)
  count_seconds = count % 60
  #dynamic typing - int to str
  if count_seconds < 10:
    count_seconds = f"0{count_seconds}"
  count_formatted = f"{count_minutes}:{count_seconds}"

  canvas.itemconfig(timer_text, text=count_formatted)

  if count > 0:
    timer = window.after(1000, count_down, count - 1)
  else:
    start_timer()
    work_sessions = "✔" * math.floor(reps/2)
    label_check.config(text=work_sessions)

# --- UI SETUP --- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_title = Label(text="Timer", font=(FONT_NAME,65,"bold"), fg=GREEN, bg=YELLOW)
label_title.grid(column=1, row=0)

canvas = Canvas(width=250, height=300, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="./tomato.png")
canvas.create_image(125,150, image=photo)
timer_text = canvas.create_text(125, 175, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="Start", command=start_timer, fg="black", highlightthickness=0, highlightbackground=YELLOW)
button_start.grid(column=0,row=2)

button_reset = Button(text="Reset", command = reset_timer, fg="black", highlightthickness=0, highlightbackground=YELLOW)
button_reset.grid(column=3,row=2)

label_check = Label(text="", fg=GREEN, bg=YELLOW)
label_check.grid(column=1, row=3)

window.mainloop()




