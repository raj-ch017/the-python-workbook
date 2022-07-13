"""
Exercise 27: Body Mass Index

Write a program that computes the body mass index (BMI) of an individual. Your program should
begin by reading a height and weight from the user. Then it should use one of the following
two formulas to compute the BMI before displaying it. 

If you read the height in inches and the weight in pounds, then BMI is computed using:

        BMI = ((weight)/(height * height)) * 703

If you read the height in meters and the weight in kilograms, then BMI is computed using:

        BMI = (weight) / (height * height)

"""

height = float(input("Please enter the height (in inches or meter): "))
weight = float(input("Please enter the weight (in pounds or kgs): "))

height_units = input("What units did you use for height?:")
weight_units = input("What units did you use for weight?: ")

if height_units == "inches" or height_units == "in" and weight_units == "pound" or weight_units == "lb":
    index = ((weight)/(height*height)) * 703
    print("Height: {} in \nWeight: {} lb".format(height,weight))
    print("BMI: {}".format(round(index,2)))
elif height_units == "meters" or height_units == "m" and weight_units == "kilograms" or weight_units == "kg":
    index = (weight)/(height*height)
    print("Height: {} m \nWeight: {} kg".format(height,weight))
    print("BMI: {}".format(round(index,2)))
