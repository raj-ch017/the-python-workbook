"""
Exercise 6: Tax and Tip

The program that you create for this exercise will begin by reading the cost 
of a meal ordered at a restaurant from the user. Then your program will compute
the tax and tip for the meal.
Use your local tax rate when computing the amount of tax owing. Compute the tip as
18% of the meal amount (without the tax).
The output from your program should include the tax amount, the tip amount, and the 
grand total for the meal, including both the tax and the tip.
Format the output so that all of the values are displayed using two decimal places.
"""

cost_meal = float(input("Enter the cost of your meal: "))
cost_tip = round((18*cost_meal) / 100,2)
print("The tip amount is ${}".format(cost_tip))

cost_mealtip = cost_meal + cost_tip

tax_charge = round((9*cost_mealtip) / 100,2)
print("The tax charged on your meal including tip is ${}".format(tax_charge))

total_cost = cost_mealtip + tax_charge
print("Grand Total is ${}".format(total_cost))


