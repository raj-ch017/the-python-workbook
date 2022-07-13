"""
Exercise 29: Celsius to Fahrenheit and Kelvin

Write a program that begins by reading a temperature from the user in degrees Celsius. Then
your programn should display the equivalent temperature in degrees Fahrenheit and degrees Kelvin.
The calculations needed to convert between different units of temperature can be found on the
internet.

"""

temp_C = float(input("Enter the temperature in degree Celsius: "))

temp_F = (temp_C * 1.8) + 32
print("{} deg C = {} deg F".format(temp_C,temp_F))

temp_K = temp_C + 273.15
print("{} deg C = {} K".format(temp_C,temp_K))

