"""
Exercise 3: Area of a Room

Write a program that asks the user to enter the width and length of a room.
Once the values have been read, your program should compute and display the 
area of the room. 
The length and width will be entered as floating point numbers. Include units
in your prompt and output message; either feet or meters, depending on which 
unit you are more comfortable working with.

"""

in_length = float(input("Please enter the length of the room (in m): "))
in_width = float(input("Please enter the width of the room (in m): "))

area = round(in_length * in_width, 3)
print("The area of the room is {} square meter.".format(area))

