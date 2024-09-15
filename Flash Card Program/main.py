## Imports
from tkinter import *
import pandas
import random


## FILES

# Images
FRONT_CARD_IMAGE_PATH = "Flash Card Program/images/card_front.png"
BACK_CARD_IMAGE_PATH = "Flash Card Program/images/card_back.png"
CORRECT_IMAGE_PATH = "Flash Card Program/images/right.png"
WRONG_IMAGE_PATH = "Flash Card Program/images/wrong.png"

# Data
DATA_PATH = "Flash Card Program/data/spanish_words.csv"
WORDS_LEFT_PATH = "Flash Card Program/data/words_to_learn.csv"

BACKGROUND_COLOR = "#B1DDC6"



## Stored Data

current_card = {}
words_to_learn = {}

# Reading the Data
try:
    data_df = pandas.read_csv(WORDS_LEFT_PATH)

except FileNotFoundError:
    original_data = pandas.read_csv(DATA_PATH)
    words_to_learn = original_data.to_dict(orient = "records")
else:
    words_to_learn = data_df.to_dict(orient = "records")



### ---------------------------------- ###

def know_card():
    words_to_learn.remove(current_card)

    words_left_to_learn = pandas.DataFrame(words_to_learn)
    words_left_to_learn.to_csv(WORDS_LEFT_PATH, index = False)

    next_card()


def flip_card():
    # Change the title to English
    canvas.itemconfig(title_text, text = f"English", fill="white")
    
    # Change the word
    english_word = current_card["English"]
    canvas.itemconfig(word_text, text = f"{english_word}", fill="white")

    # Display the back card
    canvas.itemconfig(flash_card, image=flash_card_back)



def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    current_card = random.choice(words_to_learn)

    spanish_word = current_card["Spanish"]

    canvas.itemconfig(title_text, text = f"Spanish", fill = "black")
    canvas.itemconfig(word_text, text = f"{spanish_word}", fill = "black")
    canvas.itemconfig(flash_card, image = flash_card_front)

    flip_timer = window.after(3000, func = flip_card)






### ----------- UI SETUP ------------ ###

# Window Setup
window = Tk()
window.title("Spanish Flash Cards")
window.config(padx = 50, pady = 50, background=BACKGROUND_COLOR)


flip_timer = window.after(3000, func = flip_card)


# Setup Canvas (Flash Card)
canvas = Canvas(width = 800, height = 526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_front = PhotoImage(file = FRONT_CARD_IMAGE_PATH)
flash_card_back = PhotoImage(file = BACK_CARD_IMAGE_PATH)

flash_card = canvas.create_image(400, 263, image=flash_card_front)

title_text = canvas.create_text(400, 150, text = "", fill="black", font = ("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text = "", fill="black", font = ("Ariel", 60, "bold"))

canvas.grid(row = 0, column = 0, columnspan=2)

# Incorrect Button

incorrect_image = PhotoImage(file=WRONG_IMAGE_PATH)
incorrect_button = Button(image=incorrect_image, bd = 0, highlightthickness = 0, command=next_card)
incorrect_button.grid(row = 1, column = 0)

# Correct Button
correct_image = PhotoImage(file=CORRECT_IMAGE_PATH)
correct_button = Button(image=correct_image, bd = 0, highlightthickness = 0, command = know_card)
correct_button.grid(row = 1, column = 1)


next_card()




window.mainloop()