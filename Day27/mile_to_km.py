from tkinter import *


def calculate():
    new_km_num = int(input.get()) * 1.6
    km_num.config(text=new_km_num)
    

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


input = Entry(width=10)
input.grid(column=1, row=0)
# input.config(padx=5, pady=5)

miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)
miles_text.config(padx=5, pady=5)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)
is_equal.config(padx=5, pady=5)

km_num = Label(text="0")
km_num.grid(column=1, row=1)
km_num.config(padx=5, pady=5)

km = Label(text="Km")
km.grid(column=2, row=1)
km.config(padx=5, pady=5)

calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)
calc_button.config(padx=5, pady=5)


window.mainloop()
