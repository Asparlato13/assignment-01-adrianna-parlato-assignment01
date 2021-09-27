import math
# Programming Assignment01-
# Team Members: Adrianna Parlato
# Course: CS151, Prof. Mehri
# Date: 09/27/2021
#ask user for dimensions of room
length = float(input("Enter the length of the room in feet: "))
width = float(input("Enter the width of the room in feet: "))
height = float(input("Enter the height of the room in feet: "))
# calculate the total area
dimensions_of_4_walls = 2*(length + width)*height
dimensions_of_ceiling = length * width
total_area = dimensions_of_ceiling + dimensions_of_4_walls
# display the total area
print("the total area is :", total_area,"feet")
# calculate how many gallons of paint and primer
primer = math.ceil(float(total_area/200))
paint = math.ceil(float(total_area/350))

# display how many gallons of primer and paint they will need to cover the total Area
print("You will need ", primer, "gallons of primer and ", paint, "gallons of paint")
