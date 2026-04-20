import customtkinter as ctk

#-----Global Variables-------#
number = []
result = []

app = ctk.CTk()
app.title("Calculator.py")
app.resizable(False,False)
app.update()

#--------Functions-----#
def add_value(value) -> str:
    '''Returns an ineger of the value '''
    number.append(value)
    value=("".join(number))
    entry_label.configure(text=value)
    return value

def store_value ():
    '''Stores the number into result list'''
    if number:
        value = "".join(number)
        result.append(value)
        number.clear()
    if len(result) > 3:
        del result[0:3]

def calculate(res):
    a = float(res[0])
    b = float(res [2])
    op = res [1]
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b if b != 0 else "Error"


def answer():
    store_value()
    final_answer = calculate(result)
    result.append(final_answer)
    entry_label.configure(text=str(final_answer))
    del result[0:3]
    print(result)


#-------Numbers Function-------#


def one ():
    add_value("1")

def two ():
    add_value("2")

def three ():
    add_value("3")

def four ():
    add_value("4")

def five ():
    add_value("5")

def six ():
    add_value("6")

def seven ():
    add_value("7")

def eight ():
    add_value("8")

def nine ():
    add_value("9")

def zero ():
    add_value("0")

def decimal():
    add_value(".")
# ------Show operator function--------#



def add ():
    store_value()
    result.append("+")
    entry_label.configure(text = "+")

def subtract():
    store_value()
    result.append("-")
    entry_label.configure(text = "-")

def division ():
    store_value()
    result.append("/")
    entry_label.configure(text = "/")


def multiply ():
    store_value()
    result.append("*")
    entry_label.configure(text = "*")



#--------UI begins Here------#
#--------Entry entry_label-----#
entry_label = ctk.CTkLabel(app, text="|")
entry_label.grid(row=0, column=0, columnspan=6, sticky="ew", padx=0, pady=0)

#--------Number Buttons------#
button1 = ctk.CTkButton(app, text="1", command= one)
button1.grid(row=2, column=1, pady=5, padx=10)

button2 = ctk.CTkButton(app, text="2", command=two)
button2.grid(row=3, column=1, pady=5, padx=10)

button3 = ctk.CTkButton(app, text="3", command=three)
button3.grid(row=4, column=1, pady=5, padx=10)

button4 = ctk.CTkButton(app, text="4", command=four)
button4.grid(row=2, column=2, pady=5, padx=10)

button5 = ctk.CTkButton(app, text="5", command=five)
button5.grid(row=3, column=2, pady=5, padx=10)

button6 = ctk.CTkButton(app, text="6", command=six)
button6.grid(row=4, column=2, pady=5, padx=10)

button7= ctk.CTkButton(app, text="7", command=seven)
button7.grid(row=2, column=3, pady=5, padx=10)

button8= ctk.CTkButton(app, text="8", command=eight)
button8.grid(row=3, column=3, pady=5, padx=10)

button9 = ctk.CTkButton(app, text="9", command=nine)
button9.grid(row=4, column=3, pady=5, padx=10)

button_0 = ctk.CTkButton(app, text="0", command=zero)
button_0.grid(row=5, column=1,columnspan=2, sticky="ew", pady=5, padx=10)

decimal_button =ctk.CTkButton(app, text=".", command=decimal)
decimal_button.grid(row=5, column=3, pady=5, padx=10)

# -----Arithmetic Buttons-----------#

add_button = ctk.CTkButton(app, text="+", command=add)
add_button.grid(row=2, column=4, padx=15)

subtract_button = ctk.CTkButton(app, text="-", command=subtract)
subtract_button.grid(row=3, column=4, padx=15)

multiply_button = ctk.CTkButton(app, text="*", command=multiply)
multiply_button.grid(row=4, column=4, padx=15)

division_button = ctk.CTkButton(app, text="/", command=division)
division_button.grid(row=5, column=4, padx=15)

equals_button = ctk.CTkButton(app, text="=", command=answer)
equals_button.grid(row=2, column=5,rowspan=3,sticky="ns", padx=15)




app.mainloop()