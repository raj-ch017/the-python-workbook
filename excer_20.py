"""
Exercise 20: Ideal Gas Law

The ideal gas law is a mathematical approximation of the behaviour of gases as pressure,
volume and temperature change. It is usually stated as:

    P * V = n * R * T

where (P) is the pressure in Pascals, (V) is the volume in litres, (n) is the amount of substance in moles, (R) is the ideal gas constant. equal to (8.314), and (T) is the 
temperature in degrees Kelvin.

Write a program that computes the amount of gas in moles when the user supplies the pressure,
volume and temperature. Test your program by determining the number of moles of gas in a 
SCUBA tank. A typical SCUBA tank holds 12 litres of gas at a pressure of 20,000,000 Pascals
(approximately 3000 PSI). Room temperature is approximately 20 degrees Celsius.

"""

gas_const = 8.314

pressure = float(input("Enter the pressure of the gas (in Pascals): "))
volume = float(input("Enter the volume of the gas (in litres): "))
temp = float(input("Enter the temperature of the gas (in Kelvin): "))

temp_c = temp - 273.15

moles = round((pressure * volume) / (gas_const * temp_c),3)
print("Pressure: {} pascals ".format(pressure))
print("Volume: {} litres".format(volume))
print("Temperature: {} kelvin.".format(temp))
print("Amount of moles: {}".format(moles))
