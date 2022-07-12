"""
Exercise 17: Heat Capacity

The amount of energy required to increase the temperature of one gram of a material by one
degree Celsius is the material's specific heat Capacity, C. The total amount of energy required
to raise (m) grams of a material by (del_T) degrees Celsius can be computed using the formula:

    q = m * C * (del_T)

Write a program that reads the mass of some water and the temperature change from the user. 
Your program should display the total amount of energy that must be added or removed to achieve the desired temperature change.

Extend your program so that it also computes the cost of heating water. Electricity is normally billed using units of kilowatt hours rather than Joules. In this exercise, you
should assume that electricity costs 8.9 cents per kilowatt hour. Use your program to compute
the cost of boiling water for a cup of coffee.

"""

mass = float(input("Enter the mass of water (in gms): "))
temp_change = float(input("Enter the change in temperature: "))

spec_heat = 4.186

energy = mass * temp_change * spec_heat

if energy > 0:
    print("The amount of energy that must be added is {} joules.".format(energy))
else:
    print("The amount of energy that must be removed is {} joules.".format(energy))

energy_kwhr = energy / (3.6 * 10**6)
cost = round(8.9 * energy_kwhr,2)

print("The cost of boiling {} grams of water is {} cents (${})".format(mass,cost,round((cost/100),2)))



