"""
Exercise 30: Units of Pressure

In this exercise you will create a program that reads a pressure from the user in kilo-pascals.
Once the presdsure has been read your program should report the equivalent pressure in
pounds / square in, millimeters of mercury and atmospheres. 
Use your research skills to determine the conversion factors between these units.

"""

in_press = float(input("Please enter the pressure in kilo-pascals: "))

#converting kilo-pascal to pounds per square inch
press_1 = in_press * 0.145
print("{} kilopascals = {} pounds/sq in".format(in_press,press_1))

#converting kilo-pascal to milimeter of Mercury
press_2 = in_press * 7.500
print("{} kilopascals = {} mm Hg".format(in_press,press_2))

#conveting kilo-pascal to atmospheres
press_3 = in_press * 0.00986923
print("{} kilopascals = {} atmospheres".format(in_press,press_3))

