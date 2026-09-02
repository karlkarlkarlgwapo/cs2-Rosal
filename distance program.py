
import math

#//Coordinates of Points//#

#Ask coordinates for point 1

point_x1 = float(input("Enter x1: "))
point_y1 = float(input("Enter y1: "))

#Ask coordinates for point 2

point_x2 = float(input("Enter x2: "))
point_y2 = float(input("Enter y2: "))

#//Compute the distance//#
#Compute the distance using the distance formula

point_x = point_x2 - point_x1
point_y = point_y2 - point_y1
point_xy = pow(point_x, 2) + pow(point_y, 2)
distance = math.sqrt(point_xy)

# Display the result rounded to two decimal places
print("The distance is: ", distance)


