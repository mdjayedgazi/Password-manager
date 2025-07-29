from tkinter import*
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR -------------------------------#
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&' , '*', '+']

    nr_letters = random.randint(6, 9)
    nr_symbols = random.randint(3, 6)
    nr_numbers = random.randint(2, 5)

    password_list = []
    
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)
    password = "".join(password_list)
    pass_entry.delete(0,END)
    pass_entry.insert(0,password)
    try:
        pyperclip.copy(password)
    except pyperclip.PyperclipException:
        print("Password is still in the box — copy manually.")
        messagebox.showwarning(title="Clipboard Error", message="Could not copy password to clipboard.")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def Add():
    website = web_entry.get()
    email = email_user_entry.get()
    password = pass_entry.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password,
        }
    }
    if not website or not password:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\n Is it ok to save?")
        if is_ok:
            try:
                with open ("Password Data.json", "r") as pas:
                  #Reading old data
                    data = json.load(pas)
            except (FileNotFoundError, json.JSONDecodeError):
                data = {}
                #Updating old data with new data
            data.update(new_data)
            try:
                with open("Password Data.json","w") as pas:
                #Saving updated data
                    json.dump(data,pas,indent=4)
            except Exception as e:
                messagebox.showerror(title="Save Error", message=f"Something went wrong!\n\n{e}")
            else:
                messagebox.showinfo(title="Success", message="Password saved successfully!")
            finally:
                # remove all text 
                web_entry.delete(0,END)
                pass_entry.delete(0,END)
# ----------------------------------- FIND PASSWORD -----------------------------#
def find_password():
    website = web_entry.get()
    try:
        with open("Password Data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Not Found", message=f"No details for '{website}' exists.")
    # # ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.config(padx=50,pady=50)
root.columnconfigure(1, weight=1)
# Image
loc_img = PhotoImage(file="logo.png")
canvas = Canvas(height=200,width=200,highlightthickness=0)
canvas.create_image(100,100,image=loc_img)
canvas.grid(row=0,column=0,columnspan=3)
# Website
website_label = Label(text="Website:")
website_label.grid(column=0,row=1,pady=5,sticky='e')
web_entry = Entry(width=36,font=("Helvetica",12,"normal"))
web_entry.focus()
web_entry.grid(column=1,row=1,columnspan=2,sticky="ew",pady=5,ipady=2)
# Email/Username
email_user = Label(text="Email/Username:")
email_user.grid(column=0,row=2,pady=5,sticky="e")
email_user_entry = Entry(width=36,font=("Helvetica",12,"normal"))
email_user_entry.insert(END,"mdjayedgazi@gmail.com")
email_user_entry.grid(row=2,column=1,columnspan=2,sticky="we",pady=5,ipady=2)
# Password + Generate Button
password_label = Label(text="Password:")
password_label.grid(row=3,column=0,sticky="e",pady=5)
pass_entry = Entry(width=36,font=("Helvetica",12,"normal"))
pass_entry.grid(row=3,column=1,sticky="w",pady=5,ipady=2)
generate_pss = Button(text="Generate Password",command=password_generator)
generate_pss.grid(row=3,column=2,pady=5,sticky="e")
# Add Button
add = Button(text="Add",width=36,command=Add)
add.grid(row=4,column=1,columnspan=2,pady=5,sticky="ew",ipady=2)
# Search Button
search_button = Button(text="Search",command=find_password)
search_button.grid(row=1,column=2,sticky="ew",pady=5)

root.mainloop()