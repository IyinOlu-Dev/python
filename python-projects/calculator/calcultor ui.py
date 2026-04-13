import customtkinter as ctk

#Global Variables#
number = []

app = ctk.CTk()
app.title("Calculator")
# app.geometry("200x200")

#--------Functions-----#
def add(*args):
    if args <2 :
        print("error: arguement less than two")
    else:
        number.clear()
        print(number)
        return sum(args)
        

def divide(a,b):
    print(number)
    return (a/b)
    

#-------Numbers Function-------#
def add_digits(digits):
    number.append(digits)
    value=(int("".join(number)))
    entry_label.configure(text=value)
    print(value)
    return value

def one ():
    add_digits("1")

def two ():
    add_digits("2")

def three ():
    add_digits("3")

def four ():
    add_digits("4")

def five ():
    add_digits("5")

def six ():
    add_digits("6")

def seven ():
    add_digits("7")

def eight ():
    add_digits("8")

def nine ():
    add_digits("9")

def zero ():
    add_digits("0")

#--------UI Only------#
#--------Entry entry_label-----#
entry_label = ctk.CTkLabel(app, text="|")
entry_label.grid()

#--------Number Buttons------#
button1 = ctk.CTkButton(app, text="1", command= one)
button1.grid(row=2, column=1, pady=5, padx=10)

button2 = ctk.CTkButton(app, text="2", command=two)
button2.grid(row=3, column=1, pady=5, padx=10)

button3 = ctk.CTkButton(app, text="3", command=three)
button3.grid(row=4, column=1, pady=5, padx=10)

button4 = ctk.CTkButton(app, text="4", command=four)
button2.grid(row=2, column=2, pady=5, padx=10)

button5 = ctk.CTkButton(app, text="5", command=five)
button2.grid(row=3, column=2, pady=5, padx=10)

button6 = ctk.CTkButton(app, text="6", command=six)
button2.grid(row=4, column=1, pady=5, padx=10)

button7= ctk.CTkButton(app, text="7", command=seven)
button2.grid(row=4, column=1, pady=5, padx=10)

button8= ctk.CTkButton(app, text="8", command=eight)
button2.grid(row=4, column=1, pady=5, padx=10)


add_button = ctk.CTkButton(app, text="+", command=add)
add_button.grid(row=2, column=5)

division_button = ctk.CTkButton(app, text="/", command=divide)
division_button.grid(row=3, column=5)








app.mainloop()