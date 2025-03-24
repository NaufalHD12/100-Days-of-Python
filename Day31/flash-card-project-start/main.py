from tkinter import *
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"

# Load Data
data_directory = "flash-card-project-start/data/"
word_to_learn = os.path.join(data_directory, "words_to_learn.csv")
french_word_ori = os.path.join(data_directory, "french_words.csv")

try:
    df = pd.read_csv(word_to_learn)
    if df.empty:
        df = pd.read_csv(french_word_ori)
except (FileNotFoundError, pd.errors.EmptyDataError):
    df = pd.read_csv(french_word_ori)

data_dict = df.to_dict(orient="records")  # Mengonversi DataFrame ke list of dictionaries
random_word = {}

# ---------------------------- FUNCTIONS ------------------------------- #
def pick_random_word():
    """Memilih kata acak dan menampilkan dalam bahasa Prancis."""
    global random_word, flip_timer
    if not data_dict:
        canvas.itemconfig(title_text, text="Finished!", fill="black")
        canvas.itemconfig(word_text, text="No words left!", fill="black")
        return
    
    window.after_cancel(flip_timer)
    random_word = random.choice(data_dict)  # Perbarui kata acak
    
    # Ubah kartu ke depan
    canvas.itemconfig(card_image, image=card_front_image)  
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_word["French"], fill="black")

    # Setelah 3 detik, ubah ke bahasa Inggris
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    """Membalik kartu dan menampilkan kata dalam bahasa Inggris."""
    canvas.itemconfig(card_image, image=card_back_image)  # Ganti dengan gambar belakang
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=random_word["English"], fill="white")
    
def update_csv():
    global data_dict, random_word
    # membuat dictionary baru tanpa kata yang sudah dipelajari
    data_dict = [word for word in data_dict if word != random_word]
    new_df = pd.DataFrame(data_dict)
    
    new_df.to_csv("flash-card-project-start/data/words_to_learn.csv", index=False)
    
def handle_right_button():
    pick_random_word()
    update_csv()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

# Load Images
card_front_image = PhotoImage(file="flash-card-project-start/images/card_front.png")
card_back_image = PhotoImage(file="flash-card-project-start/images/card_back.png")

# Membuat Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front_image)  # Simpan ID gambar di canvas
canvas.grid(column=0, row=0, columnspan=2)

# Menambahkan teks ke dalam canvas
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Tombol Salah (Wrong)
wrong_image = PhotoImage(file="flash-card-project-start/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=pick_random_word)
wrong_button.grid(column=0, row=1, pady=25)

# Tombol Benar (Right)
right_image = PhotoImage(file="flash-card-project-start/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=handle_right_button)
right_button.grid(column=1, row=1, pady=25)

# Memulai dengan kata pertama
pick_random_word()

window.mainloop()
