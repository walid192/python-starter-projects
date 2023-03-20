import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_UP="✔"
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    label.config(text="Timer",font=(FONT_NAME,35,"bold"))
    canvas.itemconfig(text_timer,text="00:00")
    global reps
    reps=0  
    check_up_canvas.config(text="")  
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    if reps%8==0:
        count_down(LONG_BREAK_MIN*60)
        label.config(text="Long break".upper(),fg=GREEN)
    elif reps%2==0:
        count_down(SHORT_BREAK_MIN*60)
        label.config(text="short break".upper(),fg=PINK)
        
    else:
        count_down(WORK_MIN*60)
        label.config(text="WORK",fg=RED)
    check_up_canvas.config(text=CHECK_UP*(reps//2))
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    
    if count>0:
        global timer
        canvas.itemconfig(text_timer,text=f"{count_min}:{count_sec}")
        timer=window.after(1000,count_down,count-1)
    if count==0:
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,45,"bold"))
label.grid(row=1,column=2)



tomato_img=PhotoImage(file="Pomodoro_Project/tomato.png")
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=tomato_img,anchor="center")
text_timer=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=2)
            


start_button=Button(text="start",command=start_timer,highlightthickness=0)
start_button.grid(row=3,column=1)


reset_button=Button(text="reset",highlightthickness=0,command=reset_timer)
reset_button.grid(row=3,column=3)

check_up_canvas=Label(text="",fg=GREEN)
check_up_canvas.grid(row=4,column=2)



window.mainloop()