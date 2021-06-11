# https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists#Swedish

# https://github.com/hermitdave/FrequencyWords/tree/master/content/2018

from tkinter import *
import pandas
import random

# --- CONSTANTS/INITIALIZATION --- #
BACKGROUND_COLOR = "#B1DDC6"

try:
    words_to_learn_df = pandas.read_csv("./data/words_to_learn.csv")

except FileNotFoundError:
    words_to_learn_df = pandas.read_csv(
        "./data/Swedish_Top500_FrequencyWords.csv")

finally:
    words_to_learn = words_to_learn_df.to_dict(orient="records")

word = {}
timer = None
FLIP_DELAY = 3000  # 3 seconds or 3000ms

# --- Functions --- #


def next_card():
    global word, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_img, image=card_front_img)
    word = random.choice(words_to_learn)
    canvas.itemconfig(language_label, text="Swedish", fill="black")
    canvas.itemconfig(word_label, text=word["Swedish"], fill="black")
    flip_timer = window.after(FLIP_DELAY, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=word["English"], fill="white")


def know_card():
    global word
    global words_to_learn
    words_to_learn.remove(word)
    words_to_learn_df = pandas.DataFrame(words_to_learn)
    words_to_learn_df.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# --- UI SETUP --- #
window = Tk()
window.title("Frequency Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(FLIP_DELAY, func=flip_card)

canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)

language_label = canvas.create_text(
    400, 150, text="Language", fill="black", font=("Arial", 40, "normal"))
word_label = canvas.create_text(
    400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR,
                      highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, bg=BACKGROUND_COLOR,
                      highlightthickness=0, command=know_card)
right_button.grid(column=1, row=1)

next_card()  # init the first card

window.mainloop()
