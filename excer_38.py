"""
Exercise 38: Month Name to Number of Days

The length of a month varies from 28 to 31 days. In this exercise, you will create a program
that reads the name of a month from the user as a string. Then your program should display 
the number of days in that month. Display "28 or 29 days" for February so that leap years
are addressed.

"""

month = input("Enter the name of a month: ").lower()

if month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":
    print("{} has 31 days.".format(month.title()))
elif month == "february":
    print("{} has 28 or 29 days".format(month.title()))
else:
    print("{} has 30 days".format(month.title()))

    