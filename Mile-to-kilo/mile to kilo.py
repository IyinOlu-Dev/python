from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width= 300, height=100,)
window.config(padx=20, pady=20)

miles = Label(text="Miles")
miles.grid(row=0,column=2)

convert = Label(text="is equal to")
convert.grid(row=1,column=0)

km = Label(text="KM")
km.grid(row=1,column=2)

result = Label(text="")
result.grid(row=1,column=1)

def converter():
    converted=float(entry.get())
    converted = float(round(converted*1.60934,1))
    result.config(text=converted)



button = Button(text="click to convert", command=converter)
button.grid(row=2,column=1)

entry = Entry(width=10)
entry.grid(row=0,column=1)


window.mainloop()