"""
Exercise 14: Height Units

Many people think about their height in feet and inches, even in some countries that primarily use the metric system. 

Write a program that reads a number of feet form the user, followed by a number of inches.
Once these values are read, your program should compute and display the equivalent number
of centimeters.

"""

num_foot = int(input("Enter the units of feet for your height: "))
num_inches = float(input("Enter the units of iches for your height: "))

num_foot2cm = num_foot * 12 * 2.54
num_cm = num_inches * 2.54

total_cm = round(num_foot2cm + num_cm, 1)

print("Your height {} feet {} inches is equivalent to {} cm.".format(num_foot,num_inches,total_cm))

