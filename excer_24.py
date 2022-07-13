"""
Exercise 24: Units of Time

Create a program that reads a duration from the user as a number of days, hours, minutes,
and seconds. Compute and display the total number of seconds represented by this duration.

"""

days = int(input("Enter the number of days: "))
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

the_sec = (days * 24 * 3600) + (hours * 3600) + (minutes * 60) + seconds

print("{} days : {} hours : {} minutes : {} seconds = {} seconds".format(days,hours,minutes,seconds,the_sec))

