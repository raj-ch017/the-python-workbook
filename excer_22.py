"""
Exercise 22: Area of a Triangle (Again)

In the previous exercise, you created a program that computed the area of a triangle when the
length of its base and its height were known. It is also possible to compute the area of a 
triangle when the lengthsa of all three sides are known. 

Let (s1), (s2) and (s3) be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area
of the triangle can be calculated using the following formula:

        area = (s * (s-s1) * (s-s2) * (s-s3))**(0.5)

Develop a program that reads the lengths of the sides of a triangle from the user and
display its area.

"""

sideA = float(input("Enter length of side A: "))
sideB = float(input("Enter length of side B: "))
sideC = float(input("Enter length of side C: "))

total_s = (sideA + sideB + sideC) / 2

area = (total_s * (total_s - sideA) * (total_s - sideB) * (total_s - sideC))**(0.5)

print("Area of triangle: {} square unit".format(round(area,2)))