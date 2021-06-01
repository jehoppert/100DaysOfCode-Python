from tkinter import *

def calculate():
  miles = int(input_miles.get())
  km = round(miles * 1.6)
  label_result.config(text=km)

#create the window for the program
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200,height=100)
#window.config(padx=20, pady=20)

#create components for window
input_miles = Entry(width=10)
input_miles.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_result = Label(text="0")
label_result.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1,row=2)

#keep the window open (end of program)
window.mainloop()