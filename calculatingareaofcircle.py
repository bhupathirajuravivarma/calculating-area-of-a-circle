#python program to find area of a circle

# here we imported  the math module to get pi value from python library
import math

#read radius of the circle from user
radius = float(input("Enter the radius of the circle : "))

#calculate area
area = math.pi * radius * radius

#display the area of the circle
print("Area of the Circle is : {0}".format(area))



