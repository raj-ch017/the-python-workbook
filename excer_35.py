"""
Exercise 35: Dog Years

It is commonly said that one human year is equivalent to 7 dog years. However, this simple 
conversion fails to recognize that dogs reach adulthood in approximately two years. As a 
result, some people believe that it is better to count each of the first two human years as 
10.5 dog years, and then count each additional human year as 4 dog years.

Write a program that implements the conversion from human to dog years described in the 
previous paragraph. Ensure that your program works correctly for conversions of less than
two human years and for conversions of two or more human years.
Your program should display an appropriate error message if the user enters a negative number.

"""

year = int(input("Enter human years: "))


if year > 2:
    diff = year - 2
    year1 = diff * 4
    total_years = year1 + 10.5
    print("Equivalent Dog years: {}".format(total_years))
elif year <= 2 and year >= 0:
    if year == 2:
        total_years = 10.5
        print("Equivalent Dog Years: {}".format(total_years))
    elif year == 1:
        total_years = 5.25
        print("Equivalent Dog Years: {}".format(total_years))
    elif year == 0:
        total_years = 0
        print("Equivalent Dog Years: {}".format(total_years))
else:
    print("Invalid input!")