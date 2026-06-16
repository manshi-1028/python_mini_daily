from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)

# Convert Function
def convert():
    miles = float(miles_input.get())
    km = round(miles * 1.60934, 2)
    km_result_label.config(text=str(km))

# Miles Input
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Miles Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Equal Label
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# Result Label
km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

# KM Label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Calculate Button
calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()
