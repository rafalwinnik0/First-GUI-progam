from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(150, 80)
window.config(padx=20, pady=20)

def button_clicked():
    miles = int(input.get())
    km = 1.6 * miles
    label4.config(text=km)

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=2)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="Km")
label3.grid(column=2, row=1)

input = Entry(width=10)
input.grid(column=1, row=0)

label4 = Label(text="0")
label4.grid(column=1, row=1)

window.mainloop()
