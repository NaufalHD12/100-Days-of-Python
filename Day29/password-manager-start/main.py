from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = ([random.choice(letters) for _ in range(nr_letters)] + [random.choice(symbols) for _ in range(nr_symbols)] + [random.choice(numbers) for _ in range(nr_numbers)])


    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    
    pyperclip.copy(password)    
    password_entry.insert(0, password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox

def save():
    # Mengambil data dari entry pengguna
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    
    # Cek apakah ada field yang kosong
    if not website or not email or not password:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        return  # Hentikan eksekusi fungsi jika ada yang kosong

    # Konfirmasi sebelum menyimpan
    is_ok = messagebox.askokcancel(
        title=website, 
        message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\n\nSave this information?"
    )    

    # Jika pengguna memilih "OK", simpan ke file
    if is_ok:
        try:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")

            # Mengosongkan entry field setelah data disimpan
            website_entry.delete(0, END)
            password_entry.delete(0, END)

            # Memberikan notifikasi bahwa penyimpanan berhasil
            messagebox.showinfo(title="Success", message="Password saved successfully!")

        except Exception as e:
            messagebox.showerror(title="Error", message=f"An error occurred: {e}")

    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="Day29/password-manager-start/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="w")

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="w")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="w")

# Entries
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "hadinaufal06@gmail.com")  # Placeholder email

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3, sticky="w")

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()