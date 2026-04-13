from tkinter import *

window = Tk()
window.minsize(width=200, height=200)

my_label = Label(text="abab")
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Test")

def button_click():
    my_label.config(text="button result")
    result=input.get()
    my_label.config(text=result)


click = Button(text="click", command=button_click)
click.pack()


input = Entry(width=15)
input.pack()

window.mainloop()