BACKGROUND_COLOR = "#B1DDC6"
import pandas as pd 
import random
from tkinter import *
#----------------------------------WORD RANDOMIZATION---------------------------------------------------------#

data = pd.read_csv("data/french_words.csv")
# print(data)

def word_random():
    record = data.to_dict(orient ="records")   
    origin_launguage = (random.choice(record)["French"])
    canvas.itemconfig(word, text = origin_launguage)
    canvas.itemconfig(launguage, text="French")
#--------------------------------------UI INTERFACE------------------------------------------------------------#

windows =Tk()
windows.title("Laungauge Translator")
windows.config(bg=BACKGROUND_COLOR, padx= 50, pady= 50)

canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2, padx=50)
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
canvas.create_image (400, 263, image= front)

checkmark = PhotoImage(file = "images/right.png")
right = Button(image=checkmark, command=word_random)
right.grid(column=1, row=1)


cross_image = PhotoImage(file="images/wrong.png")
wrong = Button(image= cross_image, command= word_random)
wrong.grid(column=0, row=1)



launguage = canvas.create_text(400, 150, text="Title",font=("Ariel", 40, "italic") )
word= canvas.create_text(400, 263, text= "Word", font= ("Ariel", 60, "bold"))

word_random()

windows.mainloop()