"""
#defaulting arguments
def add(n1=0, n2=2):
  print(n1 + n2)

add(n1=3)

#unlimited input arguments in a function - args = tuple ()
def add_many(*args):
  type(args) #list
  for n in args:
    print(n)

add_many(1, 4, 5, 7)

#unlimited keyword arguments in a function - kwargs = dict {}
def calculate(n, **kwargs):
  type(kwargs) #dictionary
  #for key,value in kwargs.items():
  #  print(key)
  n += kwargs["add"]
  n *= kwargs["multiply"]
  print(n)

calculate(2, add=3, multiply=5)

class Car: 
  
  def __init__(self, **kw):
    self.make = kw.get("make") #return None if not found in kw args
    self.model = kw.get("model")

  
my_car = Car(make="Nissan")
print(my_car.model) #prints None
"""
from tkinter import *

def button_clicked():
  label.config(text=input.get())

#create the window for the program
window = Tk()
window.title("My first GUI")
window.minsize(width=500,height=200)
window.config(padx=20, pady=20)

#create components for window
#label
label = Label(text="I am a label", font=("Arial", 24, "bold")) #create label object
label["text"] = "New Text"
label.config(text="Newer Text")
#label.pack(side="top")
label.grid(column=0, row=0)
label.config(padx=50,pady=50)

#button
button = Button(text="Click me", command=button_clicked)
button.place(x=200,y=150)

#entry
input = Entry(width=10)
input.grid(column=1, row=1)

#keep the window open (end of program)
window.mainloop()
  