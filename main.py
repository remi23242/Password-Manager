from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "" . join(password_list)
    pyperclip.copy(password)

    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
          with open("day29/data.json", "r") as f:
               data = json.load(f)
            
    except FileNotFoundError:
         messagebox.showinfo(title="Oops", message="No data file found")
    else:

         if website in data:
            messagebox.showinfo(title="Found", message=f"Email:{data[website]['email']},Password: {data[website]['password']}")
         else:
              messagebox.showinfo(title=" Not Found", message="Message not found")
              
              
          


def add_button():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
        }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you havent left any fields empty!")
    else:
        try:
            with open("day29/data.json", "r") as f:
                # json.dump(new_data, f, indent=4)
                #Reading old data 
                data = json.load(f)
        except FileNotFoundError:
                with open("day29/data.json", "w") as f:
                    json.dump(new_data, f, indent=4)
               
        else:
             #Updating old data with new data
                data.update(new_data)
            
                with open("day29/data.json", "w") as f1:
                    json.dump(data, f1, indent=4)
    
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)



    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="day29/logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, "shoaibrizwan9@gmail.com")
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

 
password_button = Button(text="Generate Password", command=random_password)
password_button.grid(column=2, row=3)

search_button = Button(text="Search",width=15,command=find_password)
search_button.grid(column=2, row=1)


add_button = Button(text="Add", width=36, command=add_button)
add_button.grid(row=4, column=1, columnspan=2)






window.mainloop()