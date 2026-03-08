from tkinter import *


window=Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


red = Label(bg="red", width=12)
red.grid(row=1, column=1, columnspan=2)

blue = Label(width=5, bg="blue")
blue.grid(row=2, column=1)

green = Label(bg="green", width=5)
green.grid(row=2, column=2)


window.mainloop()