import json
from random import *
from sqlite3 import Row
from tkinter import *
from tkinter import messagebox
from pandas import json_normalize
import pyperclip
import json

FONT=("Arial",12,"normal")
#-----------------------------SEARCH WEBSITE------------------------------------- #
def search():
    website=website_entry.get()
    try:
        
        with open("Password_Manager_project/data.json","r") as data_file:
            data=json.load(data_file)
            
            
    except FileNotFoundError:
        messagebox.showerror(title="oops" ,message="no such file exists ")
    else:
            try:
                messagebox.showinfo(title=website,message=data[website.title()])
            except KeyError:
                messagebox.showerror(title="oops" ,message="no such website exists in our data file")
                
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={website:{
            "email":email,
            "password":password
              }}
    
   
    if len(website)==0 or len(password)==0 or len (email)==0:
        messagebox.showerror("oops",message="please don't leave any field empty")
    else:
        
        is_ok=messagebox.askokcancel("Validation",
        message="These are the informations you want to save\n website :{website}\n email: {email}\password: {password} \n OK?? ")
        if is_ok:
            try:
            
                with open("Password_Manager_project/data.json","r") as data_file:
                    
                    #reading from the file
                    data=json.load(data_file)
                    #updating data
                    data.update(new_data)
            except FileNotFoundError:
                with open("Password_Manager_project/data.json","w") as data_file:
                    #writing the new data
                    json.dump(new_data,data_file,indent=4)
                
            else:
                
                with open("Password_Manager_project/data.json","w") as data_file:
                    #writing the new data
                    json.dump(data,data_file,indent=4)
                
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            email_entry.delete(0,END)
        
    



# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title('Password Manager')
window.config(padx=100,pady=30)

logo_image=PhotoImage(file="Password_Manager_Project/logo.png")
canvas=Canvas(width=220,height=200)
canvas.create_image(110,100,image=logo_image,anchor="center")
canvas.grid(row=0,column=1)




#labels
website_label=Label(text="Website :",font=FONT)
email_label=Label(text="Username/Email :",font=FONT)
password_label=Label(text="Password :",font=FONT)

#buttons
generate_password_button=Button(text="Generate Password",width=20,command=generate_password)
serach_button=Button(text="Search",width=20,command=search)
add_button=Button(text="Add",width=52,command=save_password)

#entries
website_entry=Entry(width=35)
website_entry.focus()
email_entry=Entry(width=60)
password_entry=Entry(width=35)





#Packing#
website_label.grid(row=1,column=0)
website_entry.grid(row=1,column=1)

email_label.grid(row=2,column=0)
email_entry.grid(row=2,column=1,columnspan=2)

password_label.grid(row=3,column=0)
password_entry.grid(row=3,column=1)

generate_password_button.grid(row=3,column=2)
add_button.grid(row=4,column=1,columnspan=2)
serach_button.grid(row=1,column=2)

window.mainloop()