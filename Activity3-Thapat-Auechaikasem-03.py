# sequence
import math

# Triangle
# input
base = 45.9
height = 67.8
# process
triangle_area = 0.5 * base * height
# output
print("Area of Triangle is:", triangle_area)

print()

# Rectangle
# input
width = float(input("Width of Rectangle:"))
height = float(input("Height of Rectangle:"))
# process
rectangle_area = float(width) * float(height)
# output
print("Area of Square is:", rectangle_area)

print()

# Circle
# input
radius = float(input("Radius of Circle:"))
# process
circle_area = round(math.pi * radius ** 2, 2)
# output
print("Area of Circle is:", circle_area)

print()

# BMI
# input
weight = float(input("Weight in kg:"))
height = float(input("Height in cm:")) / 100
# process
bmi = weight / height ** 2
# output
print("BMI is:", round(bmi, 2))
