from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


result_label = Label(text="is equal to")
result_label.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

result_unit = Label(text="Km")
result_unit.grid(column=2, row=1)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

def calculate():
    miles = float(miles_input.get())
    km = miles * 1.609
    result.config(text=f"{km}")


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()