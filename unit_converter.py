"""
Created on Tue Apr  6 13:20:56 2024

Title: Unit Converter
"""

import tkinter as tk
import pint


temp_conversion_factor = ['degC', 'degF', 'kelvin']
length_conversion_factor = ['meter', 'kilometer', 'centimeter',
                            'milimeter', 'micrometer', 'nanometer', 'inch', 'foot', 'yard']
wt_conversion_factor = ['kilogram', 'grams', 'miligrams', 'pounds']
time_conversion_factor = ['second', 'miliseconds',
                          'minute', 'hour', 'day', 'month', 'year']

result_label = None

def conversion(qty, qty_unit_from, qty_unit_to, window):
    try:
        value = float(qty.get())
    except ValueError:
        error_message = tk.Message(window, text="Invalid value. Please enter a number.", width=200, font=(
            'Helvetica', 10, 'bold'), bg='#FBFADA', fg='#12372A')
        error_message.grid(row=6, column=4, columnspan=2, pady=(10, 0))
        return
    unit_from = qty_unit_from.get()
    unit_to = qty_unit_to.get()

    u = pint.UnitRegistry() #creates an instance of pint
    qty = u.Quantity  #class that represnts phy qty with a specific value and unit
                      #helps in preformin arithematic operations
    if result_label:    #keeps track of the latest result label 
        result_label.destroy()
    
    l = qty(value, unit_from)   #object 
    converted_value = l.to(unit_to)
    
    
    result = tk.Label(window, text=converted_value)
    result.grid(row=5, column=5)


def time():
    window = tk.Toplevel()
    window.title('Weigth conversion')  # name of the page
    window.geometry('300x300')
    window.configure(bg="#FBFADA")

    
    fact = tk.Message(window, text=''' Sunlight is very old
Time passes faster for your face than for your feet
Einstein's theory of relativity states that time goes slower closer to the center of the Earth
Your language affects your perception of time
It may not be possible to have conscious experience without time
There's no such thing as a clock with 100% accuracy
The experience of time is actively created by our minds''', bg='#FBFADA', fg='#12372A')

    # title of the page
    tm_label = tk.Label(window, text='TIME CONVERSION', font=(
        'Helvetica', 20, 'bold'), bg='#FBFADA', fg='#12372A')

    # hedings
    tm_unit_label_1 = tk.Label(window, text='CONVERT FROM', font=(
        'Helvetica', 10, 'bold'), bg='#BFD8AF', fg='#12372A')

    tm_unit_label_2 = tk.Label(window, text='CONVERT TO', font=(
        'Helvetica', 10, 'bold'), bg='#BFD8AF', fg='#12372A')

    # storing options selected
    qty_unit_from = tk.StringVar()
    t_unit_from = tk.OptionMenu(
        window, qty_unit_from, *time_conversion_factor)
#The * operator unpacks the list, so each item in the list becomes a separate argument to the OptionMenu constructor.

    # storing unit to be converted to
    qty_unit_to = tk.StringVar()
    t_unit_to = tk.OptionMenu(
        window, qty_unit_to, *time_conversion_factor)

    # accepting the answers
    qty = tk.Entry(window)

    # Call the temp_conversion function with the 'temp' argument
    convert_button = tk.Button(window, text='Convert', command=lambda: conversion(qty, qty_unit_from, qty_unit_to, window))

    
    fact.grid(row=8, column=3)
    tm_label.grid(row=1, column=3)
    tm_unit_label_1.grid(row=3, column=4)   #convert_from
    tm_unit_label_2.grid(row=3, column=5)   #convert_to 
    t_unit_from.grid(row=4, column=4)
    t_unit_to.grid(row=4, column=5)
    qty.grid(row=5, column=4)
    convert_button.grid(row=5, column=6)




