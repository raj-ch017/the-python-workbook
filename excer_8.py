"""
Exercise 8: Widgets and Gizmos

An online retailer sells two products: widgets and gizmos.

Each widget weighs 75 grams. Each gizmo weighs 112 grams. 

Write a program that reads the number of widgets and the number of gizmos in an
order from the user. Then your program should compute and display the total 
weight of the order.

"""

weight_widget = 75
weight_gizmo = 112

num_widget = int(input("Enter the number of widgets in your order: "))
num_gizmo = int(input("Enter the number of gizmos in your order: "))

total_widget = weight_widget * num_widget
total_gizmo = weight_gizmo * num_gizmo
total = total_widget + total_gizmo
total_kg = total / 1000

print("The total weight of your order is {} grams ({} kgs)".format(total,total_kg))