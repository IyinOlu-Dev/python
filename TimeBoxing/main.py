from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 40
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_func ():
    window.after_cancel(timer)
    canvas.itemconfig(start_text, text="00:00")
    REPS = 0
    heading_label.config(text= "Timer")
    check.config(text = "")
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    REPS  +=1
    if REPS %8 ==0:
        count_down(LONG_BREAK_MIN *60)
        REPS = 1
        heading_label.config(fg=PINK, text="Long Break")
    elif REPS %2 !=0:
        count_down(WORK_MIN *60)
        heading_label.config(fg=GREEN, text="Work")
    else:
        count_down(SHORT_BREAK_MIN *60)
        heading_label.config(fg=RED, text="Short Break")
    print(REPS)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60

    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(start_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()

        mark = ""
        work_sessions = math.floor(reps/2)
        for i in range (work_sessions):
            mark += "✅"
        check.config(text=mark)
        
        
        



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(height=200, width=200)
window.config(width=500, height=500, bg=YELLOW, padx=20, pady=20)



canvas = Canvas(width=202,height=224, bg=YELLOW,highlightthickness=0 )
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(102,112, image=tomato_img)
start_text = canvas.create_text(102,128,font=(FONT_NAME,35,"bold"),fill="white", text="00:00")
canvas.grid(row=1,column=1)

heading_label = Label(text="Timer", font=(FONT_NAME,45,"bold"),fg=GREEN, bg=YELLOW)
heading_label.grid(row=0,column=1)


start_buuton = Button(text="Start", command=start_timer, font=(FONT_NAME))
start_buuton.grid(row=2, column=0)

reset_button = Button(text="Reset",  font=(FONT_NAME), command= reset_func)
reset_button.grid(row=2, column=2)


check = Label(fg=GREEN, font=(35), bg=YELLOW)
check.grid(row=3,column=1) 


window.mainloop()