"""
Exercise 11: Fuel Efficiency

In the United States, fuel efficiency for vehicles is normally expressed in miles-per-gallons.
In Canada, fuel efficiency is normally expressed in litres-per-hundred kilometers.

Use your research skills to determine how to convert from MPG to (L/100)km. 
Then create a program that reads a value from the user in American units and displays the 
equivalent fuel efficiency in Canadian Units.

"""

unit_american = float(input("Enter the fuel efficiency in miles-per-gallon: "))

units_canadian = unit_american * 235.215

print("The fuel efficiency in Canadian Units is {} litres/100 km.".format(round(units_canadian,3)))