def wt():
    window = tk.Toplevel()
    window.title('Weight conversion')  # name of the page
    window.geometry('300x300')
    window.configure(bg="#FBFADA")

    

    fact = tk.Message(window, text='''1.	Weight is the measure of the force exerted by gravity on an object. It's different from mass, which is the amount of matter in an object.
2.	he standard unit of weight in the International System of Units (SI) is the Newton (N). In everyday use, weight is often measured in kilograms (kg) or pounds (lbs).
3.	The two primary units for measuring weight are the kilogram (kg) and the pound (lb). In the International System of Units (SI), the kilogram is the base unit of mass, while the pound is a unit commonly used in the imperial system.
4.	In the metric system, weight can be expressed using metric prefixes such as milligrams (mg), grams (g), kilograms (kg), metric tons (t), etc. These prefixes denote multiples or fractions of the base unit (kilogram).
5.	Unit conversion of weight is commonly encountered in various fields such as engineering, physics, chemistry, and everyday life. For instance, engineers may need to convert weight measurements when working with materials or designing structures using different unit systems.''', bg='#FBFADA', fg='#12372A')

    # title of the page
    w_label = tk.Label(window, text='WEIGHT CONVERSION', font=(
        'Helvetica', 20, 'bold'), bg='#FBFADA', fg='#12372A')

    # hedings
    w_unit_label_1 = tk.Label(window, text='CONVERT FROM', font=(
        'Helvetica', 10, 'bold'), bg='#BFD8AF', fg='#12372A')

    w_unit_label_2 = tk.Label(window, text='CONVERT TO', font=(
        'Helvetica', 10, 'bold'), bg='#BFD8AF', fg='#12372A')

    # storing options selected
    qty_unit_from = tk.StringVar()
    w_unit_from = tk.OptionMenu(window, qty_unit_from, *wt_conversion_factor)

    # storing unit to be converted to
    qty_unit_to = tk.StringVar()
    w_unit_to = tk.OptionMenu(window, qty_unit_to, *wt_conversion_factor)

    # accepting the answers
    qty = tk.Entry(window)

    # Call the temp_conversion function with the 'temp' argument
    convert_button = tk.Button(window, text='Convert', command=lambda: conversion(qty, qty_unit_from, qty_unit_to, window))

    
    fact.grid(row=8, column=10)
    w_label.grid(row=1, column=3)
    w_unit_label_1.grid(row=3, column=4)
    w_unit_label_2.grid(row=3, column=5)
    w_unit_from.grid(row=4, column=4)
    w_unit_to.grid(row=4, column=5)
    qty.grid(row=5, column=4)
    convert_button.grid(row=5, column=6)



def length():
    window = tk.Toplevel()
    window.title('Length conversion')  # name of the page
    window.geometry('300x300')
    window.configure(bg="#FBFADA")

    
    fact = tk.Message(window, text='''1.	
Length is a physical quantity that refers to the extent of something along its longest dimension.
2.	In physics, length is often treated as a vector quantity when considering its direction as well as magnitude. For example, in displacement or velocity calculations, length can have both magnitude (distance) and direction.
3.	he two primary units for measuring length are the meter (m) and the foot (ft). In the International System of Units (SI), the meter is the base unit of length, while the foot is a unit commonly used in the imperial system.
4.	In the metric system, length can be expressed using metric prefixes such as millimeters (mm), centimeters (cm), kilometers (km), etc. These prefixes denote multiples or fractions of the base unit (meter).
5.	To convert from one unit to another, you can use simple multiplication or division. For example, to convert 5 meters to feet, you would multiply 5 m by the conversion factor of 3.28084 ft/m to get approximately 16.4042 feet.''', bg='#FBFADA', fg='#12372A')

    # title of the page
    l_label = tk.Label(window, text='LENGTH CONVERSION', font=(
        'Helvetica', 20, 'bold'), bg='#FBFADA', fg='#12372A')

    # hedings
    l_unit_label_1 = tk.Label(window, text='CONVERT FROM', font=(
        'Helvetica', 10, 'bold'), bg='#BFD8AF', fg='#12372A')

    l_unit_label_2 = tk.Label(window, text='CONVERT TO', font=(
        'Helvetica', 10, 'bold'), bg='#BFD8AF', fg='#12372A')

    # storing options selected
    qty_unit_from = tk.StringVar()
    l_unit_from = tk.OptionMenu(
        window, qty_unit_from, *length_conversion_factor)

    # storing unit to be converted to
    qty_unit_to = tk.StringVar()
    l_unit_to = tk.OptionMenu(window, qty_unit_to,
                              *length_conversion_factor)

    # accepting the answers
    qty = tk.Entry(window)

    # Call the temp_conversion function with the 'temp' argument
    convert_button = tk.Button(window, text='Convert', command=lambda: conversion(qty, qty_unit_from, qty_unit_to, window))

    
    fact.grid(row=8, column=10)
    l_label.grid(row=1, column=3)
    l_unit_label_1.grid(row=3, column=4)
    l_unit_label_2.grid(row=3, column=5)
    l_unit_from.grid(row=4, column=4)
    l_unit_to.grid(row=4, column=5)
    qty.grid(row=5, column=4)
    convert_button.grid(row=5, column=6)


