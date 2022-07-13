"""
Exercise 25: Units of Time (Again)

In this exercise, you will reverse the process described in the previous exercise.

Develop a program that begins by reading a number of seconds from the user. Then your 
program should display the equivalent amount of time in the form D:HH:MM::SS, where
(D),(HH),(MM) and (SS) represents days, hours, minutes and seconds respectively.

The hours, minutes and seconds should all be formatted so that they occupy two digits, with
a leading 0 displayed if necessary.

"""

the_secs = int(input("Enter the number of seconds: "))

days = the_secs // 86400
left_secs = the_secs % 86400

hours = left_secs // 3600
left_secs = left_secs % 3600

mins = left_secs // 60
left_secs = left_secs % 60

secs = left_secs

print("%d secs = %d day : %02d hour : %02d minute : %02d second"%(the_secs,days,hours,mins,secs))

