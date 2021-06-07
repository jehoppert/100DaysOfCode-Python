from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# --- SEARCH FUNCTIONALITY --- #
def search():
  index = website_entry.get().title()

  try:
      #using a json file
      with open("./data.json", "r") as search_file:
        data = json.load(search_file) #read old json

  except FileNotFoundError:
    messagebox.showerror(title="Missing Data", message="No data file found")

  else:
    try:
      message = f"Email: {data[index]['email']}\nPassword: {data[index]['password']}"
      messagebox.showinfo(title=f"{index}", message=message)

    except KeyError:
      messagebox.showerror(title=f"{index}", message=f"{index} has no details saved")


# --- PASSWORD GENERATOR --- #
def password_gen():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_list = []

  password_list += [random.choice(letters) for _ in range(nr_letters)]

  password_list += [random.choice(symbols) for _ in range(nr_symbols)]

  password_list += [random.choice(numbers) for _ in range(nr_numbers)]

  random.shuffle(password_list)

  password = "".join(password_list)

  password_entry.delete(0, END)
  password_entry.insert(0, password)

  pyperclip.copy(password)

# --- ADD PASSWORD --- #
def add():

  website = website_entry.get().title()
  username = username_entry.get()
  password = password_entry.get()

  #setup json dict object
  new_data = {
    website: {
      "email": username,
      "password": password
    }
  }

  if len(website)==0 or len(password)==0:
    messagebox.showerror(title="Invalid inputs", message="Please populate all the fields in the form")

  else:

    try:
      #using a json file
      with open("./data.json", "r") as file:
        data = json.load(file) #read old json

    except FileNotFoundError:
      with open("./data.json", "w") as file:
        json.dump(new_data, file, indent=4)

    else:
      data.update(new_data)
      with open("./data.json", "w") as file:
        json.dump(data, file, indent=4) #write updated json

    finally:
      website_entry.delete(0, END)
      password_entry.delete(0, END)
      website_entry.focus()


# --- UI SETUP --- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=23)
website_entry.grid(column=1, row=1)
website_entry.focus() #default cursor to entry field

add_button = Button(text="Search", width=13, command = search)
add_button.grid(column=2,row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_entry = Entry(width=40)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "test@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=23)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", width = 13, command = password_gen)
generate_password_button.grid(column=2,row=3)

add_button = Button(text="Add", width=20, command = add)
add_button.grid(column=1,row=4)

window.mainloop()