def temprature():
    window = tk.Toplevel()
    window.title('Temperature conversion')  # name of the page
    window.geometry('300x300')
    window.configure(bg="#FBFADA")

    
    fact = tk.Message(window, text=''' Water freezes at 0 °C and -32 °F.

Celsius is the world’s most common way of measuring temperature.

−89.2 °C (−128.6 °F) is the coldest temperature that has been ever recorded on Earth. It was recorded at Vostok Station located in Antarctica.

Absolute zero is the coldest theoretical temperature. When the substance reaches this temperature it does not possess any heat energy. It is defined as ‘Zero Kelvin’.''', bg='#FBFADA', fg='#12372A')

    # title of the page
    t_label = tk.Label(window, text='TEMPERATURE CONVERSION', font=(
        'Helvetica', 20, 'bold'), bg='#FBFADA', fg='#12372A')

    # hedings
    t_unit_label_1 = tk.Label(window, text='CONVERT FROM', font=(
        'Helvetica', 10, 'bold'), bg='#BFD8AF', fg='#12372A')

    t_unit_label_2 = tk.Label(window, text='CONVERT TO', font=(
        'Helvetica', 10, 'bold'), bg='#BFD8AF', fg='#12372A')

    # storing options selected
    qty_unit_from = tk.StringVar()
    t_unit_from = tk.OptionMenu(
        window, qty_unit_from, *temp_conversion_factor)

    # storing unit to be converted to
    qty_unit_to = tk.StringVar()
    t_unit_to = tk.OptionMenu(window, qty_unit_to, *temp_conversion_factor)

    # accepting the answers
    qty = tk.Entry(window)

    # Call the temp_conversion function with the 'temp' argument
    convert_button = tk.Button(window, text='Convert', command=lambda: conversion(qty, qty_unit_from, qty_unit_to, window))

    
    fact.grid(row=8, column=6)
    t_label.grid(row=1, column=3)
    t_unit_label_1.grid(row=3, column=4)
    t_unit_label_2.grid(row=3, column=5)
    t_unit_from.grid(row=4, column=4)
    t_unit_to.grid(row=4, column=5)
    qty.grid(row=5, column=4)
    convert_button.grid(row=5, column=6)


# parent window
root = tk.Tk()

root.title('Unit converter')  # name of the page
root.geometry('600x600')
root.minsize(300, 300)
root.configure(bg="#FFCDEA")

title = tk.Label(root, text='-----UNIT CONVERTER-----', font=('Helvetica',
                 25, 'bold'), bg="#FFCDEA", fg='#86469C').place(x=450, y=20)


temp_button = tk.Button(root, text='TEMPERATURE', font=20,
                        bg='#FB9AD1', width=15, command=temprature)
temp_button.place(x=530, y=80)


length_button = tk.Button(root, text='LENGTH', font=20,
                          bg='#FB9AD1', width=15, command=length)
length_button.place(x=530, y=130)


wt_button = tk.Button(root, text='WEIGHT', font=20,
                      bg='#FB9AD1', width=15, command=wt)
wt_button.place(x=530, y=180)


time_button = tk.Button(root, text='TIME', font=20,
                        bg='#FB9AD1', width=15, command=time)
time_button.place(x=530, y=230)

root.mainloop()
